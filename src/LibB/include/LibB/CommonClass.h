#include <string>

class CommonClass
{
public:
    CommonClass();
    virtual ~CommonClass();

    std::string GimmeString();

    std::string GimmePrivateString();

private:
    std::string private_string;
};
