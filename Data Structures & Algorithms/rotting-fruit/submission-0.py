class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m,n = len(grid), len(grid[0])
        q = []
        seen_set = set()
        count_fresh = 0
        for i in range(m):
            for j in range(n):
                if(grid[i][j] == 2):
                    q.append([i,j])
                    seen_set.add((i,j))
                if(grid[i][j] == 1):
                    count_fresh+=1
        
        max_time = 0
        
        time_array = [[0]*n for i in range(m)]

        while len(q)>0:
            i,j = q.pop(0)
            
            if(i-1>=0 and (i-1,j) not in seen_set and grid[i-1][j] == 1):
                grid[i-1][j] = 2
                time_array[i-1][j] = 1 + time_array[i][j]
                max_time = max(time_array[i-1][j], max_time)
                seen_set.add((i-1,j))
                q.append([i-1,j])
                count_fresh-=1
            
            if(i+1<m and (i+1,j) not in seen_set and grid[i+1][j] == 1):
                grid[i+1][j] = 2
                time_array[i+1][j] = 1 + time_array[i][j]
                max_time = max(time_array[i+1][j], max_time)
                seen_set.add((i+1,j))
                q.append([i+1,j])
                count_fresh-=1

            if(j-1>=0 and (i,j-1) not in seen_set and grid[i][j-1] ==1):
                grid[i][j-1] = 2
                time_array[i][j-1] = 1 + time_array[i][j]
                max_time = max(time_array[i][j-1], max_time)
                seen_set.add((i,j-1))
                q.append([i,j-1])
                count_fresh-=1

            if(j+1<n and (i,j+1) not in seen_set and grid[i][j+1] ==1):
                grid[i][j+1] = 2
                time_array[i][j+1] = 1 + time_array[i][j]
                max_time = max(time_array[i][j+1], max_time)
                seen_set.add((i,j+1))
                q.append([i,j+1])
                count_fresh-=1

            
        if count_fresh == 0:
            return max_time
        
        else:
                return -1
            
            





        