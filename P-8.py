def DFS2(graph, v, visited):
    if v not in visited:  # v가 방문되지 않았으면
        visited.add(v)  # v를 방문했다고 표시
        print(v, end=' ')  # v를 출력
        nbr = sorted(set(graph[v]) - visited)  # v의 인접 정점 리스트를 정렬
        for u in nbr:  # v의 모든 인접 정점에 대해
            DFS2(graph, u, visited)  # 순환 호출
              # queue 모듈의 Queue 사용
import queue
def BFS(graph, start_vertex):
    visited = {vertex: False for vertex in graph}  # 방문 확인을 위한 딕셔너리 생성
    vertex_queue = queue.Queue()  # 공백상태의 큐 생성
    vertex_queue.put(start_vertex)  # 맨 처음에는 시작 정점만 있음
    visited[start_vertex] = True  # 시작 정점을 "방문"했다고 표시

    while not vertex_queue.empty():
        current_vertex = vertex_queue.get()  # 큐에서 정점을 꺼냄
        print(current_vertex, end=' ')  # 정점을 출력(처리)

        # current_vertex의 모든 이웃에 대해
        for neighbor in graph[current_vertex]:
            if not visited[neighbor]:  # 방문하지 않은 이웃 정점이면
                vertex_queue.put(neighbor)  # 큐에 삽입
                visited[neighbor] = True  # "방문"했다고 표시



vertex = [v.strip() for v in input("Enter vertices: ").split(",")]
adjacency_list = {v: [] for v in vertex}

while True:
    edges = [e.strip() for e in input("Enter edges: ").split(',')]
    edge = sorted([list(e.split('-')) for e in edges])

    invalid_vertices = set()
    for e in edge:
        if e[0] not in adjacency_list:
            invalid_vertices.add(e[0])
        if e[1] not in adjacency_list:
            invalid_vertices.add(e[1])

    if invalid_vertices:
        print(
            f"Error: Following vertices are not in the vertex list: {', '.join(invalid_vertices)}. Please enter correct edges.")
    else:
        for e in edge:
            adjacency_list[e[0]].append(e[1])
            adjacency_list[e[1]].append(e[0])
        break

for k in adjacency_list:
    adjacency_list[k] = sorted(list(set(adjacency_list[k])))

print(f"vertex: {vertex}")
for v, adj_v in adjacency_list.items():
    print(f"{v}의 인접정점: {adj_v}")


print("DFS: ", end='')
DFS2(adjacency_list, vertex[0], set())
print()
print("BFS: ", end='')
BFS(adjacency_list, vertex[0])