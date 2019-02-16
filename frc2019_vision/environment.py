from cv2 import VideoCapture, rotate, ROTATE_90_CLOCKWISE

from . import FrameQueue, OverwritingLifoQueue, Target


TARGET: OverwritingLifoQueue = OverwritingLifoQueue(2)
# Set default value of Target
TARGET.put(Target.NONE)

GUI: bool = False
CAMERA_PORT: int = 0
VideoCapture = VideoCapture(CAMERA_PORT)
VIDEO_STREAM = VideoCapture = rotate(VideoCapture, rotateCode=ROTATE_90_CLOCKWISE)

NETIFACE: str = "eth0"

# Que for vision to driverstation
DRIVERSTATION_FRAMES: FrameQueue = FrameQueue(2)

# Vision Information
DISTANCE_FROM_OBJECT: OverwritingLifoQueue = OverwritingLifoQueue(2)
ANGLE_FROM_CENTER: OverwritingLifoQueue = OverwritingLifoQueue(2)
