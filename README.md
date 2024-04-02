English| [简体中文](./README_cn.md)

# Feature Introduction

`hobot_shm` is used to configure the ROS2 zero-copy environment, including the [shm_fastdds.xml](./config/shm_fastdds.xml) configuration file and [hobot_shm.launch.py](./launch/hobot_shm.launch.py) configuration script.

# Instructions

To use, include the `hobot_shm.launch.py` configuration script in your launch startup script using the `IncludeLaunchDescription` command.

```python
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory

def generate_launch_description():
    return LaunchDescription([
        # Start the zero-copy environment configuration node
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(
                    get_package_share_directory('hobot_shm'),
                    'launch/hobot_shm.launch.py'))
        )
    ])
```