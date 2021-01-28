def solution(name):
    answer = 0
    strSol = ['A'] * len(name)
    same = [False] * len(name)   # 같아졌는지
    cursor = 0
    
    # 다른 곳 파싱
    for a in range(len(name)):
        if strSol[a] != name[a]:
            same[a] = False # 다름
        else:
            same[a] = True # 같음
    
    while(True):
        # 같을 때 까지 진행
        if((False in same) is False):
            break
        
        # 가장 가까운 곳 찾아서
        diff = 0
        while(True):
            if(same[cursor] == False):
                break
                
            # 안될 경우 diff 증가
            diff += 1

            # 오른쪽 이동
            if ( same[(cursor + diff) % len(name)] == False) :
                cursor =  (cursor + diff) % len(name)
            
            # 왼쪽 이동
            elif ( same[(cursor - diff) % len(name)] == False) :
                cursor =  (cursor - diff) % len(name)
            
        
        # 해당 변경
        answer += diff
        name_char = ord(name[cursor]) - ord('A') # A로부터 올라가기
        z_char = ord('Z') - ord('A') +1 # Z로부터 내려가기
        answer += min(name_char, (z_char - name_char))
        strSol[cursor] = name[cursor]
        same[cursor] = True
                
    
    return answer