#!/usr/bin/env bash
echo '## 2. `ipconfig`'
echo -e ' * ip-addres:\t\t\c'
printf '`%s`\n' `ipconfig getifaddr en0`

echo -e ' * subnet mask:\t\t\c'
printf '`%s`\n' `ipconfig getoption en0 subnet_mask`

echo -e ' * gateway:\t\t\c'
printf '`%s`\n' `route get default | awk '/gateway/{print $2}'`

echo -e ' * dhcp address:\t\c'
printf '`%s`\n' `ipconfig getoption en0 server_identifier`

echo -e ' * mac-address:\t\t\c'
printf '`%s`\n' `ifconfig en1 | awk '/ether/{print $2}'`

echo -e ' * dns-address:\t\t\c'
printf '`%s`\n\n' `ipconfig getoption en0 domain_name_server`