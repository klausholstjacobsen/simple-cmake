#include <LibB/CommonClass.h>

CommonClass::CommonClass()
{
    private_string = "private string";
}

CommonClass::~CommonClass()
{
    
}

std::string CommonClass::GimmeString()
{
    return "libb";
}

std::string CommonClass::GimmePrivateString()
{
    return private_string;
}

