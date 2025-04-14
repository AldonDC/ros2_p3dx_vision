import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/home/alfonso/coppelia_vision_act13_ws/install/camera_streamer_pkg'
