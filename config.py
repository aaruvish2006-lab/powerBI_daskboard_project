import os
from dotenv import load_dotenv

# Load variables from a .env file if it exists
load_dotenv()

class Config:
    """Base configuration."""
    # General
    APP_NAME = os.getenv("APP_NAME", "MyAwesomeApp")
    DEBUG = False
    TESTING = False
    
    # Security
    # Always use a fallback for local dev, but require an env var for production
    SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-key-12345")
    
    # Database
    DB_USER = os.getenv("DB_USER", "admin")
    DB_PASSWORD = os.getenv("DB_PASSWORD", "")
    DB_HOST = os.getenv("DB_HOST", "localhost")
    DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/myapp_db"

class DevelopmentConfig(Config):
    DEBUG = True
    DATABASE_URL = "sqlite:///dev_db.sqlite3"

class ProductionConfig(Config):
    # Overwrite defaults for production
    DEBUG = False
    # In production, we might want to strictly require the DATABASE_URL
    DATABASE_URL = os.getenv("DATABASE_URL")

# Dictionary to easily switch between environments
config_by_name = {
    "dev": DevelopmentConfig,
    "prod": ProductionConfig
}
