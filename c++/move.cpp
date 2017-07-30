#include <iostream>
#include <vector>
#include <string>

int g_id=0;
struct Person  
{
	std::string name;
	int age;
	int id;
	Person(const std::string& p_name, int p_age)
		:name(std::move(p_name)), age(p_age),id(g_id++){
		std::cout << "\n 1000 p.name  " <<p_name 
		          << "\n      my name " <<name << " id " << id << "\n";
	}
	Person(Person&& p)
		:name(std::move(p.name)), age(p.age){
		id = g_id++;
		std::cout << "\n 2000 p.name  " <<p.name << " p.id " <<p.id
		          << "\n      my name " <<name <<" id " << id << "\n";
	}
	Person(const Person& p)
		:name(std::move(p.name)), age(p.age){
		id = g_id++;
		std::cout << "\n 3000 p.name  " <<p.name << " p.id " <<p.id
		          << "\n      my name " <<name <<" id " << id << "\n";
		
	}	
	~Person(){
		std::cout<< "\n 4000 name " << name << " id " << id << "\n";
	}
};

int main()
{
	std::string a= "Zhang San";
	Person pa = Person(a, 20);
	std::cout<<"1 : "<<a <<std::endl;
	std::vector<Person> vp;
	vp.push_back(pa);
	std::cout<<"2 : "<<a <<std::endl;
	a = "Li Si";
	vp.push_back(Person(a, 21));
	std::cout<<"3 : \n";
	vp.emplace_back("Zhao 5",22);
	std::cout<<"4 : \n" ;
}