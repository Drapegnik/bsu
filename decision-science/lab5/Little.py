"""
    Branch and bound Little's Algorithm for Travelling Salesman Problem
        https://en.wikipedia.org/wiki/Branch_and_bound
        http://dspace.mit.edu/bitstream/handle/1721.1/46828/algorithmfortrav00litt.pdf
"""

INF = float('inf')
best_cost = 0


def subtract(min_el):
    return lambda x: x - min_el if x < INF else x


def reduce(size, w, row, col, rowred, colred):
    rvalue = 0
    for i in xrange(size):
        min_el = min(w[row[i]])
        if min_el > 0:
            w[row[i]] = map(subtract(min_el), w[row[i]])
            rvalue += min_el
        rowred[i] = min_el

    for j in xrange(size):
        min_el = min([w[row[i]][col[j]] for i in xrange(size)])
        if min_el > 0:
            for i in xrange(size):
                w[row[i]][col[j]] = subtract(min_el)(w[row[i]][col[j]])
            rvalue += min_el
        colred[j] = min_el
    return rvalue


def best_edge(size, w, row, col):
    mosti = -INF
    ri = 0
    ci = 0
    for i in xrange(size):
        for j in xrange(size):
            if not w[row[i]][col[j]]:
                minrowwelt = INF
                zeroes = 0
                for k in xrange(size):
                    if not w[row[i]][col[k]]:
                        zeroes += 1
                    else:
                        minrowwelt = min(minrowwelt, w[row[i]][col[k]])
                if zeroes > 1:
                    minrowwelt = 0
                mincolwelt = INF
                zeroes = 0
                for k in xrange(size):
                    if not w[row[k]][col[j]]:
                        zeroes += 1
                    else:
                        mincolwelt = min(mincolwelt, w[row[k]][col[j]])
                if zeroes > 1:
                    mincolwelt = 0
                if minrowwelt + mincolwelt > mosti:
                    mosti = minrowwelt + mincolwelt
                    ri = i
                    ci = j
    return mosti, ri, ci


def explore(n, w, edges, cost, row, col, best, fwdptr, backptr):
    global best_cost

    colred = [0 for _ in xrange(n)]
    rowred = [0 for _ in xrange(n)]
    size = n - edges
    cost += reduce(size, w, row, col, rowred, colred)
    if cost < best_cost:
        if edges == n - 2:
            for i in xrange(n):
                best[i] = fwdptr[i]

            avoid = 0 if w[row[0]][col[0]] >= INF else 1
            best[row[0]], best[row[1]] = col[1 - avoid], col[avoid]
            best_cost = cost
        else:
            mostv, rv, cv = best_edge(size, w, row, col)
            lowerbound = cost + mostv
            fwdptr[row[rv]] = col[cv]
            backptr[col[cv]] = row[rv]

            last = col[cv]
            while fwdptr[last] != INF:
                last = fwdptr[last]

            first = row[rv]
            while backptr[first] != INF:
                first = backptr[first]
            colrowval = w[last][first]
            w[last][first] = INF
            newcol = [INF for _ in xrange(size)]
            newrow = [INF for _ in xrange(size)]

            for i in xrange(rv):
                newrow[i] = row[i]
            for i in xrange(rv, size - 1):
                newrow[i] = row[i + 1]
            for i in xrange(cv):
                newcol[i] = col[i]
            for i in xrange(cv, size - 1):
                newcol[i] = col[i + 1]

            explore(n, w, edges + 1, cost, newrow, newcol, best, fwdptr, backptr)
            w[last][first] = colrowval
            backptr[col[cv]] = INF
            fwdptr[row[rv]] = INF

            if lowerbound < best_cost:
                w[row[rv]][col[cv]] = INF
                explore(n, w, edges, cost, row, col, best, fwdptr, backptr)
                w[row[rv]][col[cv]] = 0

    for i in xrange(size):
        for j in xrange(size):
            w[row[i]][col[j]] = w[row[i]][col[j]] + rowred[i] + colred[j]


def solve_tsp(w):
    global best_cost
    size = len(w)
    col = [i for i in xrange(size)]
    row = [i for i in xrange(size)]
    best = [0 for _ in xrange(size)]
    route = [0 for _ in xrange(size)]
    fwdptr = [INF for _ in xrange(size)]
    backptr = [INF for _ in xrange(size)]
    best_cost = INF

    explore(size, w, 0, 0, row, col, best, fwdptr, backptr)

    index = 0
    for i in xrange(size):
        route[i] = index
        index = best[index]

    path = []
    cost = 0
    for i in xrange(size):
        src = route[i]
        dst = route[i + 1] if i != size - 1 else 0
        cost += w[src][dst]
        path.append([src, dst])
    return cost, path
