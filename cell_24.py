import sys
# 1. Uninstall all possible versions of OpenCV that are conflicting
!{sys.executable} -m pip uninstall opencv-python opencv-contrib-python opencv-python-headless opencv-contrib-python-headless -y

# 2. Install ONLY the complete extended package
!{sys.executable} -m pip install --no-cache-dir opencv-contrib-python
