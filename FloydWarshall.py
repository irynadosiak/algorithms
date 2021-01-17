def FloydWarshall(graph, N):
    distance = list(map(lambda i: list(map(lambda j: j, i)), graph))
    for k in range(N):
        for i in range(N):
            for j in range(N):
                distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])
    return distance


matrix = [[0, 8, 2], [8, 0, 1], [2, 1, 0]]
print(FloydWarshall(matrix, 3))
