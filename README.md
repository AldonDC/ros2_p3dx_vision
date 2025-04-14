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

