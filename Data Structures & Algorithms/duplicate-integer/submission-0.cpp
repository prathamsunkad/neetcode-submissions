class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        unordered_map<int,int> a;
        int len = nums.size();

        for (int i = 0; i<len; i++){
            a[nums[i]]+=1;
            if(a[nums[i]] > 1){
                return true;
            }
            else{
                continue;
            }
        }

        return false;



        
    }
};