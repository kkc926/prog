def cnt_alpha(name):
    LOVE = [0]*4
    
    for alpha in name:
        if alpha == 'L':
            LOVE[0] += 1
        elif alpha == 'O':
            LOVE[1] += 1
        elif alpha == 'V':
            LOVE[2] += 1
        elif alpha == 'E':
            LOVE[3] += 1
    return LOVE
        
def percentage(love):
    result = ((love[0]+love[1])*(love[0]+love[2])*(love[0]+love[3])*(love[1]+love[2])*(love[1]+love[3])*(love[2]+love[3]))%100
    res.append(result)
    return res
   
m_name = input()
N = int(input())
res = []
name_list = []
answer = []
 
for i in range(N):
    w_name = input()
    name_list.append(w_name)
    percentage(cnt_alpha(m_name+w_name))
    
max_p = max(res)
for j in range(N):
    if res[j] == max_p:
        answer.append(name_list[j])
        
answer.sort()
print(answer[0])
