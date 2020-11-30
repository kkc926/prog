# map
```
def solution(n, arr1, arr2):
    answer = []
    for a1,a2 in zip(arr1,arr2):
        a12=str(bin(a1|a2))[2:]
        a12="0"*(n-len(a12))+a12
        a12=a12.replace('1','#')
        a12=a12.replace('0',' ')
        answer.append(a12)
    return answer
```

#### zip : 같은 타입의 배열 문자 등을 묶는다
    zip(arr1,arr2):

#### bin(2) 2진법의 수로 바꾸어 준다
    0b01

#### a12.replace('a','b') a12에 있는 모든 a를 b로 바꾸어 준다

#### a12=str(bin(a1|a2))[2:]
    [2:] str 데이터의 2번째 인덱스부터 슬라이싱한다


# 비밀지도
```
a,b=input().split()
a=int(a)
b=int(b)

print(a//b,a%b)
```

#### .split() : 입력받은 값을 분배하여준다
    a,b=input().split()
    10,2 를 입력받으면 a=10,b=2 

#### a//b
    몫만 출력
#### a%b
    나머지만 출력


# 문자열 나누기(split)
    ```
    >>> a = "Life is too short"
    >>> a.split()
    ['Life', 'is', 'too', 'short']
    >>> b = "a:b:c:d"
    >>> b.split(':')
    ['a', 'b', 'c', 'd']
    ```
    split 함수는 a.split()처럼 괄호 안에 아무 값도 넣어 주지 않으면 공백(스페이스, 탭, 엔터 등)을 기준으로 문자열을 나누어 준다. 만약 b.split(':')처럼 괄호 안에 특정 값이 있을 경우에는 괄호 안의 값을 구분자로 해서 문자열을 나누어 준다

# 문자열 뒤집기
```
text=input()

for i in range(len(text)-1,-1,-1):
	print(text[i],end='')
	
```
   for i in range(len(text)-1,-1,-1): -->맨뒤에 -1은 역순으로 돌리라는 뜻 

# map() 활용 : map(intstringfloat등등등,input()) 입력된 문자의 형식을 한번에 바꿔준다
```
    a,b,c=input().split())
    a=int(a)
    b=int(b)
    c=int(c)
```
```
    a,b,c=map(int,input().split())
```
    list도 적용가능
    ```
    li=list(map(int,input().split()))
    ```


# count() : 원하는 문자가 몇개 있는지 알려준다
```
text=I am a boy

print(text.count(a))

-->2개
```

# text=list(input()) : 입력받은 값을 list화 시킴
    print(text)
    ['a', 'a', 'a', 'a', 'D', 'D', 'D', 'D']

# sum() : list의 합을 구해준다
    sum(li)



# bin(),oct(),hex()2,8,16진수 변경 함수
    0b,0o,0x


# math 함수 중 pow, sqrt : pow는 제곱 sqrt는 제곱근
    math.pow(x,2) x를 제곱
    math.sqrt(x) 루트 x


# remove, count : list에서 사용가능 remove는 지정한 값을 1개 지워줌
```
text=list(input())

n=text.count(' ') # text.count -> 공백의 갯수를 카운트함(remove함수는 한개만 지우므로 루프를 돌려야함.)
for i in range(n):
	text.remove(' ') # 한개씩 지워줌
for x in text:
	print(x,end='')
```











