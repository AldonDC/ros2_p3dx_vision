import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge
import cv2
import numpy as np

class VisualServoingController(Node):
    def __init__(self):
        super().__init__('visual_servoing_controller')

        self.bridge = CvBridge()
        self.cmd_pub = self.create_publisher(Twist, '/cmd_vel', 10)
        self.image_sub = self.create_subscription(Image, 'camera_image', self.image_callback, 10)

        # PID Coeficientes (ahora como parámetros ajustables)
        self.declare_parameter('kp', 0.005)
        self.declare_parameter('ki', 0.0)
        self.declare_parameter('kd', 0.001)

        self.kp = self.get_parameter('kp').get_parameter_value().double_value
        self.ki = self.get_parameter('ki').get_parameter_value().double_value
        self.kd = self.get_parameter('kd').get_parameter_value().double_value

        self.prev_error = 0.0
        self.integral = 0.0

        self.get_logger().info('🎯 Nodo de control visual iniciado')

    def image_callback(self, msg):
        try:
            frame = self.bridge.imgmsg_to_cv2(msg, desired_encoding='bgr8')
        except Exception as e:
            self.get_logger().error(f'Error al convertir imagen: {e}')
            return

        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

        # Detecta color naranja (ajustable)
        lower_orange = np.array([5, 100, 100])
        upper_orange = np.array([25, 255, 255])
        mask = cv2.inRange(hsv, lower_orange, upper_orange)

        contours, _ = cv2.findContours(mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

        if contours:
            largest = max(contours, key=cv2.contourArea)
            M = cv2.moments(largest)
            if M['m00'] > 0:
                cx = int(M['m10'] / M['m00'])
                cy = int(M['m01'] / M['m00'])

                error = cx - frame.shape[1] // 2

                self.integral += error
                derivative = error - self.prev_error
                angular_z = self.kp * error + self.ki * self.integral + self.kd * derivative
                self.prev_error = error

                # Control proporcional al área para variar velocidad
                area = cv2.contourArea(largest)
                linear_x = 0.1 if area < 1500 else 0.05  # más cerca = más lento

                twist = Twist()
                twist.linear.x = linear_x
                twist.angular.z = -angular_z
                self.cmd_pub.publish(twist)
                return

        # No se detecta la esfera, detener el robot
        twist = Twist()
        self.cmd_pub.publish(twist)


def main(args=None):
    rclpy.init(args=args)
    node = VisualServoingController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
