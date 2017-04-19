from graphviz import Digraph


def draw(file_name):
    g = Digraph('G', filename='{}.gv'.format(file_name), format='png')
    inp = file(file_name, 'r')
    n, m = map(lambda x: int(x), inp.readline().split())
    for _ in range(m):
        i, j, time, job_name = inp.readline().split()
        g.edge(i, j, label='{0}({1})'.format(job_name, time))
    g.render()

if __name__ == '__main__':
    draw('task1.in')
    draw('task2.in')
