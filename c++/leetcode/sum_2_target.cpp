#include <vector>
#include <iostream>
#include <unordered_map>
using namespace std;

class Solution {
public:
    std::vector<int> twoSum(std::vector<int>& nums, int target) {   
     unordered_map<int, int> hush = {{target - nums[0], 0}};   
     for(int i = 1; i < nums.size(); i++) {
        if ( hush[nums[i]]) {
            return {hush[nums[i]], i};
        } else {
            hush[target - nums[i]] = i;
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