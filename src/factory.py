"""Application factory, can be called by flask or gunicorn."""
from flask import Flask, jsonify, Response
import logging


def create_app():
    """Create the app."""
    app = Flask(__name__)
    logger = logging.getLogger()
    logger.setLevel(logging.INFO)
    from src.routes.default import bp as default_bp
    app.register_blueprint(default_bp, url_prefix='/')
    from src.routes.video import bp as video_bp
    app.register_blueprint(video_bp, url_prefix='/video')
    return app
