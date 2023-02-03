# boj.kr/12865 평범한 배낭
import sys

n, k = map(int, sys.stdin.readline().split())
w, v = list(zip(*list(map(int, sys.stdin.readline().split()) for _ in range(n))))
dp = [0 for _ in range(k+1)]

for idx in range(n):  # 물건 idx
    for cap in reversed(range(1, k+1)):  # 가방 capacity n+1 에서 1로  역순
        # 가방 최대 무게를 k부터 1까지 역순으로 체크
        # 역순으로 체크하지 않을 경우
        # dp[j-w[i]] 가 i번째 물건, 즉 자기자신에 의해 업데이트된 값이 될 수 있음.
        if w[idx] > cap:
            continue
        dp[cap] = max(dp[cap], v[idx] + dp[cap - w[idx]])

print(dp[k])
