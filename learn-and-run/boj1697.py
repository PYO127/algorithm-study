# boj.kr/1697 숨바꼭질
import collections
import sys

n, k = map(int, sys.stdin.readline().split())

cost = [-1] * 100001
deque = collections.deque()

cost[n] = 0
deque.append(n)

while deque:
    x = deque.popleft()
    t = cost[x]
    if 2 * x < 100001 and cost[2 * x] == -1:
        deque.append(2 * x)
        cost[2 * x] = t + 1
    if x + 1 < 100001 and cost[x + 1] == -1:
        deque.append(x + 1)
        cost[x + 1] = t + 1
    if x - 1 > -1 and cost[x - 1] == -1:
        deque.append(x - 1)
        cost[x - 1] = t + 1
    if cost[k] != -1:
        break

print(cost[k])
