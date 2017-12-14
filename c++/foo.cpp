#include "t_template.h"
void foo()
{
    Queue<int> *i = new Queue<int>();
    i->push(10);
    i->push(20);
    i->pop();
    i->pop();
    delete i;
}
int main(){
	foo();
}