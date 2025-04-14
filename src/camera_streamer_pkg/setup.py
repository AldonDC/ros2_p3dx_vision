from setuptools import find_packages, setup

package_name = 'camera_streamer_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/coppelia_vision_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    include_package_data=True,  # ✅ Esto permite incluir archivos como launch
    maintainer='alfonso',
    maintainer_email='A00838034@tec.mx',
    description='Nodo que publica imágenes desde CoppeliaSim en ROS 2',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'node_camera_publisher = camera_streamer_pkg.node_camera_publisher:main',
        ],
    },
)
