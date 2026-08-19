class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific_list = set()
        atlantic_list = set()
        def bfs_pacific(heights, r, c):
            if (r, c) in pacific_list:
                return

            if(r<0 or r>=rows or c<0 or c>=cols):
                return

            pacific_list.add((r,c))
            if(r-1>=0):
                if(heights[r-1][c]>=heights[r][c]):
                    bfs_pacific(heights,r-1,c)

            if(r+1<rows):
                if(heights[r+1][c]>=heights[r][c]):
                    bfs_pacific(heights,r+1,c)


            if(c-1>=0):
                if(heights[r][c-1]>=heights[r][c]):
                    bfs_pacific(heights,r,c-1)

            if(c+1<cols):
                if(heights[r][c+1]>=heights[r][c]):
                    bfs_pacific(heights,r,c+1)

            return



        def bfs_atlantic(heights, r, c):
            if (r,c) in atlantic_list:
                return
        
            if(r<0 or r>=rows or c<0 or c>=cols):
                return

            atlantic_list.add((r,c))
            if(r-1>=0):
                if(heights[r-1][c]>=heights[r][c]):
                    bfs_atlantic(heights,r-1,c)

            if(r+1<rows):
                if(heights[r+1][c]>=heights[r][c]):
                    bfs_atlantic(heights,r+1,c)


            if(c-1>=0):
                if(heights[r][c-1]>=heights[r][c]):
                    bfs_atlantic(heights,r,c-1)

            if(c+1<cols):
                if(heights[r][c+1]>=heights[r][c]):
                    bfs_atlantic(heights,r,c+1)

            return


        for i in range(rows):
            bfs_pacific(heights,i,0)
            bfs_atlantic(heights,i,cols-1)

        for j in range(cols):
            bfs_pacific(heights,0,j)
            bfs_atlantic(heights,rows-1,j)

    
        final_ans = []
        for coordinate in pacific_list:
            if(coordinate in atlantic_list):
                ri = coordinate[0]
                ci = coordinate[1]
                final_ans.append([ri,ci])

        return final_ans

            



        