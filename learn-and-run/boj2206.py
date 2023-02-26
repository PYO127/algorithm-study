# boj.kr/2206 벽 부수고 이동하기
import sys
from collections import deque

d = [-1, 0, 1, 0, -1]

n, m = map(int, sys.stdin.readline().split())
board = [sys.stdin.readline().strip() for i in range(n)]

cost = [[[0]*2 for _ in range(m)] for _ in range(n)]

queue = deque()
queue.append((0, 0, 0))
cost[0][0][0] = 1


def bfs():
    while queue:
        x, y, flag = queue.popleft()
        if x == n - 1 and y == m - 1:
            # 거리가 1씩 증가하는 bfs 이므로
            # 어떤 위치까지의 최소 거리는, 그 위치를 처음 방문할 때 걸리는 거리
            return cost[x][y][flag]
        for i in range(4):
            nx = x + d[i]
            ny = y + d[i + 1]
            if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1:
                continue
            if board[nx][ny] == '0' and cost[nx][ny][flag] == 0:
                cost[nx][ny][flag] = cost[x][y][flag] + 1
                queue.append((nx, ny, flag))
            if flag == 0 and board[nx][ny] == '1' and cost[nx][ny][1] == 0:
                cost[nx][ny][1] = cost[x][y][flag] + 1
                queue.append((nx, ny, 1))

    return -1


print(bfs())
