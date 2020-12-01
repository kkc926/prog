text=input()
n=len(text)

for i in range(n):
	if i%2 ==0:
		print(text[i//2],end='')
	else:
		print(text[n-(i+1)//2],end='')

