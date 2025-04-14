ros2\_p3dx\_vision

ROS 2 + CoppeliaSim: Seguimiento visual en tiempo real con VisionSensor y control de robot móvil Pioneer P3DX usando un controlador PID.

🎯 Objetivo

Implementar una arquitectura de control visual que permita al robot Pioneer P3DX seguir una esfera naranja en movimiento dentro de una simulación en CoppeliaSim, utilizando ROS 2 como middleware, visión por computadora con OpenCV y control PID.

🧠 Descripción General del Proyecto

Este proyecto fue desarrollado como parte de una actividad en el curso de Robótica Inteligente. Consiste en:

Publicación de imágenes desde el VisionSensor del robot en CoppeliaSim.

Procesamiento de imagen con OpenCV para detectar la esfera naranja.

Controlador PID para ajustar el movimiento del robot basándose en el error visual.

Movimiento de la esfera en trayectoria sinusoidal desde Python.

Integración de todos los nodos con un archivo launch.

🧩 Arquitectura del Sistema

CoppeliaSim (Pioneer P3DX + VisionSensor)

│

▼

node\_camera\_publisher → Publica imágenes ROS 2

│

▼

node\_visual\_servoing\_controller → Procesa imagen y genera comandos Twist

│

▼

node\_robot\_controller → Controla el robot vía /cmd\_vel

▲

│

node\_move\_sphere → Mueve la esfera con trayectoria senoidal

📦 Paquetes Utilizados

camera\_streamer\_pkg: Nodo que publica las imágenes desde CoppeliaSim.

coppelia\_bridge\_pkg: Conexión ZMQ con CoppeliaSim.

robot\_controller\_pkg: Incluye el nodo de seguimiento visual, control PID y movimiento de la esfera.

📸 Nodo de la Cámara (node\_camera\_publisher.py)

Este nodo:

Se conecta a CoppeliaSim mediante ZMQ.

Obtiene las imágenes del VisionSensor del Pioneer P3DX.

Convierte y publica las imágenes en el topic /camera\_image (tipo sensor\_msgs/Image).

Muestra la imagen en tiempo real con OpenCV.

Voltea la imagen verticalmente para corregir la orientación.

🧮 Nodo de Seguimiento Visual y PID (node\_visual\_servoing\_controller.py)

Este nodo:

Se suscribe al topic /camera\_image.

Convierte la imagen ROS a formato OpenCV.

Detecta la esfera naranja usando filtrado HSV y contornos.

Calcula el error horizontal respecto al centro de la imagen.

Aplica un controlador PID y publica un mensaje Twist para mover el robot hacia la esfera.

🟠 Movimiento de la Esfera (node\_move\_sphere.py)

Este nodo:

Se comunica vía ZMQ con CoppeliaSim.

Mueve la esfera (verde o naranja) de forma lateral con una función seno.

Proporciona una trayectoria dinámica para que el robot la siga de forma continua.

🚀 Ejecución de la Simulación

Asegúrate de tener CoppeliaSim corriendo con el robot PioneerP3DX, el VisionSensor y la esfera en la escena.

Fuentea tu workspace de ROS 2:

source install/setup.bash

Ejecuta el archivo launch.py que integra todos los nodos:

ros2 launch camera\_streamer\_pkg coppelia\_vision\_launch.py

🎥 Demostración

📹 Video demostrativo del proyecto

👉 Ver en YouTube: (Reemplaza este enlace con tu video real)

👤 Autor

Alfonso Solís Díaz

Estudiante de Ingeniería en Robótica y Sistemas Digitales

Tecnológico de Monterrey – Campus Monterrey

Abril 2025

