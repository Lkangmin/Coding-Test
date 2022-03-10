N, M = map(int, input().split())

INF = 1e9
edge = []

dist = [INF] * N

for _ in range(M):
    a, b, c = map(int, input().split())
    edge.append((a-1,b-1,c))


# 벨만 포드 알고리즘 (negative 간선 있을 시 사용)

def bf(start):
    dist[start] = 0
    for i in range(N):
        for j in range(M):
            cur_n, next_n, cost = edge[j][0], edge[j][1], edge[j][2]
            if dist[cur_n] != INF and dist[next_n] > cost + dist[cur_n]:
                dist[next_n] = cost + dist[cur_n]
                # 시작 노드 제외한 전체 노드 수 만큼 반복 수행한 뒤, 마지막으로 수행했을 때 갱신이 발생하면 음의 순환
                if i == N-1:
                    return True
    return False
    
cycle = bf(0)

if cycle:
    print(-1)
else:
    for i in range(1, N):
        if dist[i] != INF:
            print(dist[i])
        # 해당 경로에 도달할 수 없을 경우
        else:
            print(-1)