class Solution:
    def countSubstrings(self, s: str) -> int:

        count = 0
        length = len(s)

        for i in range(length):
            count+=1
            start = i-1
            end = i+1
            while(start>=0 and end<length):
                if(s[start] == s[end]):
                    count+=1
                    start = start - 1
                    end = end+1
                
                else:
                    break
        

        for i in range(length-1):
            first = i
            second = i+1
            if(s[first] == s[second]):
                count+=1
            
                start = first-1
                end = second+1
                while(start>=0 and end<length):
                    if(s[start] ==s[end]):
                        count+=1
                        start = start - 1
                        end = end+1
                    
                    else:
                        break

        
        return count


        

        
        