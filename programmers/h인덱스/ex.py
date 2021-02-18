def solution(citations):

    if min(citations) >= len(citations): answer = len(citations)
    else: answer = 0
    citations = sorted(citations)






    for i in range(min(citations), max(citations) + 1):
        left = 0
        right = 0
        for j in citations:
            if j <= i: left += 1
            if j >= i: right += 1
        if (left <= i) & (right >= i):
            answer = max(answer, i)
    return answer