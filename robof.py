#!/usr/bin/env python
import rospy
 
if __name__=='__main__':
    rospy.init_node('my_first_node')##initializing the node
    rospy.loginfo("this is my first node")
    # rospy.sleep(1)
    # rospy.loginfo('heheh')#ok done
    rate=rospy.Rate(10)#10 times a sec,its like freq
    # print(rate)
    while not rospy.is_shutdown():###when u ill the node it is shut
        rospy.loginfo('hello')
        rate.sleep()###sleeps for 0.1 sec,cause of the rate set,sleeps acc to the rate set
       ##all done now


