cmake_minimum_required(VERSION 3.19.0 FATAL_ERROR)

project(simple-cmake LANGUAGES CXX)

#set(CMAKE_VERBOSE_MAKEFILE true)
find_package(ZLIB CONFIG REQUIRED)
find_package(pugixml CONFIG REQUIRED)
find_package(CURL CONFIG REQUIRED)
find_package(OpenSSL CONFIG REQUIRED)

enable_testing()

add_subdirectory(src)
