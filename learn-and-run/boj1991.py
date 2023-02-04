# boj.kr/1991 트리 순회
import sys


def pre_order(node):
    print(node, end='')
    if graph[node]['left'] != '.':
        pre_order(graph[node]['left'])
    if graph[node]['right'] != '.':
        pre_order(graph[node]['right'])


def in_order(node):
    if graph[node]['left'] != '.':
        in_order(graph[node]['left'])
    print(node, end='')
    if graph[node]['right'] != '.':
        in_order(graph[node]['right'])


def post_order(node):
    if graph[node]['left'] != '.':
        post_order(graph[node]['left'])
    if graph[node]['right'] != '.':
        post_order(graph[node]['right'])
    print(node, end='')


n = int(sys.stdin.readline())
graph = {}
for _ in range(n):
    m, left, right = sys.stdin.readline().split()
    graph[m] = {'left': left, 'right': right}

pre_order('A')
print()
in_order('A')
print()
post_order('A')
print()
