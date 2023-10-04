#include <cstdlib>
#include <LibB/CommonClass.h>
#include <iostream>

int main(int argc, char* argv[]) 
{  
    CommonClass c;
    std::string s = c.GimmeString();
    std::cout << s << std::endl;

    return EXIT_SUCCESS;
}