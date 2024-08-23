from flask import Flask, session
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate

db = SQLAlchemy()
bcrypt = Bcrypt()



def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'your_secret_key_here'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./site.db'



    db.init_app(app)
    migrate=Migrate(app, db)
    bcrypt.init_app(app)

    from flaskblog.auth.routes import auth
    from flaskblog.blog.routes import blog
    from flaskblog.routes import main
    app.register_blueprint(auth)
    app.register_blueprint(blog)
    app.register_blueprint(main)

    return app
