INF = 9999


def printA(A):
    vsize = len(A)
    print("====================================")
    for i in range(vsize):
        for j in range(vsize):
            if A[i][j] == INF:
                print(" INF ", end='')
            else:
                print("%4d " % A[i][j], end='')
        print("")


def reconstruct_path(path, start, end):
    if path[start][end] == -1:
        return []
    route = [start]
    while start != end:
        start = path[start][end]
        route.append(start)
    return route


def shortest_path_floyd(vertex, adj):
    vsize = len(vertex)
    A = list(adj)
    path = [[-1 if adj[i][j] == INF or i == j else j for j in range(vsize)] for i in range(vsize)]

    for k in range(vsize):
        for i in range(vsize):
            for j in range(vsize):
                if A[i][k] + A[k][j] < A[i][j]:
                    A[i][j] = A[i][k] + A[k][j]
                    path[i][j] = path[i][k]
        printA(A)

    return A, path


if __name__ == "__main__":
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
    weight = [
        [0, 7, INF, INF, 3, 10, INF],
        [7, 0, 4, 10, 2, 6, INF],
        [INF, 4, 0, 2, INF, INF, INF],
        [INF, 10, 2, 0, 11, 9, 4],
        [3, 2, INF, 11, 0, 13, 5],
        [10, 6, INF, 9, 13, 0, INF],
        [INF, INF, INF, 4, 5, INF, 0]
    ]

    print("Shortest Path By Floyd's Algorithm")
    dist, path = shortest_path_floyd(vertex, weight)

    start_vertex = input("Start Vertex: ")
    end_vertex = input("End Vertex: ")

    start_index = vertex.index(start_vertex)
    end_index = vertex.index(end_vertex)

    route = reconstruct_path(path, start_index, end_index)
    if len(route) == 0:
        print("No path found.")
    else:
        print("Shortest Path: ", " -> ".join(vertex[i] for i in route))
        print("Distance of the Shortest Path: ", dist[start_index][end_index])
