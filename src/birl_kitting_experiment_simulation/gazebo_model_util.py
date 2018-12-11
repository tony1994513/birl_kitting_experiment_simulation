import sys,os
import rospy
import copy
from gazebo_msgs.srv import (
    SpawnModel,
    DeleteModel,
)
from gazebo_msgs.srv import GetModelState, GetModelStateRequest
from birl_trajectory_excution._constant import hover_height
from birl_trajectory_excution.utils import pose_to_list,handle_object_in_gazebo_offset

def get_model_pose(model_name,hover_flag=None):
    rospy.wait_for_service('/gazebo/get_model_state')
    req = GetModelStateRequest()
    req.model_name = model_name
    try:
        client = rospy.ServiceProxy('/gazebo/get_model_state', GetModelState)
        res = client(req)
    except rospy.ServiceException, e:
        print "Service call failed: %s"%e
    model_pose = copy.deepcopy(res.pose)
    pose_list = pose_to_list(model_pose)
    pose_list = handle_object_in_gazebo_offset(pose_list)
    if hover_flag != None:
        pose_list[2] = pose_list[2] + hover_height
        return pose_list
    pose_list[2] = pose_list[2] - 0.009
    return pose_list