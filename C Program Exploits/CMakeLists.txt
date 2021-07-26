cmake_minimum_required(VERSION 3.14)
project(HW4)

set(CMAKE_C_STANDARD 99)

include_directories(sploits)
include_directories(targets)

add_executable(HW4
        sploits/ID
        sploits/Makefile
        sploits/shellcode.h
        sploits/sploit0.c
        sploits/sploit1.c
        sploits/sploit2.c
        sploits/sploit3.c
        sploits/sploit4.c
        targets/Makefile
        targets/target0.c
        targets/target1.c
        targets/target2.c
        targets/target3.c
        targets/target4.c)

#add_executable(HW4 targets/target0.c)
