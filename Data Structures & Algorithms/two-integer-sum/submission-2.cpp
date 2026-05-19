class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        vector<int> v;
        int len = nums.size();
        unordered_map<int,int> a;

        for(int i = 0; i< len; i++){
            a[nums[i]]+=1;
        }

        for(int i=0; i<len;i++){
            if(target - nums[i] == nums[i] and a[nums[i]] == 1){
                continue;
            }
            if(a[target - nums[i]] >= 1){
                v.push_back(i);
            }
        }
        return v;
        
    }
};
