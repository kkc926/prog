def solution(n, edge):
    answer = 0
    node=[0 for _ in range(n)]

    node_edge=[[] for _ in range(n)]
    for i in range(len(edge)):
        node_edge[edge[i][0]-1].append(edge[i][1]-1)
        node_edge[edge[i][1]-1].append(edge[i][0]-1)
    visited_node=[]
    visited_node.append(0)
    node[0]=1
    tmp = 1
    while len(visited_node)!=0:
        count=0
        visit_count=len(visited_node)

        for i in range(visit_count):
            visit_start=visited_node.pop(0)

            for j in range(len(node_edge[visit_start])):
                if node[node_edge[visit_start][j]] == 0:
                    node[node_edge[visit_start][j]]=1
                    visited_node.append(node_edge[visit_start][j])
                    count+=1
                    tmp+=1

        if tmp==n:
            break
    answer=count

    return answer