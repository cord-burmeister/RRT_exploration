import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument, SetEnvironmentVariable
from launch_ros.substitutions import FindPackageShare
from launch.launch_description_sources import PythonLaunchDescriptionSource
 
def generate_launch_description():
    rviz_config_file = LaunchConfiguration('rviz_config_file')

    declare_rviz_config_file = DeclareLaunchArgument(
        'rviz_config_file', default_value=os.path.join(
    get_package_share_directory('single_agent_rrt'), 'rviz', 'rrt_exploration.rviz'), description='RVIZ config file')
    
    
    # rrt_exploration_node = Node(
    #     package="single_agent_rrt",
    #     executable="rrt_exploration",
    #     name='rrt_exploration',
    #     respawn=True,
    # )
    local_frontier_detector_node = Node(
        package="single_agent_rrt",
        executable="local_frontier_detector",
        name='local_frontier_detector',
        respawn=True,
    )
    global_frontier_detector_node = Node(
        package="single_agent_rrt",
        executable="global_frontier_detector",
        name='global_frontier_detector',
        respawn=True,
    )
    filter_node = Node(
        package="single_agent_rrt",
        executable="filter",
        name='filter',
        respawn=True,
    )
    
    return LaunchDescription([
        declare_rviz_config_file,
        # rrt_exploration_node,
        filter_node,
        local_frontier_detector_node,
        global_frontier_detector_node
    ])
