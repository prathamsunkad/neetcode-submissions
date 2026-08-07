class Solution:
    def dfs(self, grid, i, j, seen_set, m, n):
        if i < 0 or i >= m or j < 0 or j >= n:
            return
        if grid[i][j] != '1' or (i, j) in seen_set:
            return
        seen_set.add((i, j))
        self.dfs(grid, i - 1, j, seen_set, m, n)
        self.dfs(grid, i + 1, j, seen_set, m, n)
        self.dfs(grid, i, j - 1, seen_set, m, n)
        self.dfs(grid, i, j + 1, seen_set, m, n)

    # def dfs(self, grid,i,j,seen_set,m,n):
    #     if grid[i][j] == 0:
    #         return
        
    #     if(grid[i][j] == 1 and (i,j) not in seen_set):
    #         seen_set.add((i,j))

    #     self.dfs(grid, max(0,i-1),j, seen_set,m,n)
    #     self.dfs(grid, min(i+1,m), j, seen_set,m,n)
    #     self.dfs(grid,i,max(0,j-1),seen_set,m,n)
    #     self.dfs(grid,i,min(n,j+1),seen_set,m,n)
    #     return 

    def numIslands(self, grid: List[List[str]]) -> int:
        seen_set = set()
        m = len(grid)
        n = len(grid[0])
        island_count = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in seen_set:
                    island_count += 1
                    self.dfs(grid, i, j, seen_set, m, n)
        return island_count

    # def numIslands(self, grid: List[List[str]]) -> int:
    #     seen_set = set()
    #     m = len(grid)
    #     n = len(grid[0])
    #     island_count = 0
    #     for i in range(m):
    #         for j in range(n):
    #             if grid[i][j] == 0:
    #                 continue

    #             if grid[i][j] == 1 and (i,j) not in seen_set:
    #                 island_count+=1
    #                 self.dfs(grid,i,j,seen_set,m,n)
        
    #     return island_count




    

                

        

        