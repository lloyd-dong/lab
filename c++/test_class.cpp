#include <iostream>
class A{

	public:
	 A(){
		std::cout<<"A construcotr" <<std::endl;
	}
	A( A&& a){
		std::cout<<"A right value" <<std::endl;
	}
	A(const A& a){
		std::cout<<"A left copy \n";
	}
	 void say(){
		std::cout<<"A speak" <<std::endl;
	}
};

int main(){
	A a; 
	a.say();

	A a_1=A();
	a_1.say();
	a=a_1;

	return 0;
}