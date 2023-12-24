#include <iostream>

using namespace std;
unsigned int n ; 

vector<int> get_base_array(unsigned int n, unsigned int base) {
    vector<int> base_array;

    while (n > 0) {
        base_array.push_back(n % base);
        n /= base;
    };
    return base_array;
}

bool is_palindromic(vector<int> base_array) {
    int i = 0;
    int j = base_array.size() - 1;
    while (i < j) {
        if (base_array[i] != base_array[j]) {
            // cout << n << " is not palindromic at base " << base_array << endl;
            return false;
        }
        i++;
        j--;
    }
    return true;
}
void print_array(vector<int> base_array) {
    for (int i = 0; i < base_array.size(); i++) {
        cout << base_array[i] << ".";
    }
    cout << endl;
}
class Solution {
    public:
        bool isPalindrome(int n) {          
            for (int base = 2; base < n-1; base++) {
                vector<int> base_array = get_base_array(n, base);
                // cout << "Base " << base << " : ";
                // print_array(base_array);                
                if (!is_palindromic(base_array)) {
                    return false;                    
                }
            }
            return true;
        }
};

// ------------------------
int main() {
    Solution su;
    // do {
    // cout << "Enter a number: ";
    // cin >> n ;
    
    // string foundPalindromic = su.isPalindrome(n)? "true": "false";
    // cout << "The number " << n << " is " <<  foundPalindromic << endl << endl; 
    // } while (n > 0);
 
    for (int i = 3; i < 100000; i++) {
        if (su.isPalindrome(i)) {
            cout << i << " is palindromic" << endl;
        }
    }
    return 0;
}
