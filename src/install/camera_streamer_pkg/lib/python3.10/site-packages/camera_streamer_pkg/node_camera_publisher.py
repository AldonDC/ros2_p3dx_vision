# node_camera_publisher.py

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import numpy as np
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

class CameraPublisher(Node):
    def __init__(self):
        super().__init__('camera_publisher')
        self.publisher_ = self.create_publisher(Image, 'camera_image', 10)
        self.bridge = CvBridge()

        client = RemoteAPIClient()
        self.sim = client.getObject('sim')
        self.sensor = self.sim.getObject('/visionSensor')

        self.timer = self.create_timer(0.1, self.timer_callback)
        self.get_logger().info('Camera publisher node started')

    def timer_callback(self):
        img, resX, resY = self.sim.getVisionSensorCharImage(self.sensor)
        img = np.frombuffer(img, dtype=np.uint8).reshape(resY, resX, 3)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        img = cv2.flip(img, 0)
        msg = self.bridge.cv2_to_imgmsg(img, encoding='bgr8')
        self.publisher_.publish(msg)


def main(args=None):
    rclpy.init(args=args)
    node = CameraPublisher()
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
