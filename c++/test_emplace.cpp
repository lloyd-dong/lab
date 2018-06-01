#include <vector>  
#include <string>  
#include <iostream>  
  
struct President  
{  
    std::string name;  
    std::string country;  
    int year;  
  
    President(std::string p_name, std::string p_country, int p_year)  
        : name(std::move(p_name)), country(std::move(p_country)), year(p_year)  
    {  
        std::cout << "I am being constructed. my name is: " << p_name <<":"<<name<< std::endl;  
    }  
    President(const President& other)  
        : name(std::move(other.name)), country(std::move(other.country)), year(other.year)  
    {  
        std::cout << "I am being copied. my name is: "<< other.name<< ":"<<name<< std::endl;  
    }

    President(President&& other)  
        : name(std::move(other.name)), country(std::move(other.country)), year(other.year)  
    {  
        std::cout << "I am being moved. my name : "<< other.name <<":"<<name<< std::endl;  
    }  
    President& operator=(const President& other);  
    ~President(){
       std::cout << name<<" : I am being destructed.\n";   
    }
};  
  
int main()  
{  
    std::vector<President> elections;  
    std::cout << "emplace_back:\n";  
    elections.emplace_back("Nelson Mandela", "South Africa", 1994); //没有类的创建  
    
    for (President const& president: elections) {  
        std::cout << president.name << " was elected president of "  
            << president.country << " in " << president.year << ".\n";  
    }  


    std::cout << "\npush_back:\n"; 

    std::vector<President> reElections;   
    std::string name ="Franklin Delano Roosevelt";
    reElections.push_back(President(name, "the USA", 1936));  
    
    std::cout << "\n president 2 \n";  
    President p1= President("Lincon", "USA",1900);
    //President *p= new President("Lincon", "USA",1900);
    reElections.push_back(p1);

    std::cout<< "name is: " << name <<std::endl;

    std::cout << "\nContents:\n";    
    for (President const& president: reElections) {  
        std::cout << president.name << " was re-elected president of "  
            << president.country << " in " << president.year << ".\n";  
    }  
} 