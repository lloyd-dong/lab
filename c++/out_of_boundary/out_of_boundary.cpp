#include <iostream>
#include <vector>
using namespace std;
int main ()
{
	vector<int> myvector ({0,1,2,3,4});    

	cout << "The contents of myvector are:";
	//for (std::vector<int>::iterator it = first.begin(); it != first.end(); ++it)
	for (auto it = myvector.begin(); it != myvector.end(); ++it)
	  cout << ' ' << *it;

	cout << "\ntest myvector [] \n";
  	int ch;
	while((ch= getchar()) != '.') {
		if (ch == '\n' ) continue;
		int position = ch - '0';		
  		printf("arr[%d] is %d\n", position, myvector[position]); 
	}

	cout << "\ntest myvector.at() \n";  
	while((ch= getchar()) != '.') {
		if (ch == '\n' ) continue;
		int position = ch - '0';		
  		printf("arr[%d] is %d\n", position, myvector.at(position)); 
	}

  	return 0;
}  