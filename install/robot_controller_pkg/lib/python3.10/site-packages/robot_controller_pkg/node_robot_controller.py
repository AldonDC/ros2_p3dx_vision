import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
from coppeliasim_zmqremoteapi_client import RemoteAPIClient


class RobotController(Node):
    def __init__(self):
        super().__init__('robot_controller_node')

        try:
            self.client = RemoteAPIClient()
            self.sim = self.client.getObject('sim')
            self.sim.startSimulation()
            self.get_logger().info('✅ Conectado a CoppeliaSim y simulación iniciada')
        except Exception as e:
            self.get_logger().error(f'❌ Error al conectar con CoppeliaSim: {e}')
            raise SystemExit

        # Obtener handlers de los motores
        try:
            self.left_motor = self.sim.getObject('/PioneerP3DX/leftMotor')
            self.right_motor = self.sim.getObject('/PioneerP3DX/rightMotor')
        except Exception as e:
            self.get_logger().error(f'❌ No se pudo obtener los motores: {e}')
            raise SystemExit

        # Parámetros del robot
        self.wheel_radius = 0.0975  # radio de la rueda en metros
        self.wheel_base = 0.381     # distancia entre ruedas en metros

        # Subscripción a comandos de velocidad
        self.subscription = self.create_subscription(
            Twist,
            '/cmd_vel',
            self.cmd_vel_callback,
            10
        )

        self.log_counter = 0
        self.get_logger().info('🧠 Nodo de control del robot iniciado')

    def cmd_vel_callback(self, msg):
        v = msg.linear.x
        w = msg.angular.z

        # Cinemática inversa para robot diferencial
        v_l = (2 * v - w * self.wheel_base) / (2 * self.wheel_radius)
        v_r = (2 * v + w * self.wheel_base) / (2 * self.wheel_radius)

        # Aplicar velocidades suavizadas para evitar sacudidas bruscas
        v_l = max(min(v_l, 5.0), -5.0)
        v_r = max(min(v_r, 5.0), -5.0)

        # Enviar velocidades a los motores
        self.sim.setJointTargetVelocity(self.left_motor, v_l)
        self.sim.setJointTargetVelocity(self.right_motor, v_r)

        # Mostrar logs cada 10 ciclos (~1s)
        self.log_counter += 1
        if self.log_counter % 10 == 0:
            self.get_logger().info(
                f'v: {v:.2f} | w: {w:.2f} | v_l: {v_l:.2f} | v_r: {v_r:.2f}'
            )

    def shutdown(self):
        try:
            self.sim.stopSimulation()
            self.get_logger().info('🛑 Simulación detenida correctamente')
        except Exception as e:
            self.get_logger().warn(f'⚠️ No se pudo detener la simulación: {e}')


def main(args=None):
    rclpy.init(args=args)
    node = RobotController()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.shutdown()
        node.destroy_node()
        rclpy.shutdown()


if __name__ == '__main__':
    main()
