from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import (BooleanField, PasswordField, SelectField, StringField,
                     SubmitField)
from wtforms.validators import DataRequired, Email
from fuca.models import Team


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class AdminNewsForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('Submit News')


class AdminTeamForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = FileField("Team Image", validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Submit Team')


class AdminPlayerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    number = StringField('Number', validators=[DataRequired()])
    email = StringField('Email', validators=[Email(), DataRequired()])

    birth_day = SelectField('Day',
                            choices=[(idx, val) for idx, val in enumerate(range(1, 32))],
                            validators=[DataRequired()])

    birth_month = SelectField('Month',
                            choices=[(idx, val) for idx, val in enumerate(range(1, 13))],
                            validators=[DataRequired()])

    birth_year = SelectField('Year',
                            choices=[(idx, val) for idx, val in enumerate(range(1920, 2020))],
                            validators=[DataRequired()])
    
    image = FileField("Image", validators=[FileAllowed(['jpg', 'jpeg', 'png'])])

    teams_db = Team.query.all()
    teams = [team.jinja_dict() for team in teams_db]
    team_choices = [(id, team['name']) for team in teams]
    team_dd = SelectField('Team', choices=team_choices, validators=[DataRequired()])
    
    submit = SubmitField('Submit Player')


class AdminMatchForm(FlaskForm):
    teams_db = Team.query.all()
    teams = [team.jinja_dict() for team in teams_db]
    team_choices = [(id, team['name']) for team in teams]

    host_team_dd = SelectField('Host Team', choices=team_choices, validators=[DataRequired()])
    guest_team_dd = SelectField('Guest Team', choices=team_choices, validators=[DataRequired()])
    date_time = StringField('Date-Time', validators=[DataRequired()])
    
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
