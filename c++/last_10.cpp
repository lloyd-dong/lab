#include <iostream>
#include <fstream>
#include <string>

int main() {
  std::ifstream file("numbers.text"); // open the file "example.txt"
  if (!file.is_open()) {
    std::cerr << "Error opening file" << std::endl;
    return 1;
  }

  std::string line;
  
  std::getline(file, line);
//   int start = 0;
//   for (int i=start; i< line.length(); i++){
//     if (i==start) {
//       cout << "(line[i];
//     }
//     else if (line[i] == ' ') {
//       cout << line[i+1];
//     }
//   }
  std::cout << line.substr(0,3);

 std::string out_str = "(" + line.substr(0,3) + ")" + line.substr(3,3) + "-" + line.substr(6,3);
 std::cout << out_str << std::endl;
  file.close();
  return 0;
}