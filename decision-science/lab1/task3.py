out = open('output.txt', 'w')
H = [[14, -4, 2], [-4, 8, 8], [4, 4, 4], [2, 8, 2]]
p = [1./4, 0, 1./4, 1./2]
q = [1./3, 1./3, 1./3]

ans = 0
for i in range(4):
    for j in range(3):
        out.write('+ ({0}*{1}*{2:.2f}) '.format(H[i][j], p[i], q[j]))
        ans += H[i][j]*p[i]*q[j]

out.write('= {}'.format(ans))
