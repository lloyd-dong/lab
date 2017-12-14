#include <iostream>

// Template Declaration
template<typename T>
class Queue
{
public:
    Queue();
    ~Queue();
    void push(T e);
    T pop();
private:
    struct node
    {
	T data;
	node* next;
    };
    typedef node NODE;
    NODE* mHead;
};

// template definition
template<typename T>
Queue<T>::Queue() 
{ 
    mHead = NULL;
}

template<typename T>
Queue<T>::~Queue() 
{
    NODE *tmp;
    while(mHead) {
	tmp = mHead;
	mHead = mHead->next;
	delete tmp;
    }
}

template<typename T>
void Queue<T>::push(T e)
{
    NODE *ptr = new node;
    ptr->data = e;
    ptr->next = NULL;
    if(mHead == NULL) {
	mHead = ptr;
	return;
    }
    NODE *cur = mHead;
    while(cur) {
	if(cur->next == NULL) {
	    cur->next = ptr;
	    return;
	}
	cur = cur->next;
    }
}

template<typename T>
T Queue<T>::pop()
{
    if(mHead == NULL) return NULL;
    NODE *tmp = mHead;
    T d = mHead->data;
    mHead = mHead->next;
    delete tmp;
    return d;
}