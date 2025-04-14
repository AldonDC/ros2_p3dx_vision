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

        self.bridge = CvBridge()
        self.publisher_ = self.create_publisher(Image, 'camera_image', 10)

        # Mostrar una única ventana OpenCV
        self.window_name = "🎥 Cámara desde CoppeliaSim"
        self.show_window = True
        if self.show_window:
            cv2.namedWindow(self.window_name, cv2.WINDOW_NORMAL)

        # Conexión a CoppeliaSim y sensor
        try:
            client = RemoteAPIClient()
            self.sim = client.getObject('sim')
            self.sensor_handle = self.sim.getObject('/PioneerP3DX/visionSensor')
            self.get_logger().info('✅ Conectado con CoppeliaSim y sensor VisionSensor obtenido')
        except Exception as e:
            self.get_logger().error(f'❌ Error al conectar con CoppeliaSim: {e}')
            return

        self.timer = self.create_timer(0.1, self.timer_callback)
        self.get_logger().info('📡 Nodo de cámara iniciado y publicando...')

    def timer_callback(self):
        try:
            # Usar API moderna: sim.getVisionSensorImg
            img_data, resolution = self.sim.getVisionSensorImg(self.sensor_handle)
            resX, resY = resolution

            # Procesar imagen correctamente
            img = np.frombuffer(img_data, dtype=np.uint8).reshape((resY, resX, 3))
            img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
            img = cv2.flip(img, 180)  # Invertir verticalmente para que esté bien orientado

            # Escalar imagen (opcional)
            scale = 2  # Puedes cambiar a 1.5 si prefieres
            img_resized = cv2.resize(img, (resX * scale, resY * scale), interpolation=cv2.INTER_LINEAR)

            # Publicar mensaje ROS
            msg = self.bridge.cv2_to_imgmsg(img_resized, encoding='bgr8')
            self.publisher_.publish(msg)

            # Mostrar ventana OpenCV (solo una)
            if self.show_window:
                cv2.imshow(self.window_name, img_resized)
                cv2.waitKey(1)

        except Exception as e:
            self.get_logger().warn(f'⚠️ Error en lectura/publicación: {type(e).__name__} - {e}')

def main(args=None):
    rclpy.init(args=args)
    node = CameraPublisher()
    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        if node.show_window:
            cv2.destroyAllWindows()
        node.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()
