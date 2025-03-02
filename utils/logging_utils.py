import logging

def setup_logging(app, config):
	logging.basicConfig(
		level=getattr(logging, config.LOG_LEVEL),
		format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
	)
	logger = logging.getLogger(__name__)
	logger.info(f"Logging configured with level: {config.LOG_LEVEL}")
	return logger