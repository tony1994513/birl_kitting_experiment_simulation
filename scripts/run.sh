#!/bin/bash
echo "launch robot action server"
xterm -hold -e rosrun baxter_interface joint_trajectory_action_server.py &
sleep 5
echo "move robot the start pose"
xterm -hold -e rosrun birl_trajectory_excution move_r_arm_home.py &
sleep 10
echo "setup tables"
xterm -hold -e roslaunch birl_kitting_experiment_simulation load_gazebo_env.launch &
exit 0