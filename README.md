# 功能介绍

`hobot_shm`用于配置ROS2零拷贝环境，包含[shm_fastdds.xml](./config/shm_fastdds.xml)配置文件和[shm_fastdds.launch.py](./launch/shm_fastdds.launch.py)配置脚本。

# 使用方法

在launch启动脚本中使用`IncludeLaunchDescription`命令包含`hobot_shm.launch.py`配置脚本即可。

```python
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python import get_package_share_directory

def generate_launch_description():
    return LaunchDescription([
        # 启动零拷贝环境配置node
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(
                    get_package_share_directory('hobot_shm'),
                    'launch/hobot_shm.launch.py'))
        )
    ])
```