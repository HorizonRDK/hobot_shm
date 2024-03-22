# Copyright (c) 2022，Horizon Robotics.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

from launch import LaunchDescription
from ament_index_python.packages import get_package_prefix

def generate_launch_description():
    hobot_shm_config_file = os.path.join(
        get_package_prefix('hobot_shm'),
        "lib/hobot_shm/config/shm_fastdds.xml")
    # print("hobot_shm_config_file is ", hobot_shm_config_file)

    os.environ.setdefault('RMW_IMPLEMENTATION', 'rmw_fastrtps_cpp')
    os.environ.setdefault('FASTRTPS_DEFAULT_PROFILES_FILE', hobot_shm_config_file)
    os.environ.setdefault('RMW_FASTRTPS_USE_QOS_FROM_XML', '1')
    # print("RMW_FASTRTPS_USE_QOS_FROM_XML is ", os.getenv('RMW_FASTRTPS_USE_QOS_FROM_XML'))

    return LaunchDescription([
            ])