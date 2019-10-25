# LIDAR-based-odometry-using-EKF-and-NDT-matching-algorithm-running-on-GPU

This repo is a work at the Embedded Computing Lab at Worcester Polytechnic Institute.

This repository helps run the Normal Distributions transform algorithm on GPU. 

Changes to make before running the repo - 
1. Update the address of "autoware_build_flags" in line 18 of src/ndt_gpu/CMakeLists.txt
2. Update cuda path in line 70 of src/ndt_gpu/CMakeLists.txt
3. Update the NDT_GPU_LIB path in line 111 of src/ndt_mapping_localization/src/vehicle_localization/CMakeLists.txt
4. Update cuda path in line 135 of src/ndt_mapping_localization/src/vehicle_localization/CMakeLists.txt
5. Update adress in line 166 of src/ndt_mapping_localization/src/vehicle_localization/CMakeLists.txt
6. Update cuda address in line 200 of src/ndt_mapping_localization/src/vehicle_localization/CMakeLists.txt
7. Perform step 3,4,5 and 6 for src/ndt_mapping_localization/src/vehicle_mapping/CMakeLists.txt
8. Update the autoware_build_flags path on line 199 of src/ndt_gpu/autoware_build_flags/cmake/catkin_generated/installspace/autoware_build_flagsConfig

To run the repo, follow the steps below - 
1. clone the repo
2. cd into the repo folder and run ./lidar_odom.sh
3. source devel/setup.bash
4. roslaunch src/ndt_mapping_localization/src/vehicle_localization/launch/map_localization.launch 
5. Set the 2D pose estimate on the rviz map
6. Run the rosbag which is available at https://drive.google.com/open?id=1mqBURRoouFT1HYkWjkjENcotXf75Tz0u

Note: Please be aware that this repo uses cuda 9.0. If you wish to switch to cuda 10, you will have to update the above mentioned(steps 1,3 and 7) CMakeLists.txt. This repo is untested on cuda 10.0.
