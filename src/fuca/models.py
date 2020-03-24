from datetime import datetime
from fuca import db


class News(db.Model):
    __tablename__ = 'News'
    id          = db.Column(db.Integer,     primary_key=True)
    date        = db.Column(db.DateTime,    nullable=False, default=datetime.utcnow)
    title       = db.Column(db.String(100), nullable=False)
    content     = db.Column(db.Text,        nullable=False)

    def __repr__(self):
        return f"News('{self.title}', '{self.date}')"


class Player(db.Model):
    __tablename__ = 'Player'
    id          = db.Column(db.Integer,     primary_key=True)
    name        = db.Column(db.String(100), nullable=False)
    birthdate   = db.Column(db.DateTime,    nullable=False)
    image       = db.Column(db.String(20),  nullable=False, default='default.jpg')
    email       = db.Column(db.String(120), unique=True,    nullable=False)
    password    = db.Column(db.String(60),  nullable=False)
    # foreign keys
    team_id     = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    # relationships
    statistics  = db.relationship('Statistics', backref='player', lazy=True) 

    def __repr__(self):
        return f"Player('{self.name}', '{self.email}', '{self.image}')"


class Team(db.Model):
    __tablename__ = 'Team'
    id          = db.Column(db.Integer,     primary_key=True)
    name        = db.Column(db.String(100), nullable=False, unique=True)
    matches     = db.Column(db.Integer,     nullable=False, default=0)
    wins        = db.Column(db.Integer,     nullable=False, default=0)
    losses      = db.Column(db.Integer,     nullable=False, default=0)
    draws       = db.Column(db.Integer,     nullable=False, default=0)
    goal_diff   = db.Column(db.Integer,     nullable=False, default=0)
    logo_image  = db.Column(db.String(20),  nullable=False, default='default.jpg')
    # foreign keys
    captain_id  = db.Column(db.Integer, db.ForeignKey('player.id'))
    # relationships
    host_matches    = db.relationship('Match',  backref='host_team',    lazy=True,  foreign_keys='match.host_team')
    guest_matches   = db.relationship('Match',  backref='guest_team',   lazy=True,  foreign_keys='match.guest_team')
    players         = db.relationship('Player', backref='team',         lazy=True)

    def __repr__(self):
        return f"Team('{self.name}')"


class Match(db.Model):
    __tablename__ = 'Match'
    id          = db.Column(db.Integer, primary_key=True)
    # foreign keys
    host_team    = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    guest_team   = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    # relationships
    statistics  = db.relationship('Statistics', backref='match', lazy=True) 

    def __repr__(self):
        return f"Match(team1_id: {self.team1_id}, team2_id: {self.team2_id})"


class Statistics(db.Model):
    __tablename__ = 'Statistics'
    id          = db.Column(db.Integer, primary_key=True)
    goals       = db.Column(db.Integer, nullable=False)
    assists     = db.Column(db.Integer, nullable=False)
    experience  = db.Column(db.Integer, nullable=False)
    yellow      = db.Column(db.Integer, nullable=False)
    red         = db.Column(db.Integer, nullable=False)
    # foreign keys
    player_id   = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    match_id    = db.Column(db.Integer, db.ForeignKey('match.id'),  nullable=False)

    def __repr__(self):
        return f"Statistics(id = {self.id})"
