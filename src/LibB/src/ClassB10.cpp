#include <LibB/ClassB10.h>

namespace LibB {

#define a "ClassB10"
#define b a a a a a a a
#define c b b b b b b b
#define d c c c c c c c
#define e d d d d d d d
#define f e e e e e e e
#define g f f f f f f f
#define h g g g g g g g
#define i h h h h h h h

ClassB10::ClassB10()
{
    const char* z = i;
}

ClassB10::~ClassB10()
{
    
}

}