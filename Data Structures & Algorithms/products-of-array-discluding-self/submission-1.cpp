class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int product = 1;
        int length = nums.size();
        vector<int> v1;
        for(int i=0; i< length; i++){
            v1.push_back(product);
            product*=nums[i];
        }

        vector<int> v2(length,0);
        int product_2 = 1;
        for(int i=length - 1; i>=0; i--){
            v2[i]= product_2;
            product_2*=nums[i];
        }
        vector<int> v3;
        for(int i=0; i<length; i++){
            v3.push_back(v1[i]*v2[i]);
        }

        return v3;



    }
};
