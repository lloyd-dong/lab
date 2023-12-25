#include <iostream>

using namespace std;

class Solution {
    public:
        string restoreString(string s, vector<int>& indices) {
            string res = s;
            for (int i = 0; i < indices.size(); ++i) {
                res[indices[i]] = s[i];
            }
            return res;
        }
};

int main() {
    Solution s;
    string str = "codeleet";
    vector<int> indices = {4,5,6,7,0,2,1,3};
    cout << s.restoreString(str, indices) << endl;
}