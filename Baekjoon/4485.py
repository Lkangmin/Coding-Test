import heapq

INF = int(1e9)
dxy = [(0,1), (1,0), (-1,0), (0, -1)]
T = 1
cnt = 1

while T:
    T = int(input())
    if not T:
        break
    matrix =[]
    
    for _ in range(T):
        input_list = list(map(int, input().split()))
        matrix.append(input_list)
    
    dist = [[INF for i in range(T)] for j in range(T)]
    
    # heap을 이용한 dijkstra 구현
    def dijk(s_x, s_y):
        q = []
        heapq.heappush(q, (matrix[s_x][s_y], s_x, s_y))
        dist[s_x][s_y] = matrix[s_x][s_y]
        while q:
            cur, c_x, c_y = heapq.heappop(q)

            if dist[c_x][c_y] < cur:
                continue

            for x, y in dxy:
                if 0<= c_x + x < T and 0<= c_y + y < T:
                    n_x = c_x + x
                    n_y = c_y + y
                    cost = cur + matrix[n_x][n_y]
                    if cost < dist[n_x][n_y]:
                        dist[n_x][n_y] = cost
                        heapq.heappush(q, (cost, n_x, n_y))

    dijk(0, 0)
    print(f'Problem {cnt}:', dist[T-1][T-1])
    cnt += 1
