cmake_minimum_required(VERSION 2.8.3)
project(eposx_hardware)

find_package(catkin REQUIRED COMPONENTS
  battery_state_interface
  controller_manager
  diagnostic_updater
  eposx_library
  hardware_interface
  dynamic_joint_limits_interface
  roscpp
  sensor_msgs
  transmission_interface
  urdf
)

find_package(Boost REQUIRED COMPONENTS
  program_options
)

catkin_package(
  INCLUDE_DIRS include
  LIBRARIES epos_library_utils epos_manager epos_hardware
  CATKIN_DEPENDS 
  battery_state_interface 
  controller_manager 
  diagnostic_updater 
  eposx_library 
  hardware_interface 
  dynamic_joint_limits_interface
  roscpp 
  sensor_msgs
  transmission_interface
  urdf
)

###########
## Build ##
###########

include_directories(include)
include_directories(
  ${catkin_INCLUDE_DIRS}
)

# A collection of utilities for using the EPOS Command Libary
add_library(epos_library_utils
  src/util/utils.cpp
)
target_link_libraries(epos_library_utils
  ${catkin_LIBRARIES}
)


# Build tool to list available nodes
add_executable(list_nodes src/tools/list_nodes.cpp)
target_link_libraries(list_nodes
  ${catkin_LIBRARIES}
  ${Boost_LIBRARIES}
  epos_library_utils
)

# Build tool to list a devices state
add_executable(get_state src/tools/get_state.cpp)
target_link_libraries(get_state
  ${catkin_LIBRARIES}
  ${Boost_LIBRARIES}
  epos_library_utils
)

add_library(epos_manager
  src/util/epos_manager.cpp
  src/util/epos.cpp
  src/util/epos_operation_mode.cpp
  src/util/epos_diagnostic_updater.cpp
)
target_link_libraries(epos_manager
  ${catkin_LIBRARIES}
  epos_library_utils
)

add_library(epos_hardware
  src/util/epos_hardware.cpp
)
target_link_libraries(epos_hardware
  ${catkin_LIBRARIES}
  epos_manager
  epos_library_utils
)

add_executable(epos_hardware_node
  src/nodes/epos_hardware_node.cpp)
target_link_libraries(epos_hardware_node
  ${catkin_LIBRARIES}
  epos_hardware
)

#############
## Install ##
#############

install(DIRECTORY launch
  DESTINATION ${CATKIN_PACKAGE_SHARE_DESTINATION}
)

# Mark libraries and nodes for installation
install(TARGETS epos_library_utils epos_manager epos_hardware list_nodes get_state epos_hardware_node
  ARCHIVE DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  LIBRARY DESTINATION ${CATKIN_PACKAGE_LIB_DESTINATION}
  RUNTIME DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)

# Mark cpp header files for installation
install(DIRECTORY include/${PROJECT_NAME}/
  DESTINATION ${CATKIN_PACKAGE_INCLUDE_DESTINATION}
  FILES_MATCHING PATTERN "*.h"
  PATTERN ".svn" EXCLUDE
)
