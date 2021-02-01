stack=[]
answer=[0 for _ in range(len(prices))]
for i in range(len(prices)):
    if len(stack)==0:
        stack.append((prices[i],i+1))
    else:
        if stack[-1][0]<=prices[i]:
            stack.append((prices[i],i+1))
        else:
            for j in range(len(stack)):
                if stack[-1][0]>prices[i]:
                    tmp = stack.pop()
                    answer[tmp[1]-1] = i+1-tmp[1]
                    if len(stack)==0:
                        stack.append((prices[i],i+1))
                else:
                    stack.append((prices[i],i+1))
                    break

for i in range(len(stack)):
    tmpstack = stack.pop()
    answer[tmpstack[1]-1] = len(prices) - tmpstack[1]