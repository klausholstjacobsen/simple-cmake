#include <LibC/ClassC1.h>

#include <stdio.h>
#include <iostream>

int main() {

    std::cout << "Hello World!" << std::endl;

    LibC::ClassC1 c;
    auto t = c.GetText();

    std::cout << t << std::endl;

    return 0;
}
