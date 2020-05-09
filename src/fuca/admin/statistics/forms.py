from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired
from fuca.models import Match, Player


class AdminAddStatisticsForm(FlaskForm):
    match_dd = SelectField('Match', choices=[])
    player_dd = SelectField('Player', choices=[])

    match = StringField('Match', validators=[DataRequired()])
    player = StringField('Player', validators=[DataRequired()])
    goals = StringField('Goals', validators=[DataRequired()])
    assists = StringField('Assists', validators=[DataRequired()])
    red = StringField('Red', validators=[DataRequired()])
    yellow = StringField('Yellow', validators=[DataRequired()])
    submit = SubmitField('Add Statistics')

    def populate_dd(self):
        matches = Match.query.all()
        match_choices = [(match.id, match.host_team.name + ' vs ' + match.guest_team.name) for match in matches]
        self.match_dd.choices = match_choices

        players = Player.query.filter_by(is_admin=False).all()
        player_choices = [(player.team_id, player.name) for player in players]
        self.player_dd.choices = player_choices


class AdminUpdateStatisticsForm(FlaskForm):
    match_dd = SelectField('Match', choices=[])
    player_dd = SelectField('Player', choices=[])

    goals = StringField('Goals', validators=[DataRequired()])
    assists = StringField('Assists', validators=[DataRequired()])
    red = StringField('Red', validators=[DataRequired()])
    yellow = StringField('Yellow', validators=[DataRequired()])
    submit = SubmitField('Update Statistics')

    def populate_dd(self):
        matches = Match.query.all()
        match_choices = [(match.id, match.host_team.name + ' vs ' + match.guest_team.name) for match in matches]
        self.match_dd.choices = match_choices

        players = Player.query.filter_by(is_admin=False).all()
        player_choices = [(player.team_id, player.name) for player in players]
        self.player_dd.choices = player_choices


class AdminDeleteStatisticsForm(FlaskForm):
    match_dd = SelectField('Match', choices=[])
    player_dd = SelectField('Player', choices=[])
    submit = SubmitField('Delete Statistics')

    def populate_dd(self):
        matches = Match.query.all()
        match_choices = [(match.id, match.host_team.name + ' vs ' + match.guest_team.name) for match in matches]
        self.match_dd.choices = match_choices

        players = Player.query.filter_by(is_admin=False).all()
        player_choices = [(player.team_id, player.name) for player in players]
        self.player_dd.choices = player_choices