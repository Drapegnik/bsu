import numpy as np


def edges_list_to_matrix(filename):
    inp = file(filename, 'r')
    n, m = map(lambda x: int(x), inp.readline().split())
    t = np.ndarray((n, n))
    t.fill(-1)
    for _ in range(m):
        i, j, time = map(lambda x: int(x), inp.readline().split())
        t[i][j] = time
    return t


def format_array(array, prefix):
    return '\t'.join(map(lambda (ind, x): '{0}[{1}]={2}'.format(prefix, ind, x), enumerate(array)))


def print_matrix(matrix, time_matrix, prefix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if time_matrix[i][j] != -1:
                print '\t{0}({1}, {2}) = {3}'.format(prefix, i, j, matrix[i][j])
    print


def count_params(filename):
    time_matrix = edges_list_to_matrix(filename)
    n = len(time_matrix)

    events_early_terms = np.array([-float('inf') for _ in range(n)])
    events_early_terms[0] = 0
    for i in range(n):
        for j in range(n):
            if time_matrix[j][i] != -1:
                events_early_terms[i] = max(events_early_terms[i], events_early_terms[j] + time_matrix[j][i])
    print 'Events early terms:\t\t{}'.format(format_array(events_early_terms, prefix='Tp'))

    events_late_terms = np.array([float('inf') for _ in range(n)])
    events_late_terms[n - 1] = events_early_terms[n - 1]
    for i in reversed(range(n)):
        for j in range(n):
            if time_matrix[i][j] != -1:
                events_late_terms[i] = min(events_late_terms[i], events_late_terms[j] - time_matrix[i][j])
    print 'Events late terms:\t\t{}'.format(format_array(events_late_terms, prefix='Tn'))

    events_time_reserves = map(lambda (early, late): late - early, zip(events_early_terms, events_late_terms))
    print 'Events time reserves:\t{}\n'.format(format_array(events_time_reserves, prefix='R'))

    jobs_early_terms_start = np.ndarray((n, n))
    jobs_early_terms_finish = np.ndarray((n, n))
    jobs_late_terms_start = np.ndarray((n, n))
    jobs_late_terms_finish = np.ndarray((n, n))
    jobs_summary_reserves = np.ndarray((n, n))
    jobs_free_reserves = np.ndarray((n, n))
    jobs_independent_reserves = np.ndarray((n, n))
    jobs_guaranteed_reserves = np.ndarray((n, n))

    for i in range(n):
        for j in range(n):
            if time_matrix[i][j] == -1:
                continue

            jobs_early_terms_start[i][j] = events_early_terms[i]
            jobs_early_terms_finish[i][j] = events_early_terms[i] + time_matrix[i][j]

            jobs_late_terms_start[i][j] = events_late_terms[j] - time_matrix[i][j]
            jobs_late_terms_finish[i][j] = events_late_terms[j]

            jobs_summary_reserves[i][j] = events_late_terms[j] - events_early_terms[i] - time_matrix[i][j]
            jobs_free_reserves[i][j] = events_early_terms[j] - events_early_terms[i] - time_matrix[i][j]
            jobs_independent_reserves[i][j] = max(0, events_early_terms[j] - events_late_terms[i] - time_matrix[i][j])
            jobs_guaranteed_reserves[i][j] = events_late_terms[j] - events_late_terms[i] - time_matrix[i][j]

    jobs_params_titles = ['Jobs early terms start:', 'Jobs early terms finish:', 'Jobs late terms finish:',
                          'Jobs late terms finish:', 'Jobs summary reserves:', 'Jobs free reserves:',
                          'Jobs independent reserves:', 'Jobs guaranteed reserves:']
    jobs_params_values = [jobs_early_terms_start, jobs_early_terms_finish, jobs_late_terms_finish,
                          jobs_late_terms_finish, jobs_summary_reserves, jobs_free_reserves,
                          jobs_independent_reserves, jobs_guaranteed_reserves]
    jobs_params_names = ['Tps', 'Tpf', 'Tns', 'Tnf', 'Rs', 'Rf', 'Rn', 'Rg']

    for title, matrix, prefix in zip(jobs_params_titles, jobs_params_values, jobs_params_names):
        print title
        print_matrix(matrix, time_matrix, prefix=prefix)


if __name__ == '__main__':
    # task 1
    print '-'*100
    print 'task1:\n'
    count_params('task1.in')
    print '-'*100
    print 'task2:\n'
    count_params('task2.in')
    print '-'*100
