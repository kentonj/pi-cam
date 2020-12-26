
"""Continously record video and publish frames to redis."""
import time
import picamera
from .stream import STREAM


def record():
    """Continously record video."""
    print('warming up camera')
    with picamera.PiCamera() as camera:
        time.sleep(2)
        print('capturing frames and putting them in redis')
        for _ in camera.capture_continuous(STREAM, 'jpeg', use_video_port=True):
            pass


if __name__ == '__main__':
    record()
