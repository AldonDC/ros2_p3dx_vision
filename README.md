# ros2_p3dx_vision

**ROS 2 + CoppeliaSim:** Seguimiento visual en tiempo real con VisionSensor y control de robot móvil Pioneer P3DX usando un controlador PID.

---

## 🎯 Objetivo

Implementar una arquitectura de control visual que permita al robot Pioneer P3DX seguir una esfera naranja en movimiento dentro de una simulación en CoppeliaSim, utilizando ROS 2 como middleware, visión por computadora con OpenCV y control PID.

---

## 🧠 Descripción General del Proyecto

Este proyecto fue desarrollado como parte de una actividad en el curso de Robótica Inteligente. Consiste en:

- Publicación de imágenes desde el VisionSensor del robot en CoppeliaSim.
- Procesamiento de imagen con OpenCV para detectar la esfera naranja.
- Controlador PID para ajustar el movimiento del robot basándose en el error visual.
- Movimiento de la esfera en trayectoria sinusoidal desde Python.
- Integración de todos los nodos con un archivo `launch`.

---

## 🧩 Arquitectura del Sistema



---

## 📦 Paquetes Utilizados

- **camera_streamer_pkg**: Nodo que publica las imágenes desde CoppeliaSim.
- **coppelia_bridge_pkg**: Conexión ZMQ con CoppeliaSim.
- **robot_controller_pkg**: Incluye el nodo de seguimiento visual, control PID y movimiento de la esfera.

---

## 📸 Nodo de la Cámara (`node_camera_publisher.py`)

Este nodo:

- Se conecta a CoppeliaSim mediante ZMQ.
- Obtiene las imágenes del VisionSensor del Pioneer P3DX.
- Convierte y publica las imágenes en el topic `/camera_image` (tipo `sensor_msgs/Image`).
- Muestra la imagen en tiempo real con OpenCV.
- Voltea la imagen verticalmente para corregir la orientación.

---

## 🧮 Nodo de Seguimiento Visual y PID (`node_visual_servoing_controller.py`)

Este nodo:

- Se suscribe al topic `/camera_image`.
- Convierte la imagen ROS a formato OpenCV.
- Detecta la esfera naranja usando filtrado HSV y contornos.
- Calcula el error horizontal respecto al centro de la imagen.
- Aplica un controlador PID y publica un mensaje `Twist` para mover el robot hacia la esfera.

---

## 🟠 Movimiento de la Esfera (`node_move_sphere.py`)

Este nodo:

- Se comunica vía ZMQ con CoppeliaSim.
- Mueve la esfera (verde o naranja) de forma lateral con una función seno.
- Proporciona una trayectoria dinámica para que el robot la siga de forma continua.

---

## 🚀 Ejecución de la Simulación

1. Asegúrate de tener CoppeliaSim corriendo con el robot PioneerP3DX, el VisionSensor y la esfera en la escena.
2. Fuentea tu workspace de ROS 2:

```bash
source install/setup.bash
