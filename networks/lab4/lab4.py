# -*- coding: utf-8 -*-

#
#  Created by Drapegnik on 06.03.17.
#

from math import log, floor

OCTET_LEN = 8
ADDR_LEN = OCTET_LEN * 4

inp_file = open('input.txt', 'r')
out_file = open('report.md', 'w')

# some magic with newline on end of file
end = open('input.txt', 'r+')
end.seek(-1, 2)
last = end.read(1)
if last != '\n':
    end.write('\n')


def _to_bin(x, write=False):
    """
    convert int from 10 base to 2
    :param x: int
    :param write: bool if write to output file
    :return: string bin_str
    """
    if x == 0:
        return '0' * 8

    first = True
    deg = int(floor(log(x, 2)))
    bin_x = ['0'] * (deg + 1)
    out_file.write('* `{} ='.format(x)) if write else None
    while x > 0:
        two_in_deg = 2 ** deg
        if x >= two_in_deg:
            x -= two_in_deg
            bin_x[deg] = '1'
            plus = '' if first else ' +'
            out_file.write('{0} {1} '.format(plus, two_in_deg)) if write else None
            first = False
        deg -= 1
    bin_x.reverse()
    bin_str = ''.join(bin_x)

    if len(bin_str) < 8:
        bin_str = '0' * (8 - len(bin_str)) + bin_str

    out_file.write('= {}`\n'.format(bin_str)) if write else None
    return bin_str


def check_if_ip(address):
    """
    check if valid ip address
    :param address: string address
    :return: bool
    """
    address_list = map(lambda x: int(x), address.split('.'))

    if len(address_list) != 4:
        return False
    for octet in address_list:
        if not 0 <= octet <= 255:
            return False
    if address_list[0] in [0, 10, 127, 255]:
        return False
    return True


def check_if_mask(address):
    """
    check if valid mask address
    :param address: string address
    :return: bool
    """
    bin_address = address_to_bin(address)
    bin_str = ''.join(bin_address.split('.'))
    i = 0
    while i < len(bin_str) and bin_str[i] == '1':
        i += 1

    if i == 0:
        return False

    for j in range(i, len(bin_str)):
        if bin_str[j] == '1':
            return False

    return True


def address_to_bin(address):
    """
    convert address to binary
    :param address: string address
    :return: binary string addres s
    """
    address_list = map(lambda x: int(x), address.split('.'))
    bin_list = map(_to_bin, address_list)
    bin = '.'.join(bin_list)
    return bin


def get_type(address):
    """
    get address type
    :param address:
    :return: string type one of 'VALID MASK', 'VALID IP', 'INVALID IP or MASK'
    """
    if check_if_mask(address):
        type = 'VALID MASK'
    elif check_if_ip(address):
        type = 'VALID IP'
    else:
        type = 'INVALID IP or MASK'
    return type


def get_addres_parts(ip, mask):
    """
    extract net and host parts of ip with mask info
    :param ip: string
    :param mask: string
    :return: string net, string host, int net_count, string count_string
    """
    ip_list = ip.split('.')
    mask_list = mask.split('.')
    net_size = 0
    for octet in mask_list:
        if octet != '255':
            break
        net_size += 1

    net = '.'.join(ip_list[:net_size])
    host = '.'.join(ip_list[net_size:])
    bit_count = OCTET_LEN * (4 - net_size)
    net_count = 2 ** bit_count - 2
    count_string = '2^{0}-2'.format(bit_count)
    return net, host, net_count, count_string


def _split_bin_str_on_ocsets(bin_str):
    """
    :param bin_str: str of with len=ADDR_LEN
    :return: list
    """
    return [bin_str[i:i + OCTET_LEN] for i in range(0, ADDR_LEN, OCTET_LEN)]


def _mask_from_size(size):
    """
    :param size: int mask size
    :return: list of string octets
    """
    bin_str = '1' * size + '0' * (ADDR_LEN - size)
    bin_list = _split_bin_str_on_ocsets(bin_str)
    return bin_list


def _address_from_bin_list(bin_list):
    """
    :param bin_list:
    :return: mask separated by point
    """
    return ".".join(map(lambda x: str(int(x, 2)), bin_list))


def _add_mask_to_ip(ip_bin_list, mask_size, char='0'):
    """
    :param ip_bin_list: list of binary octets
    :param mask_size: int mask_size
    :return: bin_ip_list
    """
    bin_str = ''.join(ip_bin_list)
    new_bin_str = bin_str[:mask_size] + char * (ADDR_LEN - mask_size)
    ip_list = _split_bin_str_on_ocsets(new_bin_str)
    return ip_list


