#include <LibA/ClassA5.h>

namespace LibA {

#define a "ClassA5"
#define b a a a a a a a
#define c b b b b b b b
#define d c c c c c c c
#define e d d d d d d d
#define f e e e e e e e
#define g f f f f f f f
#define h g g g g g g g
#define i h h h h h h h

ClassA5::ClassA5()
{
    const char* z = i;
}

ClassA5::~ClassA5()
{
    
}

}