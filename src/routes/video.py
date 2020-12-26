from flask import jsonify, Blueprint, Response, current_app as app, stream_with_context
from src.av.cam import Camera
import time


bp = Blueprint('video', __name__)

cam = Camera()

@bp.route('/feed')
def video_feed():
    """Start a video feed and return it to the browser."""
    app.logger.info(f'starting video feed')
    return Response(cam.get_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')
