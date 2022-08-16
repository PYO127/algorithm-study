# p331 Q32. 섬의 개수
from typing import List

class Solution:
    def numIsland(self, grid:List[List[str]]) -> int:
        def dfs(i, j): # 중첩함수
            if i<0 or i>= len(grid) or \
                j<0 or j>= len(grid[0]) or \
                grid[i][j] != '1':
                return

            grid[i][j] = '0'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)

        count = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == '1':
                    dfs(i,j)
                    count += 1
        return count