#include <iostream>
#include <vector>
#include <string>
using namespace std;
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
	string a= "Zhang San";
	Person pa = Person(a, 20);
	cout<<"1 : "<<a <<endl;
	vector<Person> vp;
	vp.push_back(pa);
	cout<<"2 : "<<a <<endl;
	a = "Li Si";
	vp.push_back(Person(a, 21));
	cout<<"3 : \n";
	vp.emplace_back("Zhao 5",22);
	cout<<"4 : \n" ;
}