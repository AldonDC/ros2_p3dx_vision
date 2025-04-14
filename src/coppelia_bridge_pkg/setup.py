from setuptools import find_packages, setup

package_name = 'coppelia_bridge_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Si decides guardar también el launch aquí:
        #('share/' + package_name + '/launch', ['launch/coppelia_vision_launch.py']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    include_package_data=True,  # ✅ necesario para archivos como launch
    maintainer='alfonso',
    maintainer_email='A00838034@tec.mx',
    description='Nodo puente que transmite imágenes desde CoppeliaSim a ROS 2',
    license='MIT',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'image_streamer = coppelia_bridge_pkg.image_streamer:main',
        ],
    },
)
