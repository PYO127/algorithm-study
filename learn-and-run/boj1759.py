# boj.kr/1759 암호 만들기
import sys

l, m = map(int, sys.stdin.readline().split())
char = list(sys.stdin.readline().split())
char.sort()


def dfs(start: int, seq: str):
    if len(seq) == l:
        mo = len([1 for c in seq if c in ['a', 'e', 'i', 'o', 'u']])
        if mo >= 1 and l - mo >= 2:
            print(seq)
        return
    for i in range(start, m):
        c = char[i]
        dfs(i + 1, seq + c)


dfs(0, '')
