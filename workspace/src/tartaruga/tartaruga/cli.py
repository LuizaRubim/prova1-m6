import argparse
from collections import deque
from geometry_msgs.msg import Twist
import rclpy 
from rclpy.node import Node

dq = deque()

vx=0.0
vy=0.0
vt=0.0
t=0

class MinimalPublisher(Node):

    def __init__(self):
        super().__init__('minimal_publisher')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)
        timer_period = dq[0][3][0]  # seconds
        self.timer = self.create_timer(timer_period, self.timer_callback)
        self.i = 0

    def timer_callback(self):
        msg = Twist()
        msg.linear.x = dq[0][0]
        msg.linear.y = dq[0][1]
        msg.angular.z = dq[0][2]
        self.publisher_.publish(msg)
        self.i += 1


def main(args=None):
    parser = argparse.ArgumentParser(description='recebe movimentos da tartaruga')
    parser.add_argument('--vx', metavar='N', type=float, nargs=1,
                        help='velocity in x axis')
    parser.add_argument('--vy', metavar='N', type=float, nargs=1,
                        help='velocity in y axis')
    parser.add_argument('--vt', metavar='N', type=float, nargs=1,
                        help='angular velocity')
    parser.add_argument('--t', metavar='N', type=int, nargs=1,
                        help='time in miliseconds')

    args_cli = parser.parse_args(["--vx", "1.0", "--vy", "0.0", "--vt", "0.0", "--t", "1000"])

    if args_cli.vx!=0 and args_cli.vy!=0 and args_cli.vt!=0 and args_cli.t!=0:
        dq.append([args_cli.vx, args_cli.vy, args_cli.vt, args_cli.t])
    else:
        dq.append([0.0, 0.0, 0.0, 0])

    print(dq[0])

    rclpy.init(args=args)

    minimal_publisher = MinimalPublisher()

    rclpy.spin(minimal_publisher)
    
    # Destroy the node explicitly
    # (optional - otherwise it will be done automatically
    # when the garbage collector destroys the node object)
    minimal_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()


