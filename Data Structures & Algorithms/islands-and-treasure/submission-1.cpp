class Solution {
public:
    void islandsAndTreasure(vector<vector<int>>& grid) {

        queue<pair<int,int>> q;
        int m = grid.size();
        int n = grid[0].size();


        vector<vector<int>> visited_array(m, vector<int>(n, 0));

        for(int i = 0;i<m;i++){
            for(int j=0;j<n;j++){
                if(grid[i][j]==0){
                    q.push({i,j});
                    visited_array[i][j] = 1;
                }
            }
        }

        

        while (!q.empty()){
            pair<int,int> index = q.front();
            q.pop();
            
            int i = index.first;
            int j = index.second;
            

            if(i-1>=0 and visited_array[i-1][j] == 0 and grid[i-1][j]!= -1){
                grid[i-1][j] = grid[i][j] + 1;
                q.push({i-1,j});
                visited_array[i-1][j] = 1;
            }

            if(i+1<m and visited_array[i+1][j] == 0 and grid[i+1][j]!= -1){
                grid[i+1][j] = grid[i][j] + 1;
                q.push({i+1,j});
                visited_array[i+1][j] = 1;
            }
            if(j-1>=0 and visited_array[i][j-1] == 0 and grid[i][j-1]!= -1){
                grid[i][j-1] = grid[i][j] + 1;
                q.push({i,j-1});
                visited_array[i][j-1] = 1;
            }
            if(j+1<n and visited_array[i][j+1] == 0 and grid[i][j+1]!= -1){
                grid[i][j+1] = grid[i][j] + 1;
                q.push({i,j+1});
                visited_array[i][j+1] = 1;
            }



        }
        
    }
};
