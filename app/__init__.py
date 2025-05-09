# import os
# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy
# from flask_migrate import Migrate
# from dotenv import load_dotenv

# load_dotenv()

# db = SQLAlchemy()
# migrate = Migrate()

# def create_app():
#     # app = Flask(__name__)
#     app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))

#     app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
#     app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
#     app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#     db.init_app(app)
#     migrate.init_app(app, db)

#     from app.routes import student, admin
#     app.register_blueprint(student.bp)
#     app.register_blueprint(admin.bp)

#     return app

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv

load_dotenv()

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    # app = Flask(__name__)
    app = Flask(__name__, static_folder=os.path.join(os.path.dirname(__file__), 'static'))

    # Configure the app
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL')
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Ensure the upload folder exists
    UPLOAD_FOLDER = 'uploads'
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # Create folder if it doesn't exist
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # Optionally set the upload folder in the config

    # Initialize db and migrate
    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints
    from app.routes import student, admin
    app.register_blueprint(student.bp)
    app.register_blueprint(admin.bp)

    return app
