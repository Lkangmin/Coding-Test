cnt = 0

def dfs(x, y, n, matrix, visited):
    dx = [0, 1, 0, -1]
    dy = [1, 0, -1, 0]
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if -1 < nx < n and -1 < ny < n and matrix[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = 1
            global cnt
            cnt += 1
            dfs(nx, ny, n, matrix, visited)

n = int(input())
matrix = []
for _ in range(n):
    temp = list(map(int,input()))
    matrix.append(temp)
visited = [[0]*n for _ in range(n)]
total = []

for i in range(n):
    for j in range(n):
        if matrix[i][j] and not visited[i][j]:
            visited[i][j] = 1
            cnt = 1
            dfs(i, j, n, matrix, visited)
            total.append(cnt)
            
total.sort()
print(len(total))
for i in range(len(total)):
    print(total[i])

