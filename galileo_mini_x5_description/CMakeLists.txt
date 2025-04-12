cmake_minimum_required(VERSION 3.8)
project(galileo_mini_x5_description)

find_package(ament_cmake REQUIRED)

install(
		DIRECTORY launch meshes urdf
		DESTINATION share/${PROJECT_NAME}/
)

ament_package()