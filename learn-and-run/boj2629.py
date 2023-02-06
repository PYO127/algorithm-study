# boj.kr/2629 양팔저울
import sys

n = int(sys.stdin.readline())
weight = [*map(int, sys.stdin.readline().split())]
m = int(sys.stdin.readline())
test = list(map(int, sys.stdin.readline().split()))

# 추의 갯수: 30개 이하, 추의 무게: 500g 이하 -> 15,000g 이하의 구슬만 측정 가능

dp = [0] * 15001
dp[0] = 1
visit = [0]

# 무게의 중간 과정이 0보다 작거나, 15000이상인 경우도 발생할 수 있어서,
# visit에는 포함시킨다. 단, 0 <= 중간과정의 무게 <= 15000 인 경우에만
# dp[] 에 체크한다. (런타임에러 방지)
for w in weight:
    tmp_visit = visit[:]
    # 중간에 visit의 크기가 변경되는 것을 방지하기 위해 매회 tmp_visit을
    # 복사해준다.
    for v in visit:
        if v + w not in visit:
            tmp_visit.append(v + w)
            if v + w < 15001:
                dp[v+w] = 1
        if v - w not in visit:
            tmp_visit.append(v - w)
            if v - w >= 0:
                dp[v-w] = 1
    visit = tmp_visit[:]

print(*['Y' if t < 15001 and dp[t] == 1 else 'N' for t in test])
