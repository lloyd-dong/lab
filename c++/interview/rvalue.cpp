#include <iostream>
#include <vector>
#include <string>
using namespace std;

//g++ rvalue.cpp -std=c++11 -o out/rvalue 
//rvalue is C++11 feature

int g_id=0;
struct Person  
{
	string name;
	int age;
	int id;
	//this is required if init vecotr with size
	Person ():id(g_id++){
		cout <<"Person () id " << id << endl;
	}
	Person & operator=( const Person &rhs ) {
		if (this == &rhs)
			return *this;
		cout << "Person & operator= id " << id << endl;
		this->name = rhs.name;
		this->age = rhs.age;
		//this->id  = rhs.id;
		return *this;
	}
	//Person & operator=( const Person &rhs ) =default;
	Person(string p_name, int p_age):name(move(p_name)), age(p_age),id(g_id++){
		cout << "Person(name, age) p.name " <<p_name << " my name " <<name << " id " << id << endl;
	}
	//if move constructure is defined, copy constructor won't be generated automatically
	//note: copy constructor is implicitly deleted because 'Person' has a user-declared move       constructor。
	Person(Person&& p):name(move(p.name)), age(p.age),id(g_id++){
		cout << "Person(Person&& p) p.name " <<p.name << " p.id " <<p.id << " my name " <<name <<" id " << id << endl;
	}

	// this is copy constructor, without this, vector.push_back(a_person) will fail to be compiled
	Person(const Person& p):name(move(p.name)), age(p.age),id(g_id++){
		cout << "Person(const Person& p) p.name " <<p.name << " p.id " <<p.id << " my name " <<name <<" id " << id << endl;		
	}	
	~Person(){
		cout<< "~Person() name " << name << " id " << id << endl;
	}
};

int main()
{
	vector<Person> vp(10);

	cout << "1 : " << endl;		
	Person p1_0("A1_0",210 ); 
	//initialized as same as p1, not initialize p2 with default constructor, and an anonymous Person, then = operation
	Person p1_1 = Person("A1_1", 211); 

	//amazing, this one calls Person(const Person& p)
	// https://msdn.microsoft.com/en-us/library/87by589c.aspx, Copy Assignment Operators
	Person p1_2 = p1_0; 
	Person p1_3(p1_0);

	//this one calls ====
	Person p1_4;
	p1_4 = p1_0;

	cout <<"2 : "<<endl;	
	//push_back overload const ref and right value T&&
	vp.push_back(p1_0); //created a new Person id 5, copy from p1_0, like Person p5(p1_0), you have to create p1_0 first
	vp.push_back(Person("A2_1",221)); //one more step of creation and desctroy, call rvalue
	//vp.push_back("A2_3", 223);  this one doesn't work

	//emplace_back overlaod copy and move constructor as well
	//emplace_back is from c++ 11
	// vp.emplace_back("A2",220); //create new Person in vp directly,  saved creation of p1_0
	// vp.emplace_back(Person("A2_2",222)); //call rvalue
	


	cout<<"4 :" <<endl ;
}