"""
Author: Igor Andrejic
"""
from datetime import datetime
from fuca import db, login_manager
from flask_login import UserMixin
from flask import current_app
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer


@login_manager.user_loader
def load_user(player_id):
    return Player.query.get(int(player_id))


class News(db.Model):
    """
    Class which represent NEWS table in database.
    """
    __tablename__ = 'news'
    id          = db.Column(db.Integer,     primary_key=True)
    date        = db.Column(db.DateTime,    nullable=False, default=datetime.utcnow)
    title       = db.Column(db.String(100), nullable=False)
    content     = db.Column(db.Text,        nullable=False)

    def __repr__(self):
        return f"News('{self.title}', '{self.date}')"


class Player(db.Model, UserMixin):
    """
    Class which represent PLAYER table in database.
    """
    __tablename__ = 'player'
    id          = db.Column(db.Integer,     primary_key=True)
    name        = db.Column(db.String(100), nullable=False)
    birthdate   = db.Column(db.DateTime,    nullable=False)
    number      = db.Column(db.Integer,     nullable=False)
    image       = db.Column(db.String(20),  nullable=False, default='default.jpg')
    email       = db.Column(db.String(120), unique=True,    nullable=False)
    password    = db.Column(db.String(200))
    registered  = db.Column(db.Boolean, default=False)
    is_admin    = db.Column(db.Boolean, default=False)
    # foreign keys
    team_id     = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    # relationships
    statistics  = db.relationship('Statistics', backref='player', lazy=True) 

    def get_reset_token(self, expires_sec=600):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'player_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            player_id = s.loads(token)['player_id']
        except:
            None
        return Player.query.get(player_id)


    @property
    def goals(self):
        goals = 0
        for stat in self.statistics:
            goals += stat.goals
        return goals

    @property
    def assists(self):
        assists = 0
        for stat in self.statistics:
            assists += stat.assists
        return assists

    @property
    def red(self):
        red = 0
        for stat in self.statistics:
            red += stat.red
        return red

    @property
    def yellow(self):
        yellow = 0
        for stat in self.statistics:
            yellow += stat.yellow
        return yellow

    @property
    def points(self):
        return self.goals + self.assists - self.yellow - 2 * self.red

    def __repr__(self):
        return f"Player('{self.name}', '{self.email}', '{self.image}')"


class Match(db.Model):
    """
    Class which represent MATCH table in database.
    """
    __tablename__ = 'match'
    id                      = db.Column(db.Integer, primary_key=True)
    date_time               = db.Column(db.DateTime, nullable=False)
    
    host_team_goals         = db.Column(db.Integer, default=0)
    host_team_yellow        = db.Column(db.Integer, default=0)
    host_team_red           = db.Column(db.Integer, default=0)
    host_team_shots         = db.Column(db.Integer, default=0)

    guest_team_goals        = db.Column(db.Integer, default=0)
    guest_team_yellow       = db.Column(db.Integer, default=0)
    guest_team_red          = db.Column(db.Integer, default=0)
    guest_team_shots        = db.Column(db.Integer, default=0)

    # foreign keys
    host_team_id     = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    guest_team_id    = db.Column(db.Integer, db.ForeignKey('team.id'), nullable=False)
    # relationships
    statistics  = db.relationship('Statistics', backref='match', lazy=True)

    @property
    def host_team_playing(self):
        cnt = 0

        players = Player.query.filter_by(team_id=self.host_team_id).all()
        for player in players:
            playing = PlayingMatch.query.filter_by(player_id=player.id).filter_by(match_id=self.id).first()
            if playing and playing.playing:
                cnt += 1

        return cnt

    @property
    def host_team_not_playing(self):
        cnt = 0

        players = Player.query.filter_by(team_id=self.host_team_id).all()
        for player in players:
            playing = PlayingMatch.query.filter_by(player_id=player.id).filter_by(match_id=self.id).first()
            if playing and not playing.playing:
                cnt += 1

        return cnt

    @property
    def host_team_pending(self):
        cnt = 0

        players = Player.query.filter_by(team_id=self.host_team_id).all()
        for player in players:
            playing = PlayingMatch.query.filter_by(player_id=player.id).filter_by(match_id=self.id).first()
            if not playing:
                cnt += 1

        return cnt

    @property
    def guest_team_playing(self):
        cnt = 0

        players = Player.query.filter_by(team_id=self.host_team_id).all()
        for player in players:
            playing = PlayingMatch.query.filter_by(player_id=player.id).filter_by(match_id=self.id).first()
            if playing and playing.playing:
                cnt += 1

        return cnt

    @property
    def guest_team_not_playing(self):
        cnt = 0

        players = Player.query.filter_by(team_id=self.host_team_id).all()
        for player in players:
            playing = PlayingMatch.query.filter_by(player_id=player.id).filter_by(match_id=self.id).first()
            if playing and not playing.playing:
                cnt += 1

        return cnt

    @property
    def guest_team_pending(self):
        cnt = 0

        players = Player.query.filter_by(team_id=self.host_team_id).all()
        for player in players:
            playing = PlayingMatch.query.filter_by(player_id=player.id).filter_by(match_id=self.id).first()
            if not playing:
                cnt += 1

        return cnt

    def __repr__(self):
        return f"Match(host team id: {self.host_team_id}, guest team id: {self.guest_team_id})"
                

class Team(db.Model):
    """
    Class which represent TEAM table in database.
    """
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

    @property
    def points(self):
        return self.wins*3 + self.draws*1
            
    @property
    def players_count(self):
        return len(self.players)

    def __repr__(self):
        return f"Team('{self.id}, {self.name}')"


class Statistics(db.Model):
    """
    Class which represent STATISTICS table in database.
    """
    __tablename__ = 'statistics'
    id          = db.Column(db.Integer, primary_key=True)
    goals       = db.Column(db.Integer, nullable=False)
    assists     = db.Column(db.Integer, nullable=False)
    yellow      = db.Column(db.Integer, nullable=False)
    red         = db.Column(db.Integer, nullable=False)
    # foreign keys
    player_id   = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    match_id    = db.Column(db.Integer, db.ForeignKey('match.id'),  nullable=False)

    def __repr__(self):
        return f"Statistics(id = {self.id})"


class PlayingMatch(db.Model):
    """
    Class which represent MATCH table in database.
    """
    __tablename__ = 'playingMatch'
    id          = db.Column(db.Integer, primary_key=True)
    playing     = db.Column(db.Boolean, nullable=False)
    # foreign keys
    player_id   = db.Column(db.Integer, db.ForeignKey('player.id'), nullable=False)
    match_id    = db.Column(db.Integer, db.ForeignKey('player.id'),nullable=False)
