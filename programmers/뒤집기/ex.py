s = input()
a = []
for i in range(len(s) - 1):
    if s[i + 1] != s[i]:
        a.append(s[i])
a.append(s[-1])

print(min(a.count('1'), a.count('0')))