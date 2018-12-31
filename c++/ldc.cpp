#include <fstream>
#include <iostream>
using namespace std;

int main(){
	ifstream in("name.in");
	ofstream out("name.out");

	int n;
	string name;
	in >> n;
	string str[n];
	for (int i=0; i<n; i++){
		in >> str[i];
	}
	in >> name;
	int flg=0;
	for (int i =0; i<n; i++){
		cout<<i << ":" <<str[i] <<" == " << name <<endl;
		if (str[i].compare(name)==0){
			out << i+1 << " " <<name;
			flg++;
			break;
		}
	}
	if (flg==0){
		out << -1;
	}
	in.close();
	out.close();
	return 0;
	
}