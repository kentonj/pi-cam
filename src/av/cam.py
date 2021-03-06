"""Camera module."""
import time
from .stream import STREAM


class Camera(object):
    """Camera class for getting frames (as a generator) off the redis stream."""
    def __init__(self):
        pass

    def convert_frame(self, frame):
        """Convert the jpeg bytes to a usable frame for the browser to decode."""
        return (b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
    
    def get_frames(self):
        """Read frames off of the stream, starting with our current timestamp."""
        starting_key = f"{int((time.time()) * 1000)}-0"
        while True:
            response = STREAM.r.xread({STREAM.stream_name: starting_key})
            if response:
                messages = response[0][1]
                for identifier, payload in messages:
                    frame = payload[b'1']
                    yield self.convert_frame(frame)
                    # once we run out of frames, set the starting frame to now so that we always stay as up to date as possible with frames
                    starting_key = f"{int((time.time()) * 1000)}-0"
