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
	Person(string p_name, int p_age):name(move(p_name)), age(p_age),id(g_id++){
		cout << "1000 p.name " <<p_name << " my name " <<name << " id " << id << "\n";
	}
	Person(Person&& p):name(move(p.name)), age(p.age){
		id = g_id++;
		cout << "2000 p.name " <<p.name << " p.id " <<p.id << " my name " <<name <<" id " << id << "\n";
	}

	// this is copy constructor, without this, vector.push_back(a_person) will fail to be compiled
	Person(const Person& p):name(move(p.name)), age(p.age){
		id = g_id++;
		cout << "2500 p.name " <<p.name << " p.id " <<p.id << " my name " <<name <<" id " << id << "\n";		
	}	
	~Person(){
		cout<< "3000 name " << name << " id " << id << "\n";
	}
};

int main()
{
	vector<Person> vp;

	cout<<"1 : \n"<<endl;		
	Person p1 = Person("A1", 21);	
	Person p2("A2",22 )
	// vp.push_back(pa);

	// cout<<"2 : \n"<<endl;
	// String a = "A2";	 
	// vp.push_back(Person(a, 21));
	// cout<< a <<endl; //test move

	// cout<<"3 : \n";
	// vp.emplace_back("A3",22);

	cout<<"4 : \n" ;
}