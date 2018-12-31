#include <iostream>
#include <memory>
class A {
	public:
		A(){
			std::cout << "A()" <<std::endl;
		}
		A(double d) {
			std::cout << "A(double d)" <<std::endl;
		}
		~A(){
			std::cout << "~A()" <<std::endl;
		} 
		virtual void fun1(){
			std::cout << "fun1()" <<std::endl;
		}
		void fun2(){
			std::cout << "A::fun2()" <<std::endl;		
		}
};
class A_A :public A {
	public:
		void fun1(){
			std::cout << "A_A::fun1()" <<std::endl;	
		}
		void fun2(){
			std::cout << "A_A::fun2()" <<std::endl;		
		}
		~A_A(){
			std::cout << "~A_A()" <<std::endl;
		} 

};

void test_share(std::shared_ptr<A> a){
	std::cout << "=========================" <<std::endl;	
	a->fun2();
}
void test_implicit_convert(){
	std::cout << "=========================" <<std::endl;	
	A a = 2.3;
}
void test_v_table(){
	std::cout << "=========================" <<std::endl;	
	std::shared_ptr<A> a1 = std::make_shared<A_A>();	
	a1->fun1();
	a1->fun2();

	auto a2 = std::make_shared<A_A>();
	a2->fun1();
	a2->fun2();
}
void test_cast(){
	std::cout << "=========================" <<std::endl;	
	A* a2 = static_cast<A *>(new A_A());
	A* a3 = (A*) new A_A();
	std::shared_ptr<A> a4 = std::make_shared<A_A>();	
}
int main(int argc, char* argv[]){
	//test_implicit_convert();
	// test_v_table();
	// test_cast();
	std::shared_ptr<A> a4 = std::make_shared<A_A>();	
	test_share(a4);
}