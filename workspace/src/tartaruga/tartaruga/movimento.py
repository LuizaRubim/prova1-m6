import rclpy 
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import argparse
from collections import deque

dq = deque()

#código adicionado da ponderada
class TurtleMove(Node):
    def __init__(self):
        super().__init__("TurtleMove")
        # Cria um publisher para enviar comandos de movimento para a titiruga "turtle1"
        self.publisher=self.create_publisher(
            msg_type=Twist,
            topic="turtle1/cmd_vel",
            qos_profile=10
        )
        self.subscription = self.create_subscription(
            Twist,
            '/comandos',
            self.listener_callback,
            10)
        
        

#código adicionado da ponderada
def move_turtle(self,x,y,theta):
        msg=Twist()
        msg.linear.x=x
        msg.linear.y=y
        msg.angular.z=theta
        self.publisher.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    td = TurtleMove()

    vx=0.0
    vy=0.0
    vt=0.0
    t=0

    parser = argparse.ArgumentParser(description='recebe movimentos da tartaruga')
    parser.add_argument('--vx', metavar='N', type=float, nargs='1',
                        help='velocity in x axis')
    parser.add_argument('--vy', metavar='N', type=float, nargs='1',
                        help='velocity in y axis')
    parser.add_argument('--vt', metavar='N', type=float, nargs='1',
                        help='angular velocity')
    parser.add_argument('--t', metavar='N', type=int, nargs='1',
                        help='time in miliseconds')

    args = parser.parse_args()

    if vx!=0 and vy!=0 and vt!=0 and t!=0:
        dq.append([args.vx, args.vy, args.vt, args.t])
    else:
        dq.append([0.0, 0.0, 0.0, 0])

    

