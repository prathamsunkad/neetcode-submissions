class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) {
        int length = numbers.size();
        int j = length - 1;
        int i = 0;
        vector<int> final;
        while (j>i) {
            int sum = numbers[j] + numbers[i];
            if(sum == target and j!=i){
                final.push_back(i+1);
                final.push_back(j+1);
                break;
            }

            if(sum> target){
                j--;
            }

            if(sum<target){
                i++;
            }
        }
        return final;
    }
};
