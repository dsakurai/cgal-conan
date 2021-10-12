cmake_minimum_required(VERSION 3.17)

project(test_cgal)

set(CMAKE_CXX_STANDARD 20)

set(CONAN_DISABLE_CHECK_COMPILER Yes)

include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup(KEEP_RPATHS)

foreach(target IN ITEMS boolean_operations arrangement_with_data ex_overlay_color)
    add_executable(${target} ${target}.cpp)
    target_link_libraries(${target}
            ${CONAN_LIBS}
            )
endforeach()
