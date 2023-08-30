#include <iostream>
using namespace std;

int main(){    
    int number ; 
    cout << "input a number: ";    
    cin >> number;    
    int sum = 0;
    int remain = number;
    do{
        sum += remain %10;
        remain /= 10;
    }while(remain >0);
    cout << "digits sum of " << number << " = " << sum << endl;
    
    return 0;
}