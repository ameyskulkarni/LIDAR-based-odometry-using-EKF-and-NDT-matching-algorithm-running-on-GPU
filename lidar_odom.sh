#!/bin/bash

# This workspace requires ndt_gpu to be built first before building the other packages. Hence this bash scipt is useful to build the packages #sequentially.


catkin_make --only-pkg-with-deps -DCMAKE_BUILD_TYPE=Release ndt_gpu
cd build/
make install
cd ..
catkin_make -DCMAKE_BUILD_TYPE=Release -DCATKIN_WHITELIST_PACKAGES=""
source devel/setup.bash
