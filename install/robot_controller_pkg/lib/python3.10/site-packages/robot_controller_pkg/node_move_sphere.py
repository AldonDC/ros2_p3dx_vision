# robot_controller_pkg/node_move_sphere.py

import rclpy
from rclpy.node import Node
from coppeliasim_zmqremoteapi_client import RemoteAPIClient
import math
import time


class SphereMover(Node):
    def __init__(self):
        super().__init__('sphere_mover_node')

        # Conexión con CoppeliaSim
        try:
            self.client = RemoteAPIClient()
            self.sim = self.client.getObject('sim')
            self.sphere = self.sim.getObject('/Sphere')
            self.get_logger().info('✅ Conectado a CoppeliaSim y esfera detectada')
        except Exception as e:
            self.get_logger().error(f'❌ Error al conectar o localizar la esfera: {e}')
            raise SystemExit

        # Parámetros de trayectoria
        self.radius = 0.3
        self.height = 0.1
        self.start_time = time.time()

        # Temporizador de actualización de posición (20 Hz)
        self.timer = self.create_timer(0.05, self.move_sphere)
        self.get_logger().info('🟠 Nodo de movimiento de esfera iniciado')

    def move_sphere(self):
        t = time.time() - self.start_time

        # Movimiento circular en plano XY y ligero oscilatorio en Z
        x = self.radius * math.sin(t)
        y = self.radius * math.cos(t)
        z = self.height + 0.02 * math.sin(0.5 * t)

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


if __name__ == '__main__':
    main()
