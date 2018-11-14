1. checkout https://github.com/dniewinski/universal_robot/tree/ur_e,   use branch ur_e

2. checkout https://github.com/dniewinski/ur_modern_driver/tree/kinetic-devel, use branch kinetic-devel

3. install ros-kinetic related dependancies if complie fails

4. roslaunch ur_modern_driver ur5e_bringup.launch robot_ip:=10.10.11.38

5. rostopic echo /joint_states to see joint angles

6. get ur5e manual from official website

7. First I tried control the robot using URscript from command line, it is quite handy

rostopic pub /ur_driver/URScript std_msgs/String "movej([0,-1.57,0,-1.57,0,0],a=30, v=20, t=0, r=0)"

8. read script manual to understand how to set up the system and send approporate control. Basically, all commands in Chapter 2 of the script manual can be sent to the robot using this cmd method

9. try "test_move.py", use /follow_joint_trajectory interface to send a joint trajectory and then follows it

10. Next, try send /joint_speed using script. I found that this type of control interface is removed in dniewinski's ur_modern_driver version for some reason. 

/joint_speed is of type trajectory_msgs/JointTrajectory

So abandon this method temporarily

11. Peter and I found that RTDE is used to control external gripper

12. Next attempt is to write a loop and inside the loop use URscript to control the robot. This dose not work well with movej, but use speedj(or speedl) to control the speed is quite smooth, I wrote a joy demo "test_joint_speed.py"

before using this demo, system must have ros-kinetic-joy installed. and ur-modern-driver is sourced so that this demo script can find the driver


13. So a complete workflow to this point is

	A. power on the robot, make sure its network address is 10.10.11.38

	B. roslaunch ur_modern_driver ur5e_bringup.launch robot_ip:=10.10.11.38
	
	C. test_joint_speed.py 

