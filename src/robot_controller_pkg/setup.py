from setuptools import find_packages, setup

package_name = 'robot_controller_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    include_package_data=True,
    maintainer='alfonso',
    maintainer_email='A00838034@tec.mx',
    description='Nodo controlador que envía comandos de movimiento desde ROS 2 a CoppeliaSim',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'node_robot_controller = robot_controller_pkg.node_robot_controller:main',
            'node_trajectory_controller = robot_controller_pkg.node_trajectory_controller:main',
            'node_visual_servoing_controller = robot_controller_pkg.node_visual_servoing_controller:main',
            'node_move_sphere = robot_controller_pkg.node_move_sphere:main',
            # Descomenta si los usas:
            # 'circle_controller = robot_controller_pkg.circle_controller:main',
            # 'node_circle_controller = robot_controller_pkg.node_circle_controller:main',
        ],
    },
)
