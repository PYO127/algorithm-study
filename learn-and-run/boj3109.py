# boj.kr/3109 빵집
import sys

r, c = map(int, sys.stdin.readline().split())
board = [list(sys.stdin.readline().replace('\n', '')) for _ in range(r)]


def dfs(x, y):
    board[x][y] = '*'
    if y == c - 1:
        return 1
    # 1. 오른쪽 윗 방향
    if x - 1 >= 0 and board[x - 1][y+1] == '.' and dfs(x - 1, y+1):
        return 1
    # 2. 오른쪽 방향
    if board[x][y+1] == '.' and dfs(x, y+1):
        return 1
    # 3. 오른쪽 아랫방향
    if x + 1 < r and board[x + 1][y+1] == '.' and dfs(x + 1, y+1):
        return 1
    return 0


cnt = 0
for i in range(r):
    cnt += dfs(i, 0)

print(cnt)
