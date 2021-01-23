def solution(total, coin):
    arr = [1] + [0]*total
    for c in coin:
        for i in range(c, total+1):
            arr[i] += arr[i-c]
    return arr.pop()