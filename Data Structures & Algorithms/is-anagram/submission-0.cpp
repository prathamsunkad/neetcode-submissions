class Solution {
public:
    bool isAnagram(string s, string t) {

        int s_len = s.size();
        int t_len = t.size();
    
        if(s_len != t_len)
            return false;
    
        unordered_map<char,int> s_map;
        unordered_map<char,int> t_map;
        for(int i = 0; i < s_len; i++){
            s_map[s[i]]+=1;
            t_map[t[i]]+=1;
            
        }

        if(s_map == t_map){
            return true;
        }
        else{
            return false;
        }
        
    }
};
