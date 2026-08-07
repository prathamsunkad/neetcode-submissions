class Solution:
    def dfs(self, grid,i,j,seen_set,m,n):
        if(i<0 or i>=m or j<0 or j>=n):
            return 0
        if(grid[i][j]!= 1 or (i,j) in seen_set):
            return 0
        seen_set.add((i,j))
        return 1 + (self.dfs(grid,i+1,j,seen_set,m,n) + self.dfs(grid,i-1,j,seen_set,m,n)+
        self.dfs(grid,i,j+1,seen_set,m,n) + self.dfs(grid,i,j-1,seen_set,m,n))

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen_set = set()
        m = len(grid)
        n = len(grid[0])
        max_area = 0
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 1 and (i,j) not in seen_set):
                    temp_area = self.dfs(grid,i,j,seen_set,m,n)
                    max_area = max(temp_area,max_area)
        return max_area
        