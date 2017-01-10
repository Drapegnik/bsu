import math
import time


def get_dimensions(rows, size):
    """
    Count number of cols and rows for topology
    :param rows: number of rows
    :param size: number of process
    :return: number of rows and cols
    """
    comm_cols = int(math.sqrt(rows))

    while comm_cols > 1 and size % comm_cols:
        comm_cols -= 1

    return int(size / comm_cols), comm_cols


class Colors:
    HEADER = '\033[1;95m'
    OKBLUE = '\033[1;94m'
    OKGREEN = '\033[1;92m'
    WARNING = '\033[1;93m'
    FAIL = '\033[1;91m'
    CYAN = '\033[1;96m'
    ENDC = '\033[0m'


def formatting(rank, message):
    template = '${color} {name}{end_color}: {message}'

    return template.format(
        color=(Colors.FAIL if rank == 0 else Colors.OKGREEN),
        name=('master' if rank == 0 else 'proc{}'.format(rank)),
        end_color=Colors.ENDC,
        message=message
    )


def write_matrix(matrix, out):
    out.write('{}\n'.format(len(matrix)))
    for row in matrix:
        out.write(('{:.3f}\t' * len(matrix) + '\n').format(*row))


class Timer:
    def __init__(self, message):
        self.message = message
        self.start = time.time()

    def finish(self, rank):
        print formatting(
            rank, '{0}: {1:.3f}s'.format(self.message, (time.time() - self.start))
        )
