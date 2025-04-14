import cv2
import numpy as np
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

client = RemoteAPIClient()
sim = client.getObject('sim')
sensor = sim.getObject('/visionSensor')

cv2.namedWindow("Cámara desde CoppeliaSim", cv2.WINDOW_NORMAL)

try:
    while True:
        img, resX, resY = sim.getVisionSensorCharImage(sensor)
        img = np.frombuffer(img, dtype=np.uint8).reshape(resY, resX, 3)
        img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
        img = cv2.flip(img, 0)  # Corrige orientación

        cv2.imshow("Cámara desde CoppeliaSim", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except KeyboardInterrupt:
    print("Interrumpido por teclado")

cv2.destroyAllWindows()
