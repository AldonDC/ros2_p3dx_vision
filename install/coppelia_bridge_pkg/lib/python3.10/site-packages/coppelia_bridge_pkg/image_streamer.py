import cv2
import numpy as np
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

# Conectar con CoppeliaSim
client = RemoteAPIClient()
sim = client.getObject('sim')
sensor = sim.getObject('/PioneerP3DX/visionSensor')  # Asegúrate que el path es correcto

# Crear ventana OpenCV
cv2.namedWindow("📷 Vista del VisionSensor", cv2.WINDOW_NORMAL)

try:
    while True:
        # Usar API moderna
        img_data, resolution = sim.getVisionSensorImg(sensor)
        resX, resY = resolution

        # Convertir buffer a imagen
        img = np.frombuffer(img_data, dtype=np.uint8).reshape((resY, resX, 3))
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        img = cv2.flip(img, 180)  # Corregir orientación vertical

        # Mostrar imagen
        cv2.imshow("📷 Vista del VisionSensor", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("🛑 Interrumpido por teclado")

cv2.destroyAllWindows()
    