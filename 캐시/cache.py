def solution(cacheSize, cities):
    answer = 0
    cache=[]
    if cacheSize == 0:
        return len(cities)*5
    for c in cities:
        c=c.lower()
        if c in cache:
            cache.pop(cache.index(c))
            cache.append(c)
            answer += 1
        else:
            if len(cache)<cacheSize:
                cache.append(c)
            else:                
                cache=cache[1:]+[c]
            answer += 5
        
    return answer