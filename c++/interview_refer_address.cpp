#include <iostream>
using namespace std;

void swap(int&   x, int  &   y, int   &z){
	z= x;
	x=y;
	y=z;
}

void print_array(int* a){
	int len = sizeof(a)/sizeof(*a);
	cout<<len << ":" <<sizeof(a) <<":"<<sizeof(*a)<<endl;
	for (int i=0;i<len;i++){
		cout<<a[i];
	}
	cout<<endl;
}

int main(){
	int x=10, y=0, z;
	swap(x,y,z);
	cout << "x: " <<x <<" y: " <<y <<endl;

	int a[]={1,2,3,4,5,6};
	cout<<"size of array:" <<sizeof(a) <<endl;
	print_array(a);
	return 0;
} 