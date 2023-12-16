#include <vector>
#include <iostream>

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {     
     for(int i = 0; i < nums.size(); i++) {
        for(int j = i+1; j < nums.size(); j++) {
            if(nums[i] + nums[j] == target) {
                return {i, j};
            }         
        }
     }
     return {}; 
 }        
};

int main(){
    std::vector<int> nums = {2, 7, 11, 15};
    int  target = 18;
    Solution s;
    std::vector<int> result = s.twoSum(nums, target);
    std::cout << result[0] << " " << result[1] << std::endl;
}