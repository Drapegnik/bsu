import time

import numpy as np

from Little import atsp
from utils import read_graph_matrix, draw_graph_with_path

if __name__ == '__main__':
    m = read_graph_matrix('lab5.in')
    out = file('report.md', 'w')
    out.write('# lab5\nPazhitnykh Ivan\n\n* Solve **Travelling Salesman Problem**, with matrix:\n')
    out.write('```\n{}\n```\n'.format(np.array(m)))

    start_time = time.time()
    cost, path = atsp(m)
    print 'Cost = ', cost
    print 'Path = ', path
    print 'Time (s)', time.time() - start_time

    out.write('* Branch and bound tree:\n')
    out.write('![](http://res.cloudinary.com/dzsjwgjii/image/upload/v1492168988/ds-lab5.png)\n')

    draw_graph_with_path(m, path)
    out.write('* Graph with Hamilton cycle fot TSP:\n')
    out.write('![](https://raw.githubusercontent.com/drapegnik/bsu/master/decision-science/lab5/out/lab5.gv.png)\n')

    out.write('\n* Minimal cost:\n')
    sum = 0
    expression = ''
    for i, j in path:
        expression = '{} + {}'.format(expression, int(m[i][j]))
        sum += m[i][j]
    out.write('`C = {0} = {1}`'.format(expression[2:], int(sum)))
