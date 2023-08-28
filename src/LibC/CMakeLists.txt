project (LibC LANGUAGES CXX)

add_library(${PROJECT_NAME} 
    src/ClassC1.cpp
)

target_include_directories(${PROJECT_NAME} PUBLIC
    ${CMAKE_CURRENT_SOURCE_DIR}/include
)

target_link_libraries(${PROJECT_NAME}
)
