# boj.kr/7576 토마토
import collections
import sys

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n, m = map(int, sys.stdin.readline().split())
deque = collections.deque()
board = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

for i in range(m):
    for j in range(n):
        if board[i][j] == 1:
            deque.append((i, j, 0))

while deque:
    x, y, d = deque.popleft()  # python 은 반복문 안에서 선언된 변수도 global (d)
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 0:
            deque.append((nx, ny, d + 1))
            board[nx][ny] = 1

for i in range(m):
    if board[i].count(0):
        d = -1
        break
print(d)  # while문이 종료되기 전 마지막으로 돌 때, d가 최대일 것.
