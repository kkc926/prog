def solution(m, n, puddles):
    route = [[0] * (m + 1) for _ in range(n + 1)]


    route[1][1] = 1


    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            if [j, i] in puddles:
                route[i][j] = 0
            else:
                route[i][j] += (route[i - 1][j] + route[i][j - 1])


    return (route[-1][-1]) % 100000007