import time

import numpy as np

from Little import atsp
from utils import read_graph_matrix

if __name__ == '__main__':
    m = read_graph_matrix('lab5.in')
    start_time = time.time()
    cost, path = atsp(m)
    print 'Cost = ', cost
    print 'Path = ', path
    print 'Time (s)', time.time() - start_time
