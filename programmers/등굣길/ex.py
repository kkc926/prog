def solution(m, n, puddles):
    route = [[0] * (m + 1) for _ in range(n + 1)]  # 전체 지도를 만든다. 일단 방문한 적이 없으므로 모두 0을 준다.

    route[1][1] = 1  # 시작점으로 가는 방법은 총 1개가 있다. 바로 가만히 있기
    for i in range(1, n + 1):  # 1에서 n의 자리까지 모든 경우
        for j in range(1, m + 1):  # 1에서 m의 자리까지 모든 경우
            if i == 1 and j == 1:  # 만약, i,j 가 1 일때는 시작 지점이니 스킵
                continue
            if [j, i] in puddles:  # 물웅덩이가 있는 곳을 지나는 건0으로 친다.
                route[i][j] = 0
            else:  # 왼쪽으로 들어오는 경우와 위쪽에서 들어오는 경우를 합한다.
                route[i][j] += (route[i - 1][j] + route[i][j - 1])
    return (route[-1][-1]) % 100000007