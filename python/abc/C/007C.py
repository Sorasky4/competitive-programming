from queue import Queue


def bfs():
    R, C = map(int, input().split())
    sy, sx = map(int, input().split())
    gy, gx = map(int, input().split())
    maze = [list(input()) for _ in range(R)]
    dist = [[float('inf') for i in range(C)] for j in range(R)]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    sy -= 1
    sx -= 1
    gy -= 1
    gx -= 1
    dist[sy][sx] = 0
    q = Queue()
    q.put((sy, sx))
    while not q.empty():
        p = q.get()
        if p[0] == gy and p[1] == gx:
            break
        for i in range(4):
            ny = p[0] + dy[i]
            nx = p[1] + dx[i]
            if 0 <= ny < R and 0 <= nx < C and maze[ny][nx] != '#' and dist[ny][nx] == float('inf'):
                dist[ny][nx] = dist[p[0]][p[1]] + 1
                q.put((ny, nx))
    print(dist[gy][gx])
    return 0

if __name__ == '__main__':
    bfs()