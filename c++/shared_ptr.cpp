#include <memory>
#include <iostream>
 
struct Foo {
    Foo() { std::cout << "Foo...\n"; }
    ~Foo() { std::cout << "~Foo...\n"; }
};
 
void test(const std::shared_ptr<Foo>& sh0){
    std::cout << "========= in test ==========="<< std::endl;
    std::cout << "in test " <<sh0.use_count() << '\n';
}
int main()
{
    {
        // declared a pointer, but not allocate mem
        std::cout << "constructor with no managed object\n";
        std::shared_ptr<Foo> sh1;
        std::cout << "sh1 usage count "<< sh1.use_count() << std::endl;
        std::cout << "===================="<< std::endl;
    }
 
    {
        std::cout << "constructor with object\n";
        // decalred pointer and allocated mem
        std::shared_ptr<Foo> sh2(new Foo);
        std::cout << "sh2 usage count " << sh2.use_count() << '\n';
        // usage +1
        std::shared_ptr<Foo> sh3(sh2);
        std::cout << "sh3 usage count "<< sh3.use_count() << '\n';
        // sh2 usage count is 2 as well
        test(sh2);

        // decalred pointer and allocated mem
        std::shared_ptr<Foo> sh4 = std::make_shared<Foo>();
        test(sh4);
    }
 
}