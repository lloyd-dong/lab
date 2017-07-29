#include <iostream>

void swap(int x&, int y&){
	int temp = x;
	x=y;
	y=temp;
}

int main(){
	int x=10, y=0;
	swap(x,y);
	std::cout << "x: " <<x <<" y: " <<y <std::<endl;
	
	return 0;
}