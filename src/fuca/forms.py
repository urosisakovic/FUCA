from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class AdminNewsForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    submit = SubmitField('Submit News')


class AdminTeamForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = StringField('Image', validators=[DataRequired()])
    submit = SubmitField('Submit Team')


class AdminPlayerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    number = StringField('Number', validators=[DataRequired()])
    team = StringField('Team', validators=[DataRequired()])
    birthdate = StringField('Birthdate', validators=[DataRequired()])
    image = StringField('Image', validators=[DataRequired()])
    email = StringField('Email', validators=[Email(), DataRequired()])
    submit = SubmitField('Submit Player')


class AdminMatchForm(FlaskForm):
    date_time = StringField('Date-Time', validators=[DataRequired()])
    host_team = StringField('Host Team', validators=[DataRequired()])
    guest_team = StringField('Guest Team', validators=[DataRequired()])
    submit = SubmitField('Submit Match')


class AdminResultForm(FlaskForm):
    match = StringField('Match', validators=[DataRequired()])

    host_team_goals = StringField('Host Team Goals', validators=[DataRequired()])
    host_team_yellow = StringField('Host Team Yellow', validators=[DataRequired()])
    host_team_red = StringField('Host Team Red', validators=[DataRequired()])
    host_team_shots = StringField('Host Team Shots', validators=[DataRequired()])
    host_team_possession = StringField('Host Team Possession', validators=[DataRequired()])

    guest_team_goals = StringField('Guest Team Goals', validators=[DataRequired()])
    guest_team_yellow = StringField('Guest Team Yellow', validators=[DataRequired()])
    guest_team_red = StringField('Guest Team Red', validators=[DataRequired()])
    guest_team_shots = StringField('Guest Team Shots', validators=[DataRequired()])
    guest_team_possession = StringField('Guest Team Possession', validators=[DataRequired()])

    best_player = StringField('Best Player', validators=[DataRequired()])

    submit = SubmitField('Submit Results')


class AdminStatsForm(FlaskForm):
    match = StringField('Match', validators=[DataRequired()])
    player = StringField('Player', validators=[DataRequired()])
    goals = StringField('Goals', validators=[DataRequired()])
    assists = StringField('Assists', validators=[DataRequired()])
    red = StringField('Red', validators=[DataRequired()])
    yellow = StringField('Yellow', validators=[DataRequired()])
    submit = SubmitField('Submit Statistics')
    