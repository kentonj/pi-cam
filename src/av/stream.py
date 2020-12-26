"""Redis stream object that picamera can write to."""
import redis
import time
import os


class RedisStream(object):
    """Write-able object that publishes a frame to the redis stream, keeping (push/pop) max_frame_buffer frames in the buffer."""

    def __init__(self, r, stream_name, max_frame_buffer=300):
        self.r = r
        self.stream_name = stream_name
        # maximum number of frames to keep on the buffer at any one time
        self.max_frame_buffer = max_frame_buffer
    
    def write(self, frame):
        """Write a new frame to the redis stream, timestamped with the current unix milliseconds."""
        ts = int(time.time() * 1000)
        msg_id = f"{ts}-0"
        self.r.xadd(
            self.stream_name,
            {1: frame},
            id=msg_id,
            maxlen=self.max_frame_buffer
        )


STREAM = RedisStream(
    redis.Redis(host=os.environ['REDIS_HOST'], port=os.environ['REDIS_PORT'], db=0),
    stream_name='video',
    max_frame_buffer=1000
)
