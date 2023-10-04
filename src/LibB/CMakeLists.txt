project (LibB LANGUAGES CXX)

add_library(${PROJECT_NAME} 
    src/ClassB1.cpp
    src/ClassB2.cpp
    src/ClassB3.cpp
    src/ClassB4.cpp
    src/ClassB5.cpp
    src/ClassB6.cpp
    src/ClassB7.cpp
    src/ClassB8.cpp
    src/ClassB9.cpp
    src/ClassB10.cpp
    src/CommonClass.cpp
)

target_include_directories(${PROJECT_NAME} PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)

target_link_libraries(${PROJECT_NAME}
    LibA
)
