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