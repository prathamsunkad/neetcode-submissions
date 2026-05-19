class Solution:
    def isPalindrome(self, s: str) -> bool:
            length = len(s)
            i = 0
            j = length - 1
            valid_range = [i for i in range(48, 58, 1)] + [j for j in range(97,123,1)] + [k for k in range(65,91,1)]
            while j>i:
                if ord(s[i]) not in valid_range:
                    i+=1
                    continue
                
                if ord(s[j]) not in valid_range:
                    j-=1
                    continue

                if(s[i].lower()!=s[j].lower()):
                    return False
                
                if(s[i].lower()==s[j].lower()):
                    i+=1
                    j-=1
            
            return True
            
        