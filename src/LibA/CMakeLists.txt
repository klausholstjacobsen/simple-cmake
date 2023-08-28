project (LibA LANGUAGES CXX)

add_library(${PROJECT_NAME} 
    src/ClassA1.cpp
    src/ClassA2.cpp
    src/ClassA3.cpp
    src/ClassA4.cpp
    src/ClassA5.cpp
    src/ClassA6.cpp
    src/ClassA7.cpp
    src/ClassA8.cpp
    src/ClassA9.cpp
    src/ClassA10.cpp
)

target_include_directories(${PROJECT_NAME} PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)

target_link_libraries(${PROJECT_NAME}
)

#add_dependencies(${PROJECT_NAME}
#    CustomCommand1
#)