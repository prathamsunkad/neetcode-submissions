class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ##row wise checking
        n = len(board)
        for i in range(n):
            row = board[i]
            check_array = [0]*10
            for num in row:
                if num == '.':
                    continue

                check_array[int(num)]+=1
                if check_array[int(num)]>1:
                    return False
        

        ## column wise checking
        for j in range(n):
            column = [row[j] for row in board]
            check_array = [0]*10
            for num in column:
                if num == '.':
                    continue

                check_array[int(num)]+=1
                if check_array[int(num)]>1:
                    return False

        ## 3x3 matching
        x = 0
        y = 0
        count = 0
        while (count < n):
            check_array = [0]*10
            for i in range(x,x+3):
                for j in range(y,y+3):
                    num = board[i][j]
                    if num == '.':
                        continue
                    check_array[int(num)]+=1
                    if check_array[int(num)]>1:
                        return False
            count+=1
            if(count%3!=0):
                x+=3
            
            if(count%3 == 0):
                x = 0
                y+=3
        
        return True

        


        


        