from flask import Flask 

from .config import DevelopmentConfig, TestingConfig, ProductionConfig, Config


def create_app(config_name="development"):
    from .extensions import db, migrate

    app = Flask(__name__)
    if config_name == "development":
        app.config.from_object(DevelopmentConfig)
    elif config_name == "testing":
        app.config.from_object(TestingConfig)
    elif config_name == "production":
        app.config.from_object(ProductionConfig)
    else:
        print("Unknown config, using base config")
        app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    print("create_app called with config_name", config_name)

    from .models import characters_bp

    app.register_blueprint(characters_bp)

    print("Effective DB URI:", app.config["SQLALCHEMY_DATABASE_URI"])

    return app