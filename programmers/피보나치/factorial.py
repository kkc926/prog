N = int(input())
F0, F1 = 0, 1
for i in range(N):
    F0, F1 = F1, F0+F1
print(F0)