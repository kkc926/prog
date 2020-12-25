import sys def solve(a, b, c): if b >= c: return -1 else: return a // (c - b) + 1 if __name__ == "__main__": _a, _b, _c = map(int, sys.stdin.readline().split()) print(solve(_a, _b, _c))
