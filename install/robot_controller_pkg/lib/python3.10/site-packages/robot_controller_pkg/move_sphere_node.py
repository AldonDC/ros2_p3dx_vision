# robot_controller_pkg/node_move_sphere.py

import rclpy
from rclpy.node import Node
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import math
import time

class SphereMover(Node):
    def __init__(self):
        super().__init__('node_move_sphere')
        self.client = RemoteAPIClient()
        self.sim = self.client.getObject('sim')

        try:
            self.sphere = self.sim.getObject('/Sphere')
        except Exception as e:
            self.get_logger().error(f'❌ No se encontró la esfera: {e}')
            raise SystemExit

        self.start_time = time.time()
        self.timer = self.create_timer(0.05, self.move_sphere)
        self.get_logger().info('🟠 Nodo de movimiento de esfera iniciado')

    def move_sphere(self):
        t = time.time() - self.start_time
        x = 0.5 * math.sin(0.3 * t)
        y = 0.5 * math.cos(0.3 * t)
        z = 0.08  # altura constante

        try:
            self.sim.setObjectPosition(self.sphere, -1, [x, y, z])
        except Exception as e:
            self.get_logger().warn(f'⚠️ No se pudo mover la esfera: {e}')

def main(args=None):
    rclpy.init(args=args)
    node = SphereMover()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        rclpy.shutdown()
