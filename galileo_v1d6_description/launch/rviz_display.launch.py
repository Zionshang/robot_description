import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node


package_name = "galileo_v1d6_description"
urdf_name = "galileo_v1d6.urdf"


def generate_launch_description():
    urdf_file_path = os.path.join(
        get_package_share_directory(package_name), "urdf", urdf_name
    )

    rviz2_node = Node(
        package="rviz2",
        executable="rviz2",
        name="rviz2",
        output="screen",
    )

    joint_state_publisher_node = Node(
        package="joint_state_publisher_gui",
        executable="joint_state_publisher_gui",
        name="joint_state_publisher_gui",
        arguments=[urdf_file_path],
    )

    robot_state_publisher_node = Node(
        package="robot_state_publisher",
        executable="robot_state_publisher",
        arguments=[urdf_file_path],
    )

    return LaunchDescription(
        [rviz2_node, joint_state_publisher_node, robot_state_publisher_node]
    )
