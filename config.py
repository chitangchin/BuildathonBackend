import os
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from .env


# Debug: print the specific variable and all environment variables
print("CLAUDE_API_URL:", os.getenv("CLAUDE_API_URL"))
print("All environment variables:")
for key, value in os.environ.items():
    if "CLAUDE" in key or "ELEVENLABS" in key or key == "FLASK_ENV":
        print(key, "=", value)

class Config:
    DEBUG = False
    LOG_LEVEL = "INFO"
    CLAUDE_API_KEY = os.getenv("CLAUDE_API_KEY")
    CLAUDE_API_URL = os.getenv("CLAUDE_API_URL")
    CLAUDE_MODEL = os.getenv("CLAUDE_MODEL")
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY")
    ELEVENLABS_API_URL = os.getenv("ELEVENLABS_API_URL")
    ELEVENLABS_VOICE_ID = os.getenv("ELEVENLABS_VOICE_ID")

class DevelopmentConfig(Config):
    DEBUG = True
    LOG_LEVEL = "DEBUG"

class ProductionConfig(Config):
    pass

# Select config based on FLASK_ENV environment variable
config = DevelopmentConfig() if os.environ.get("FLASK_ENV") == "development" else ProductionConfig()