def _get_additional_addrs(bin_ip_list, mask_size):
    """
    :param bin_ip_list: list bin address
    :param mask_size: int mask size
    :return: min, max, broadcast - adrress point separated
    """
    min_last_octet = bin_ip_list[-1][:-1] + '1'
    min = _address_from_bin_list(bin_ip_list[:-1] + [min_last_octet])

    brcst_bin_list = _add_mask_to_ip(bin_ip_list, mask_size, '1')
    broadcast = _address_from_bin_list(brcst_bin_list)

    max_last_octet = brcst_bin_list[-1][:-1] + '0'
    max = _address_from_bin_list(brcst_bin_list[:-1] + [max_last_octet])

    return min, max, broadcast


def extract_ip_and_mask(ip_with_mask):
    """
    parse '155.79.209.96/23' to ip and mask
    :param ip_with_mask: string address with mask after slash
    :return: dict result
        string ip,
        string mask,
        int net_count
        string max
        string min
        string broadcast
    """
    ip_list = ip_with_mask.split('.')
    ip_list[-1], mask_size = ip_list[-1].split('/')
    mask_size = int(mask_size)
    net_size = 2 ** (ADDR_LEN - mask_size) - 2
    bin_mask_list = _mask_from_size(mask_size)

    bin_ip_list = map(lambda x: _to_bin(int(x)), ip_list)
    bin_ip_list = _add_mask_to_ip(bin_ip_list, mask_size)
    min, max, broadcast = _get_additional_addrs(bin_ip_list, mask_size)

    results = {
        'ip': _address_from_bin_list(bin_ip_list),
        'mask': _address_from_bin_list(bin_mask_list),
        'net_size': net_size,
        'min': min,
        'max': max,
        'broadcast': broadcast
    }
    return results


# header
out_file.write('# lab4\n')
out_file.write('* *Пажитных Иван Павлович*\n')
out_file.write('* *3 курс, 1 группа, МСС*\n')
out_file.write('* [github lab link](https://github.com/Drapegnik/bsu/tree/master/networks/lab4)\n\n')

# task 1
out_file.write('## task1\n')
n = int(inp_file.readline())
for i in range(n):
    _to_bin(int(inp_file.readline()), write=True)

# task 2
out_file.write('\n## task2\n')
out_file.write('ip | binary | type\n')
out_file.write('--- | --- | ---\n')
n = int(inp_file.readline())
for i in range(n):
    address = inp_file.readline()[:-1]
    out_file.write('`{}` | '.format(address))
    bin_address = address_to_bin(address)
    type = get_type(address)
    out_file.write('`{0}` | {1}\n'.format(bin_address, type))

# task3
out_file.write('\n## task3\n')
n = int(inp_file.readline())
for i in range(n):
    out_file.write('name | value | binary\n')
    out_file.write('--- | --- | ---\n')

    ip = inp_file.readline()[:-1]
    mask = inp_file.readline()[:-1]
    if not check_if_mask(mask):
        raise ValueError('Not a mask, please pass VALID mask address')

    out_file.write('ip | `{0}` | `{1}`\n'.format(ip, address_to_bin(ip)))
    out_file.write('mask | `{0}` | `{1}`\n'.format(mask, address_to_bin(mask)))

    net, host, net_count, count_string = get_addres_parts(ip, mask)
    out_file.write('net part | `{0}` | `{1}`\n'.format(net, address_to_bin(net)))
    out_file.write('host part | `.{0}` | `.{1}`\n'.format(host, address_to_bin(host)))
    out_file.write('count of nets | `{0}` | `{1}`\n'.format(net_count, count_string))

# task4
out_file.write('\n## task4\n')
n = int(inp_file.readline())
for i in range(n):
    out_file.write('name | value\n')
    out_file.write('--- | ---\n')
    ip_with_mask = inp_file.readline()[:-1]
    out_file.write('ip/mask | `{}`\n'.format(ip_with_mask))
    results = extract_ip_and_mask(ip_with_mask)
    out_file.write('ip | `{}`\n'.format(results['ip']))
    out_file.write('mask | `{}`\n'.format(results['mask']))
    out_file.write('net size | `{}`\n'.format(results['net_size']))
    out_file.write('min addr | `{}`\n'.format(results['min']))
    out_file.write('max addr | `{}`\n'.format(results['max']))
    out_file.write('broadcast | `{}`\n\n'.format(results['broadcast']))
