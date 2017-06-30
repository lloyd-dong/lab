#include <stdexcept>
#include <string>
#include <thread>
enum
    {
        NUM_OF_SLOTS = 34
    };  
int main(){
	int nThreads = std::thread::hardware_concurrency();
	std::string pmpt= "thread # " + std::to_string((long long)nThreads) +
			" > slot num " + std::to_string((long long)NUM_OF_SLOTS);
	throw std::out_of_range(pmpt);
}
