from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import (BooleanField, PasswordField, SelectField, StringField,
                     SubmitField)
from wtforms.validators import DataRequired, Email
from fuca.models import Team, Match, News, Player


class AdminAddResultForm(FlaskForm):
    match_dd = SelectField('Match', choices=[])

    host_team_goals = StringField('Host Team Goals', validators=[DataRequired()])
    host_team_yellow = StringField('Host Team Yellow', validators=[DataRequired()])
    host_team_red = StringField('Host Team Red', validators=[DataRequired()])
    host_team_shots = StringField('Host Team Shots', validators=[DataRequired()])

    guest_team_goals = StringField('Guest Team Goals', validators=[DataRequired()])
    guest_team_yellow = StringField('Guest Team Yellow', validators=[DataRequired()])
    guest_team_red = StringField('Guest Team Red', validators=[DataRequired()])
    guest_team_shots = StringField('Guest Team Shots', validators=[DataRequired()])

    best_player = StringField('Best Player', validators=[DataRequired()])

    submit = SubmitField('Submit Results')


class AdminUpdateResultForm(FlaskForm):
    match_dd = SelectField('Match', choices=[])

    host_team_goals = StringField('Host Team Goals', validators=[DataRequired()])
    host_team_yellow = StringField('Host Team Yellow', validators=[DataRequired()])
    host_team_red = StringField('Host Team Red', validators=[DataRequired()])
    host_team_shots = StringField('Host Team Shots', validators=[DataRequired()])

    guest_team_goals = StringField('Guest Team Goals', validators=[DataRequired()])
    guest_team_yellow = StringField('Guest Team Yellow', validators=[DataRequired()])
    guest_team_red = StringField('Guest Team Red', validators=[DataRequired()])
    guest_team_shots = StringField('Guest Team Shots', validators=[DataRequired()])

    best_player = StringField('Best Player', validators=[DataRequired()])

    submit = SubmitField('Submit Results')


class AdminDeleteResultForm(FlaskForm):
    match_dd = SelectField('Match', choices=[])

    host_team_goals = StringField('Host Team Goals', validators=[DataRequired()])
    host_team_yellow = StringField('Host Team Yellow', validators=[DataRequired()])
    host_team_red = StringField('Host Team Red', validators=[DataRequired()])
    host_team_shots = StringField('Host Team Shots', validators=[DataRequired()])

    guest_team_goals = StringField('Guest Team Goals', validators=[DataRequired()])
    guest_team_yellow = StringField('Guest Team Yellow', validators=[DataRequired()])
    guest_team_red = StringField('Guest Team Red', validators=[DataRequired()])
    guest_team_shots = StringField('Guest Team Shots', validators=[DataRequired()])

    best_player = StringField('Best Player', validators=[DataRequired()])

    submit = SubmitField('Submit Results')