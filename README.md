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



# 채점하기  point : split을 하면 입력값이 str로 리스트로 들어간다. 만약 ooooxoo를 입력받고 split()을 쓰면 ['ooooxoo']이 됨.
    ```
n=input()
s=0
score=0

for i in n:
	if i !='x':
		s += 1
		score +=s
		
	else:
		s=0
			
print(score)
    ```
    


# 문자열 번갈아 출력하기 point : 뒤에서 2칸걸러 값을 출력하고 싶으면 n-(i+1//2) 를 하면 된다.
```
text=input()
n=len(text)

for i in range(n):
	if i%2 ==0:
		print(text[i//2],end='')
	else:
		print(text[n-(i+1)//2],end='')


```

# 의좋은 형제 point : 25를 12, 13으로 나누고 싶을때는 25//2를 하고 나머지 25%2를 더하면 된다
```
a,b=map(int,input().split())
d=int(input())

for i in range(d):
	if i%2==0:
		b=b+a//2+a%2
		a=a//2
	else:
		
		a=a+b//2+b%2
		b=b//2
		
print(a,b)
```


# 부분문자열 point : 슬라이싱 방법 print(text[:i+1]) -->text[start:end:step]
``` 
text=str(input())


for i in range(len(text)):
	print(text[:i+1])
```

# 3n+1 point : for 문 안에 while 문을 넣을때 만약 i 를 기준으로 돌린다면 n=i로 새로운 변수를 써야 for문이 안꼬임
```
a,b=map(int,input().split())
count=0
li=[]
for i in range(a,b+1):
	count=0
	n=i
	while (n!=1):
		if n%2==0:
			n=n/2
		else:
			n=n*3+1
		count += 1
	count +=1
	li.append(count)
		
print(max(li))
```
# 유일한 수 point : count함수 사용 li.count(i)==1: li라는 리스트에 i라는 인수가 1개면
```
n=int(input())
li=list(map(int,input().split()))


for i in li:
	if li.count(i)==1:
		print(i)
	

```


# 소수의 갯수 구하기 point : check = True 이용하기 // 소수는 1과 자기자신으로 나눴을때 나머지가 0인수 따라사 2개를 범위에서 빼서 생각해보기
```
n=int(input())
count=0

for i in range(2,n+1):
	check=True
	for j in range(2,i):
		if i%j==0:
			check=False
	if check==True:
		count += 1
print(count)
```





