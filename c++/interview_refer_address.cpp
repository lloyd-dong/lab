#include <iostream>
using namespace std;

void swap(int&   x, int  &   y, int   &z){
	z= x;
	x=y;
	y=z;
}
void swap2(int* x, int * y, int   *z){
	*z=*x;
	*x=*y;
	*y=*z;
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
	cout << "x: " <<x <<" y: " <<y << " z: " << z <<endl;

        swap2(&x, &y, &z);
	cout << "x: " <<x <<" y: " <<y << " z: " << z <<endl;

	int a[]={1,2,3,4,5,6};
	cout<<"size of array:" <<sizeof(a) <<endl;
	cout<<" size array element :" <<sizeof(a[0]) <<endl;
	print_array(a);
	return 0;
} 
