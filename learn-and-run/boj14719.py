# boj.kr/14719 빗물
import sys

h, w = map(int, sys.stdin.readline().split())
a = [*map(int, sys.stdin.readline().split())]

left, right = 0, w-1
ans = 0
left_max, right_max = a[left], a[right]

while left < right:
    left_max, right_max = max(a[left], left_max), max(a[right], right_max)
    # left, right 모두 height 중 가장 높은 곳으로 수렴하도록
    if left_max < right_max:  # left_max 가 낮으면 left -> left+1
        ans += left_max - a[left]
        left += 1
    else:  # right 가 낮으면 right -> right-1
        ans += right_max - a[right]
        right -= 1

print(ans)
