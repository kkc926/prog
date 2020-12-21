def partial_sum(arr):
    arr = [0] + arr
    partial_sum = [0] * len(arr)
    
    for i in range(1, len(arr)):
        partial_sum[i] = partial_sum[i-1] + arr[i]
        
    partial_sum = partial_sum[1:]
    print("partial_sum", partial_sum)
    
    max_partial_sum = partial_sum[0]
    
    for b in range(0, len(arr)-1):
        for a in range(0, b):
            print(a, b, partial_sum[b] - partial_sum[a-1])
            max_partial_sum = max(max_partial_sum, partial_sum[b] - partial_sum[a-1])
            
    print("max partial sum", max_partial_sum)



scores = [-14, 7, 2, 10, -4, 9, -10]
print("list", scores)
partial_sum(scores)
#
list [-14, 7, 2, 10, -4, 9, -10]
partial_sum [-14, -7, -5, 5, 1, 10, 0]
0 1 -7
0 2 -5
1 2 9
0 3 5
1 3 19
2 3 12
0 4 1
1 4 15
2 4 8
3 4 6
0 5 10
1 5 24
2 5 17
3 5 15
4 5 5
0 6 0
1 6 14
2 6 7
3 6 5
4 6 -5
5 6 -1
max partial sum 24
