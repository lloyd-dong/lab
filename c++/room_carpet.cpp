// Author: Tiger Dong
// Assignment Title: Carpet
// Assignment Description: calculate the total cost of the carpet
// Due Date: 9/6/2023
// Date Created: 9/5/2023
// Date Last Modified:9/6/2023

//  main.cpp
//  Class stuff 1
//
//  Created by Zhexian Dong on 2023/9/5.
//

#include <iostream>
#include <iomanip>
using namespace std;


int main() {
    //Data Abstraction:
    
    int roomWidth;
    int roomLength;
    double PPSF; // price per square foot
    
    int roomA; // Room Area
    float carpetP; // Carpet Price
    float laborP; // Labor Price
    float taxP; // Text Price
    float totalP; // Total Price
    
    
    //Input:
    // cin >> roomWidth;
    // cin >> roomLength;
    // cin >> PPSF;
    cout << fixed << setprecision(2);
    cout << "Please input room wideth: ";
    cin >> roomWidth;
    cout << "Please input room length: ";
    cin >> roomLength;
    cout << "Please input PPSF: ";
    cin >> PPSF;

    //Process:
    roomA = roomWidth * roomLength;
    carpetP = roomA * PPSF * 1.2;
    laborP = roomA * 0.75;
    taxP = (carpetP + laborP) * 0.07;
    totalP = carpetP + laborP + taxP;
    
    //Outputs;
    cout << "Order #1" << endl;
    cout << "Room: " << roomA << " sq ft" << endl;
    cout << "Carpet: $" << carpetP << endl;
    cout << "Labor: $"  << laborP << endl;
    cout << "Tax: $" <<  taxP << endl;
    cout << endl;
    cout << "Total Cost: $" << totalP << endl;
   
    //Assumptions:
    return 0;
}