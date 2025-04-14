import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class TrajectoryController(Node):
    def __init__(self):
        super().__init__('trajectory_controller')

        self.get_logger().info('🌀 Modo: círculo pequeño activado')

        self.publisher_ = self.create_publisher(Twist, '/cmd_vel', 10)
        self.timer = self.create_timer(0.1, self.timer_callback)

    def timer_callback(self):
        msg = Twist()

        # Movimiento circular pequeño
        msg.linear.x = 0.0125    # velocidad lineal reducida
        msg.angular.z = 1.250    # velocidad angular más alta para giro cerrado

        self.publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TrajectoryController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
