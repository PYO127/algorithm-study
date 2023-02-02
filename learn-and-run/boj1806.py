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
        # 만약 left = right, seq[left] >= curr_sum 이 되면
        # while 위에서 left +=1 이 되고, while문 밖으로
        # 나가진다. 정답에는 이상이 없을 것 같지만(정답이 될 수 있는
        # 최소 길이 = 1), 의도한 로직은 그게 아니므로 아래에
        # left 가 right 보다 커졌을 경우를 처리해준다.
        if left > right:
            right = left
    else:
        right += 1
        if right < n:
            curr_sum += seq[right]

if ans == n+1:
    print(0)
else:
    print(ans)

