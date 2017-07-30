// example for thread::join
#include <iostream>       // std::cout
#include <thread>         // std::thread, std::this_thread::sleep_for
#include <chrono>        
#include <vector> // std::chrono::seconds
using namespace std;
 
void pause_thread(int n) 
{
  std::cout << "start "<<n <<"\n";	
  std::this_thread::sleep_for (std::chrono::seconds(n));
  std::cout << "pause of " << n << " seconds ended\n";
}
void my_thread1(){
	pause_thread(3);
}
void my_thread2(){
	pause_thread(6);
} 
int main() 
{
  std::cout << "Spawning 3 threads...\n";
  std::vector<std::thread> tgroup;
  tgroup.emplace_back(std::bind(pause_thread, 6));
  tgroup.emplace_back(std::bind(pause_thread, 3));
  // std::thread t1 (my_thread1);
  // std::thread t2 (my_thread2);
  //std::thread t3 (pause_thread,1);
  std::cout << "Done spawning threads. Now waiting for them to join:\n";
 

  std::this_thread::sleep_for (std::chrono::seconds(10)); 
  // t1.join();
  // std::cout << "joined 1\n";
  // t2.join();
  // std::cout << "joined 2\n";
  // //t3.join();
  std::cout << "All threads joined!\n";

  return 0;
}