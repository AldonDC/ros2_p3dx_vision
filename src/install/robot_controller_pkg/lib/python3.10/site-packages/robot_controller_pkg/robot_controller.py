import time
from coppeliasim_zmqremoteapi_client import RemoteAPIClient

client = RemoteAPIClient()
sim = client.getObject('sim')

left_motor = sim.getObject('/PioneerP3DX/leftMotor')
right_motor = sim.getObject('/PioneerP3DX/rightMotor')

print("✅ Motores conectados")

v_l = 2.0  # Velocidad izquierda
v_r = 2.0  # Velocidad derecha
sim.setJointTargetVelocity(left_motor, v_l)
sim.setJointTargetVelocity(right_motor, v_r)

print("Robot en movimiento...")
time.sleep(3)

# Detener
sim.setJointTargetVelocity(left_motor, 0)
sim.setJointTargetVelocity(right_motor, 0)
print("Robot detenido")
