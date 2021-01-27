def solution(number, k):
    answer = []
    
    # O(N)의 파싱
    for i, num in enumerate(number):
        # 가장 최근 넣은 값 보다 현재값이 크면 빼기, 빼야되는 수가 남아있으면
        while len(answer) > 0 and answer[-1] < num and k > 0 :
            answer.pop()
            k-=1 # 빼야되는 수 감소
        
        # 더이상 뺄게 없으면 남은 거 전부 추가
        if k == 0:
            answer += number[i:]
            break
            
        answer.append(num) # 추가
    
    # 만약 빼지 못했으면 삭제하기
    if k > 0 :
        answer = answer[:-k]
    
    return ''.join(answer)