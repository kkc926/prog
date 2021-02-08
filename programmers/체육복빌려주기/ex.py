def solution(n, lost, reserve):
    clothes_list = [1]*n         

    for i in reserve:             
        clothes_list[i-1] = 2

    for i in lost:           
        clothes_list[i-1] = clothes_list[i-1]-1

    for index,value in enumerate(clothes_list):    
        if index > 0 and value == 0 and clothes_list[index-1]==2:  
            clothes_list[index] = 1                                
            clothes_list[index-1] =1                                
        elif index < n-1 and value == 0 and clothes_list[index+1]==2:
            clothes_list[index] = 1
            clothes_list[index+1] =1

    return n-clothes_list.count(0) 