#include <LibB/ClassB1.h>

namespace LibB {

#define a "ClassB1"
#define b a a a a a a a
#define c b b b b b b b
#define d c c c c c c c
#define e d d d d d d d
#define f e e e e e e e
#define g f f f f f f f
#define h g g g g g g g
#define i h h h h h h h

ClassB1::ClassB1()
{
    const char* z = i;
}

ClassB1::~ClassB1()
{
    
}

}