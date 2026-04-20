import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    vehicle_platform_share = get_package_share_directory("vehicle_platform")
    delegated_launch = os.path.join(vehicle_platform_share, "launch", "system_bringup.launch.py")

    return LaunchDescription(
        [
            IncludeLaunchDescription(
                PythonLaunchDescriptionSource(delegated_launch),
            )
        ]
    )