from flask import redirect, url_for, Blueprint

bp = Blueprint('default', __name__)

@bp.route('')
def default():
    """Home redirect should take you to the video.video_feed handler."""
    return redirect(url_for('video.video_feed'))
