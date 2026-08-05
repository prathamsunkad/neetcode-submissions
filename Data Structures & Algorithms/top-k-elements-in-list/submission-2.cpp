class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int,int> numtocount;
        int len = nums.size();
        for(int i=0; i<len;i++){
            numtocount[nums[i]]+=1;
        }

        vector<vector<int>> vec(len+1);
        for(auto it = numtocount.begin(); it != numtocount.end(); ++it){
            vec[it->second].push_back(it->first);
        }
        vector<int> final_vector;
        int index = len;
        while(k>0){
            while(vec[index].size() != 0){
                int ele = vec[index].back();
                vec[index].pop_back();
                final_vector.push_back(ele);
                k--;
                if(k==0){
                    break;
                }
            
            }
        index--;
        }

        return final_vector;
    }
};
