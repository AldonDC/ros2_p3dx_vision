# node_robot_controller.py

import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller')
        self.subscription = self.create_subscription(
            Twist,
            'cmd_vel',
            self.listener_callback,
            10
        )

        client = RemoteAPIClient()
        self.sim = client.getObject('sim')
        self.left_motor = self.sim.getObject('/PioneerP3DX/leftMotor')
        self.right_motor = self.sim.getObject('/PioneerP3DX/rightMotor')

        self.get_logger().info('Robot controller node started')

    def listener_callback(self, msg):
        v = msg.linear.x
        w = msg.angular.z
        L = 0.381  # distancia entre ruedas en m (aprox. del Pioneer P3DX)
        R = 0.0975  # radio rueda aprox

        v_l = (2*v - w*L) / (2*R)
        v_r = (2*v + w*L) / (2*R)

        self.sim.setJointTargetVelocity(self.left_motor, v_l)
        self.sim.setJointTargetVelocity(self.right_motor, v_r)


def main(args=None):
    rclpy.init(args=args)
    node = RobotController()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
