from flask import Flask
from flask_cors import CORS
from utils.logging_utils import setup_logging
from routes.location_routes import location_bp
from routes.health_routes import health_bp
from config import config

def create_app():
  app = Flask(__name__)
  
  # Apply configuration
  app.config.from_object(config)
  
  # Setup CORS
  CORS(app)
  
  # Setup logging
  logger = setup_logging(app, config)
  
  # Register blueprints
  app.register_blueprint(location_bp)
  app.register_blueprint(health_bp)
  
  # Attach config and logger to blueprints
  location_bp.config = config
  location_bp.logger = logger
  
  return app