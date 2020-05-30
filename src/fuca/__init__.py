"""
Author: Djodje Vucinic
"""
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from fuca.config import Config
from flask_mail import Mail


db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__)
    # import all the configurations
    app.config.from_object(Config)

    # import blueprints
    from fuca.main.routes import main
    from fuca.users.routes import users
    from fuca.teams.routes import teams
    from fuca.standings.routes import scores
    from fuca.admin.news.routes import news
    from fuca.admin.teams.routes import adminteams
    from fuca.admin.players.routes import players
    from fuca.admin.matches.routes import matches
    from fuca.admin.results.routes import results
    from fuca.admin.statistics.routes import statistics
    from fuca.admin.routes import adminhome
    from fuca.errors.handlers import errors

    # register blueprints
    app.register_blueprint(main)    
    app.register_blueprint(users)    
    app.register_blueprint(teams,       url_prefix='/teams')
    app.register_blueprint(scores,      url_prefix='/standings')
    app.register_blueprint(adminhome,   url_prefix='/admin')
    app.register_blueprint(news,        url_prefix='/admin/news')
    app.register_blueprint(adminteams,  url_prefix='/admin/teams')
    app.register_blueprint(players,     url_prefix='/admin/players')
    app.register_blueprint(matches,     url_prefix='/admin/matches')
    app.register_blueprint(results,     url_prefix='/admin/results')
    app.register_blueprint(statistics,  url_prefix='/admin/statistics')
    app.register_blueprint(errors)

    # initiate flask extensions
    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)
    mail.init_app(app)

    return app