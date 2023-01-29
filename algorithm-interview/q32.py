# p331 Q32. 섬의 개수
# https://leetcode.com/problems/number-of-islands/
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            grid[x][y] = 0
            if x + 1 < len(grid[0]) and grid[x+1][y] == '1':
                dfs(x + 1, y)
            if x > 0 and grid[x-1][y] == '1':
                dfs(x - 1, y)
            if y + 1 < len(grid) and grid[x][y+1] == '1':
                dfs(x, y + 1)
            if y > 0 and grid[x][y-1] == '1':
                dfs(x, y - 1)

        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    ans += 1
                    dfs(i, j)

        return ans
