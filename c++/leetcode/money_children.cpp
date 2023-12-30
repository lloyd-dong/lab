#include <iostream>
#include <unordered_map>
using namespace std;

class Solution {
public:
    int distMoney(int money, int children) {
        if (money < children ) return -1;
        if (children *8 < money) return --children;    
        int eights = money/8;  
        if (money % 8 == 4 && children - eights == 1) return --eights;
        for (int i = 0; i < eights; i++){
            if (money % 8 + i * 8 >= children - eights +i) 
                return eights - i;
        }
        return 0;
     }  
    int distMoney0(int money, int children) {
        if (money < children) return -1;
        if (children *8 < money) return children-1; 
        unsigned int eights = (money - children) / 7; 
        if (children - eights == 1 && money - eights * 8 == 4) eights--;
        return eights;   
    }   
};

int main(){
    vector<vector<int>> money_children = {
        {23, 2, 1},
        {16, 2, 2},
        {17, 2, 1},
        {30, 2, 1},
        {4, 2, 0},
        {8, 2, 0},
        {9, 8, 0},
        {12, 3, 1},
        {20,3, 1},
        {20, 7, 1},
        {16, 10, 0},
        {8, 8, 0},
        {9, 9, 0},
        {10,10,0},
        {17, 10, 1},
        {17, 11, 0},
        {18,11, 1},
        {24, 18, 0}
    };
    Solution s;
    for ( auto mc: money_children){
        int money = mc[0];
        int children = mc[1];
        cout << "money: " << money << " children: " << children << " expected: " << mc[2] << endl;
        int result = s.distMoney0(money, children);
        std::cout << "result: " << result  << endl;
        assert(result == mc[2]);
    };
}