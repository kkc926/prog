import sys
K = int(sys.stdin.readline())
number = list()
for i in range(K):
    N = int(sys.stdin.readline())
    if N == 0:
        number.pop(-1)
    else:
        number.append(N)
 
print(sum(number))