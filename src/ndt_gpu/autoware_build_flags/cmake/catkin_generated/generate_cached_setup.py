# -*- coding: utf-8 -*-
from __future__ import print_function
import argparse
import os
import stat
import sys

# find the import for catkin's python package - either from source space or from an installed underlay
if os.path.exists(os.path.join('/opt/ros/kinetic/share/catkin/cmake', 'catkinConfig.cmake.in')):
    sys.path.insert(0, os.path.join('/opt/ros/kinetic/share/catkin/cmake', '..', 'python'))
try:
    from catkin.environment_cache import generate_environment_script
except ImportError:
    # search for catkin package in all workspaces and prepend to path
    for workspace in "/opt/ros/kinetic".split(';'):
        python_path = os.path.join(workspace, 'lib/python2.7/dist-packages')
        if os.path.isdir(os.path.join(python_path, 'catkin')):
            sys.path.insert(0, python_path)
            break
    from catkin.environment_cache import generate_environment_script

code = generate_environment_script('/home/amey/NDT_GPU_Autoware/autoware-623c51c8dc29f2d9d66ed6cbd39bcfb1d45183b7-ros-src-computing-perception-localization-lib-ndt_gpu/ros/src/computing/perception/localization/lib/ndt_gpu/common-master-autoware_build_flags/autoware_build_flags/cmake/devel/env.sh')

output_filename = '/home/amey/NDT_GPU_Autoware/autoware-623c51c8dc29f2d9d66ed6cbd39bcfb1d45183b7-ros-src-computing-perception-localization-lib-ndt_gpu/ros/src/computing/perception/localization/lib/ndt_gpu/common-master-autoware_build_flags/autoware_build_flags/cmake/catkin_generated/setup_cached.sh'
with open(output_filename, 'w') as f:
    #print('Generate script for cached setup "%s"' % output_filename)
    f.write('\n'.join(code))

mode = os.stat(output_filename).st_mode
os.chmod(output_filename, mode | stat.S_IXUSR)
