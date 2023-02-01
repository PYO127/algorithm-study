import sys

sys.setrecursionlimit(10 ** 6)
# 최대 재귀 깊이 설정

preorder = []


def pre_to_post(first: int, last: int):
    if first > last:
        return
    # preorder: NLR 이므로
    # 처음으로 Node N 보다 자식(R)의 인덱스(mid) 찾기
    mid = first + 1
    for i in range(first + 1, last + 1):
        if preorder[first] < preorder[i]:
            mid = i
            break
    pre_to_post(first + 1, mid - 1)
    pre_to_post(mid, last)
    print(preorder[first], sep=' ')


# 입력이 없을 때 까지 입력
while True:
    tmp = sys.stdin.readline().split()
    if not tmp:
        break
    preorder.append(int(tmp[0]))

pre_to_post(0, len(preorder) - 1)
