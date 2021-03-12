def solution(bridge_length, weight, truck_weights):
    time=0
    queue=[0]*bridge_length
    s_queue=0
    while queue:
        time+=1
        s_queue-=queue.pop()
        if truck_weights:

            if truck_weights[0]+s_queue<=weight:
                s_queue+=truck_weights[0]
                queue.insert(0,truck_weights.pop(0))

            else:
                queue.insert(0,0)
    return time

print(solution(10,10,[7,4,5,6]))