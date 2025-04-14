# ros2_p3dx_vision

![Build](https://img.shields.io/badge/build-passing-brightgreen)
![Python](https://img.shields.io/badge/python-3.10-blue)
![License](https://img.shields.io/badge/license-MIT-blue)


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

```plaintext
CoppeliaSim (Pioneer P3DX + VisionSensor)
        │
        ▼
node_camera_publisher         → Publica imágenes ROS 2
        │
        ▼
node_visual_servoing_controller → Procesa imagen y genera comandos Twist
        │
        ▼
node_robot_controller         → Controla el robot vía /cmd_vel
        ▲
        │
node_move_sphere              → Mueve la esfera con trayectoria senoidal
```

---

## 📦 Paquetes Utilizados

- `camera_streamer_pkg`: Nodo que publica las imágenes desde CoppeliaSim.
- `coppelia_bridge_pkg`: Conexión ZMQ con CoppeliaSim.
- `robot_controller_pkg`: Incluye el nodo de seguimiento visual, control PID y movimiento de la esfera.

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
```

3. Ejecuta el archivo `launch.py` que integra todos los nodos:

```bash
ros2 launch camera_streamer_pkg coppelia_vision_launch.py
```

---


## 🖼️ Imágenes de la Simulación

A continuación, se presentan algunas capturas de pantalla y una animación de la simulación en **CoppeliaSim**, donde el robot Pioneer P3DX realiza el seguimiento visual de una esfera naranja:

---

### 🧠 Escena en CoppeliaSim

<div align="center">
  <img src="https://github.com/user-attachments/assets/94c3249f-bedc-45de-b752-affae1a7dac9" alt="Escena CoppeliaSim" width="600"/>
</div>

---

### 🤖 Robot siguiendo la esfera

<div align="center">
  <img src="https://github.com/user-attachments/assets/eebf6069-c7fc-4336-9625-810bbf1de507" alt="Seguimiento visual 1" width="600"/>
  <br/><br/>
  <img src="https://github.com/user-attachments/assets/31c35db2-9ce9-4c06-8c0b-b8b4f2d7076f" alt="Seguimiento visual 2" width="600"/>
</div>

---

### 🎞️ Animación de la Simulación

<div align="center">
  <a href="https://www.youtube.com/watch?v=LFesywvOHP8" target="_blank">
    <img src="https://img.youtube.com/vi/LFesywvOHP8/hqdefault.jpg" alt="Simulación Visual Pioneer P3DX - YouTube" width="600"/>
  </a>
</div>

<p align="center"><i>Haz clic en la imagen para ver el video completo en YouTube.</i></p>

> 📽️ *La animación muestra cómo el robot Pioneer P3DX sigue en tiempo real una esfera naranja que se mueve en trayectoria senoidal, utilizando visión artificial y un controlador PID dentro de un entorno de simulación con CoppeliaSim.*


## 👤 Autor

**Alfonso Solís Díaz**  
Estudiante de Ingeniería en Robótica y Sistemas Digitales  
Tecnológico de Monterrey – Campus Monterrey  
_Abril 2025_
