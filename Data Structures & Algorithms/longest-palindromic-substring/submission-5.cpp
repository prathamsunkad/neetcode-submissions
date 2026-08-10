class Solution {
public:
    string longestPalindrome(string s) {
        int length = s.size();
        int max_length = 1;
        string max_string = "";
        if(length == 1){
            return s;
        }

        if(length == 2 && s[0]!=s[1]){
            return max_string = s[0];
        }

        if(length == 2 && s[0]==s[1]){
            return s;
        }


        for(int i = 0;i<length;i++){

            int start = i-1;
            int end = i+1;

            while(start>=0 && end<length){
                if(s[start]==s[end]){
                    int temp_len = end-start+1;
                    if(temp_len>max_length){
                        max_length = temp_len;
                        max_string = s.substr(start, end - start+1);
                        
                    }
                }
                if(s[start]!=s[end]){
                    break;
                }
                start--;
                end++;
            }



            int second = i+1;
            int first = i;
            if(second<length && s[first]==s[second]){

                int temp_len = second - first + 1;
                if(temp_len>max_length){
                    max_length = temp_len;
                    max_string = s.substr(first, temp_len);
                }


                int start = first-1;
                int end = second+1;

                while(start>=0 && end<length){
                if(s[start]==s[end]){
                    int temp_len = end-start+1;
                    if(temp_len>max_length){
                        max_length = temp_len;
                        max_string = s.substr(start, end - start+1);
                    }
                }
                if(s[start]!=s[end]){
                    break;
                }
                start--;
                end++;
            }
            
            }


        }


        return max_string;

        
    }
};
