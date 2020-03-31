from datetime import datetime
from fuca import db


class News(db.Model):
    __tablename__ = 'news'
    id          = db.Column(db.Integer,     primary_key=True)
    date        = db.Column(db.DateTime,    nullable=False, default=datetime.utcnow)
    title       = db.Column(db.String(100), nullable=False)
    content     = db.Column(db.Text,        nullable=False)

    def __repr__(self):
        return f"News('{self.title}', '{self.date}')"

    def jinja_dict(self):
        return {'news_title'    : self.title,
                'content'       : self.content,
                'date'          : str(self.date)}



class Player(db.Model):
    __tablename__ = 'player'
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


class Match(db.Model):
    __tablename__ = 'match'
    id          = db.Column(db.Integer, primary_key=True)
    date_time        = db.Column(db.DateTime)
    
    host_team_goals         = db.Column(db.Integer, default=0)
    host_team_yellow        = db.Column(db.Integer, default=0)
    host_team_red           = db.Column(db.Integer, default=0)
    host_team_shots         = db.Column(db.Integer, default=0)
    host_team_possession    = db.Column(db.Integer, default=0)

    guest_team_goals        = db.Column(db.Integer, default=0)
    guest_team_yellow       = db.Column(db.Integer, default=0)
    guest_team_red          = db.Column(db.Integer, default=0)
    guestt_team_shots         = db.Column(db.Integer, default=0)
    guest_team_possession   = db.Column(db.Integer, default=0)

    # foreign keys
    host_team_id     = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    guest_team_id    = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    best_player_id   = db.Column(db.Integer, db.ForeignKey('player.id'))
    # relationships
    statistics  = db.relationship('Statistics', backref='match', lazy=True) 

    def __repr__(self):
        return f"Match(host team id: {self.host_team}, guest team id: {self.guest_team})"

    def jinja_dict(self):
        return {'date':         self.date_time,
                'team1_name'    : self.host_team.name,
                'team1_goals'   : self.host_team_goals,
                'team1_logo'    : self.team1_logo,
                'team2_name'    : self.guest_team.name,
                'team2_goals':  self.guest_team_goals}


class Team(db.Model):
    __tablename__ = 'team'
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
    host_matches    = db.relationship('Match',  backref='host_team',    lazy=True,  foreign_keys=Match.host_team_id)
    guest_matches   = db.relationship('Match',  backref='guest_team',   lazy=True,  foreign_keys=Match.guest_team_id)
    players         = db.relationship('Player', backref='team',         lazy=True,  foreign_keys=Player.team_id)

    def __repr__(self):
        return f"Team('{self.name}')"


class Statistics(db.Model):
    __tablename__ = 'statistics'
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
