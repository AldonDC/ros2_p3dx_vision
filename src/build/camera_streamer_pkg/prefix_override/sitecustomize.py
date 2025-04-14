import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/alfonso/coppelia_vision_control_ws/src/install/camera_streamer_pkg'
