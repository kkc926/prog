a, b, c = input().split()
a = int(a); b = int(b); c = int(c)

max_ = max(a, b, c)
min_ = min(a, b, c)


print(a + b + c - max_ - min_)