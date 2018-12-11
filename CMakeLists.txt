cmake_minimum_required(VERSION 2.8.3)
project(birl_kitting_experiment_simulation)


find_package(catkin REQUIRED COMPONENTS
  rospy
  birl_baxter_description
  baxter_gazebo
  birl_gripper_description
)

catkin_python_setup()

catkin_package(
 CATKIN_DEPENDS birl_baxter_description  baxter_gazebo birl_gripper_description)

 include_directories(
  ${catkin_INCLUDE_DIRS}
)