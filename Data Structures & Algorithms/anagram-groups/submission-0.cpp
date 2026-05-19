class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) {
        
        int vector_length = strs.size();
        map<vector<int>,vector<string>> final_hash;
        for(int i = 0; i<vector_length; i++){
            string s = strs[i];
            int string_length = s.size();
            vector<int> a (26,0);
            for(int j = 0;j<string_length; j++){
                a[int(s[j]) - 97]+=1;
            }

            final_hash[a].push_back(strs[i]);
        }


        vector<vector<string>> values;

        for (auto &p : final_hash) {
        values.push_back(p.second);
                }
        return values;

    }
};
