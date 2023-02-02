# boj.kr/1806 부분합
import sys

n, s = map(int, sys.stdin.readline().split())
seq = [*map(int, sys.stdin.readline().split())]

ans = n + 1
left = 0
right = 0
curr_sum = seq[left]
while left <= right < n:
    if curr_sum >= s:
        if ans > right - left + 1:
            ans = right - left + 1
        curr_sum -= seq[left]
        left += 1
    else:
        right += 1
        if right < n:
            curr_sum += seq[right]

if ans == n+1:
    print(0)
else:
    print(ans)
