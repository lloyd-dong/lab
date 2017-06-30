#include <iostream>
#include <typeinfo>
using namespace std;
int main(){
	enum Color {red, green, blue};		
	cout<< char('0'+red)<<": type "<<typeid(red).name()<<endl;
	enum  {red1, green1, blue1};	
	cout<< char('0'+red1)<<": type "<<typeid(red1).name()<<endl;
	if (red1==red){
		cout<<"red1==red"<<endl;
	}
}