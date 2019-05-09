from bisect import bisect_right
T = int(input())
for i in range(T):
    s = input().split()
    N = int(s[0])
    K = int(s[1])
    V = [int(vs) for vs in input().split()]
    
    E = []
    E.append(sum(V) / N)
    E.append(sum([max(v, E[0]) for v in V]) / N)
    V.sort()
    for k in range(2, K + 1):
        xk = bisect_right(V, E[k - 1])
        E.append(xk * E[k - 1] / N + sum(V[xk:]) / N)
    print('Case #%d: %.6f' % ((i + 1), E[K]))