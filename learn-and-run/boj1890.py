# boj.kr/1890 점프
import sys

n = int(sys.stdin.readline())
board = [[*map(int, sys.stdin.readline().split())] for _ in range(n)]
dp = [[0 for _ in range(n)] for _ in range(n)]
dp[0][0] = 1

for x in range(n):
    for y in range(n):
        if x != 0:
            dp[x][y] += sum([dp[row][y] for row in range(x) if board[row][y]+row == x])
        if y != 0:
            dp[x][y] += sum([dp[x][col] for col in range(y) if board[x][col]+col == y])

print(dp[n-1][n-1])
