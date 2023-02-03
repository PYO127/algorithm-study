# boj.kr/2225 합분해
import sys

n, k = map(int, sys.stdin.readline().split())
dp = [[0] * (k+1) for _ in range(n+1)]

for i in range(0, n+1):
    for j in range(1, k+1):
        dp[i][j] = 1
        if j > 1:
            dp[i][j] += sum([row[j-1] for row in dp[1:i+1]]) % 1000000000
            # dp[i][j] = dp[i][j-1] + dp[i-1][j-1] + ... dp[1][j-1] + dp[0][j-1]
            # dp[0][j-1] = 1
print(dp[n][k])
