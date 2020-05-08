from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from fuca.config import Config


db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
login_manager.login_message_category = 'info'


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)

    # register users blueprint
    from fuca.main.routes import main
    app.register_blueprint(main)

    # register users blueprint
    from fuca.users.routes import users
    app.register_blueprint(users)

    # register teams blueprint
    from fuca.teams.routes import teams
    app.register_blueprint(teams, url_prefix='/teams')

    # register standings blueprint
    from fuca.standings.routes import scores
    app.register_blueprint(scores, url_prefix='/standings')

    # register admin blueprint
    from fuca.admin.news.routes import news
    app.register_blueprint(news, url_prefix='/admin/news')

    # register admin blueprint
    from fuca.admin.teams.routes import adminteams
    app.register_blueprint(adminteams, url_prefix='/admin/teams')

    # register players blueprint
    from fuca.admin.players.routes import players
    app.register_blueprint(players, url_prefix='/admin/players')

    # register matches blueprint
    from fuca.admin.matches.routes import matches
    app.register_blueprint(matches, url_prefix='/admin/matches')

    # register results blueprint
    from fuca.admin.results.routes import results
    app.register_blueprint(results, url_prefix='/admin/results')

    # register statistics blueprint
    from fuca.admin.statistics.routes import statistics
    app.register_blueprint(statistics, url_prefix='/admin/statistics')

    # register statistics blueprint
    from fuca.admin.routes import adminhome
    app.register_blueprint(adminhome, url_prefix='/admin')

    db.init_app(app)
    bcrypt.init_app(app)
    login_manager.init_app(app)

    return app