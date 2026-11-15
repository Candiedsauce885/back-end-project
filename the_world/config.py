import os
from dotenv import load_dotenv

load_dotenv()

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
INSTANCE_DIR = os.path.join(BASE_DIR, "..", "instance")

class Config:
    DEBUG = False
    DATABASE_URL = os.getenv("DATABASE_URL")
    if DATABASE_URL:
        SQLALCHEMY_DATABASE_URI = DATABASE_URL
    else:
        dev_db_path = os.path.join(INSTANCE_DIR, "dev.db")
        SQLALCHEMY_DATABASE_URI = "sqlite://" + dev_db_path
    INTERNAL_TOKEN = os.getenv("INTERNAL_SERVICE_TOKEN")
    jwt_secret =  os.getenv("JWT_SECRET")
    if jwt_secret is None:
        raise RuntimeError("JWT_SECRET is required but not set. Define it in .env or the enviorment")
    JWT_SECRET = jwt_secret
    CACHE_TYPE = "SimpleCache"
    CACHE_DEFAULT_TIMEOUT = 30
class DevelopmentConfig(Config):
    DEBUG = True



class TestingConfig(Config):
    DEBUG = False



class ProductionConfig(Config):
    DEBUG = False
