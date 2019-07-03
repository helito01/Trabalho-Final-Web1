from flask import Flask, render_template
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy

from config import Config
from flask_login import LoginManager

bootstrap = Bootstrap()
db = SQLAlchemy()
config = Config()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)
    config.init_app(app)
     
    app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

    
    from .models import User, Role
    admin = Admin(app, name='microblog', template_mode='bootstrap3')
    admin.add_view(ModelView(User, db.session))
    admin.add_view(ModelView(Role, db.session)) 
    app.run()

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)


    return app
