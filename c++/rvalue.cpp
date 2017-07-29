#include <iostream>

void swap(int& x, int &y, int & z){
	int temp = x;
	x=y;
	y=temp;
}

int main(){
	int x=10, y=0, z=100;
	swap(x,y, z);
	std::cout << "x: " <<x <<" y: " <<y <<std::endl;
	
	return 0;
}

// compile gcc rvalue.cpp