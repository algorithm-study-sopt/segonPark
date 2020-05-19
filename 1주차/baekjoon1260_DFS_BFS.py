import sys

#정점의 개수, 간선의 개수, 탐색 시작할 정점의 번호
N, M, V = map(int, sys.stdin.readline().split())

#N+1을 하는 이유는 리스트의 인덱스가 0부터 시작하므로 순서상 헷갈리므로 1을 더해준다!
#즉, 1 2 3 4 5 노드에 각각 1 2 3 4 5를 넣어야 헷갈리지 않는다는 말!(원래의 리스트라면 인덱스 0 1 2 3 4에 1 2 3 4 5가 들어감)
graph_list = [set([]) for _ in range(N+1)]

#간선은 노드끼리의 연결을 의미하므로 a,b에 입력한 노드들은 서로 연결됨을 표시
for _ in range(M) :
    a, b = map(int, sys.stdin.readline().split())
    graph_list[a].add(b)
    graph_list[b].add(a)

def DFS(graph_list, start_node) :
    visit_node = []
    stack = [start_node]

    while stack :
        node = stack.pop()
        if node not in visit_node :
            visit_node.append(node)
            stack += sorted(list(graph_list[node] - set(visit_node)), reverse=True)
            #방금 넣은 node에 연결된 다른 노드 중 방문하지 않은 것들만 스택에 역정렬해서 넣는다.
    return visit_node

def BFS(graph_list, start_node) :
    visit_node = []
    queue = [start_node]

    while queue :
        node = queue.pop(0)
        if node not in visit_node :
            visit_node.append(node)
            queue += sorted(list(graph_list[node] - set(visit_node)))

    return visit_node

for i in list(DFS(graph_list, V)) :
    print(i, end =" ")
print()
for j in list(BFS(graph_list, V)) :
    print(j, end = " ")