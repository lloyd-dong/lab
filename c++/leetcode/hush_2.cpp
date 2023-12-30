#include <unordered_map>
#include <string>
#include <iostream>
using namespace std;

int main(){

    unordered_map<char, char> hush;
    string key = "the quick fox jumps over the lazy dog";
    
    if (hush['a'] )
        cout << "a:" << hush['a'] << "--" << endl;
    else
        cout << "a: not found" << endl;

    string value = "abc";
    for (char c : value){
        c = c + 1;
    }
    cout << value << endl;
    return 0;
}