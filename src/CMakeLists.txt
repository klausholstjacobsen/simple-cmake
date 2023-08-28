cmake_minimum_required(VERSION 3.19.0 FATAL_ERROR)

project(simple-cmake LANGUAGES CXX)

#set(CMAKE_VERBOSE_MAKEFILE true)

enable_testing()

add_subdirectory(Custom1)
add_subdirectory(LibA)
add_subdirectory(LibB)
add_subdirectory(LibC)
add_subdirectory(Exe1)
