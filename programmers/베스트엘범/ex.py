def solution(genres, plays):
    S,L = {},{}
    
    for i in range(len(genres)):
        S[genres[i]] = S.get(genres[i],0) + plays[i]
        L[genres[i]] = L.get(genres[i],[]) + [(i,plays[i])]
    
    Best_genre = sorted(S.items(),key=lambda s:s[1],reverse=True)
    answer = []
    for G,_ in Best_genre:
        Music = sorted(L[G],key=lambda l:l[1],reverse=True)
        answer += [i for i,_ in Music[:2]]              
    return answer
