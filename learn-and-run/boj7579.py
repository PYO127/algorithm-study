# boj.kr/7579 앱
import sys
from collections import defaultdict

n, m = map(int, sys.stdin.readline().split())
mem = [*map(int, sys.stdin.readline().split())]
cost = [*map(int, sys.stdin.readline().split())]

# 또 다른 아이디어
# 1 <= n <= 100 and 0 <= c <= n
# 총 비용: 최대 10001 루프 밖에 안된다....
# dp[x]: x 비용으로 확보할 수 있는 최대 메모리
# 기존에는, dp[x]: x 메모리를 확보하는데 드는 최대 비용
len_dp = sum(cost)
dp = [0] * (len_dp+1)

for m_, c_ in zip(mem, cost):
    for cap in reversed(range(c_, len_dp+1)):
        dp[cap] = max(dp[cap], dp[cap-c_] + m_)

for idx, m_sum in enumerate(dp):
    if m_sum >= m:
        print(idx)
        break
