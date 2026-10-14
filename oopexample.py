from robot import Robot
from roboticarms import RoboticArm
from roboticarms import PackagingSolution


#Creating instances of the classes

my_robot = Robot("R2D2", 30, 5 , 300) #myrobot_instance
my_robot2 = Robot("C3PO", 25, 3) #myrobot2_instance
my_robot3 = RoboticArm("FULL ROBOT", 10, True, "2cm") #myrobotbotharms_instance
robotic_arm_right = RoboticArm("ArmRightBot", 10, False, "2cm") #myrobotrightarm_instance
robotic_arm_left = RoboticArm("ArmLeftBot", 10, True, "2cm") #myrobotleftarm_instance
my_packaging_solution = PackagingSolution(robotic_arm_left, robotic_arm_right)



# #Robot Invocations

# print("Robot 1 and 2 Invocations:")
my_robot.print_info()
my_robot2.print_info()

# my_robot2.print_info()    

#Robotic Arm Invocations
print("Robot 3 and Robotic Arm Invocations:")
# my_robot3.print_info()
robotic_arm_right.print_info()
robotic_arm_left.print_info()
my_packaging_solution.package(1, 2, 3, 4, 5, 6)
# arm1 = RoboticArm("Arm1", 1, 36.5, 100)
# arm2 = RoboticArm("Arm2", 2, 37.0, 200)no

# arm1.print_info()
# arm2.print_info()

    

# #Robotic Arm Invocations
# print("Robotic Arm Invocations:")
# my_robot3.print_info()
# my_robot3.pick_object(1, "hello")
# my_robot3.place_object(3, 4)

