# -*- coding: utf-8 -*- 
import sys _input = sys.stdin.readline()[:-1] #개행문자 제외 
cnt = [0, 0, 0, 0, 0, 0, 0, 0, 0] # 0부터 8까지 
for n in _input: 
    index = int(n) 
    if index == 9: 
        index = 6 # 9인 경우, 6으로 재할당 
    cnt[index] += 1 # counting 
cnt[6] = (cnt[6] + 1) // 2 # round() 함수는 쓰지 않음
print(max(cnt))

