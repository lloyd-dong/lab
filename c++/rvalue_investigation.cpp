#include <iostream>

using namespace std;

void printReference (int& value)
{
        cout << "lvalue: value = " << value << endl;
}
void swap(int&   x, int  &   y, int&z){
	z= x;
	x=y;
	y=z;
}

void f( int* a, int *b){
	std::cout << "a is : " <<a <<" *a is : " << *a << *(a+1)<<std::endl;
	std::cout << "a[0] is " <<a[0] <<std::endl;
	*(a+1) =0;
	int* c =a;
	*c=0;
}
int& g(int &x){
	return x;
}

int x1=100;
int&& foo(){
	return &x1;
}

int main(){
	int x=10, y=0,z;
	swap(x,y,z);
	std::cout << "x: " <<x <<" y: " <<y <<std::endl;

	int a[]={1,2,3,4,5,6};
	int b=100;
	f(a, &b);
	std::cout<< "a:" << a[0]<<a[1]<<a[2]<<std::endl;

	std::cout << "sizeo of a: " << sizeof(a) 
			  << " size of p: "  << sizeof(*a) <<std::endl;

	g(x)=83;
	foo()=100;

	printReference(83);
	return 0;
}

// compile gcc rvalue.cpp