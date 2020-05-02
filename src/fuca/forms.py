from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import (BooleanField, PasswordField, SelectField, StringField,
                     SubmitField)
from wtforms.validators import DataRequired, Email
from fuca.models import Team, Match, News


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class AdminAddNewsForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('Add News')


class AdminUpdateNewsForm(FlaskForm):
    news_dd = SelectField('News', choices=[])
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('Update News')


class AdminDeleteNewsForm(FlaskForm):
    news_dd = SelectField('News', choices=[])
    submit = SubmitField('Delete News')


class AdminAddTeamForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = FileField("Team Image", validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Add Team')


class AdminUpdateTeamForm(FlaskForm):
    teams_dd = SelectField('Teams', choices=[])
    name = StringField('Name', validators=[DataRequired()])
    image = FileField("Team Image", validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Update Team')


class AdminDeleteTeamForm(FlaskForm):
    teams_dd = SelectField('Teams', choices=[])
    submit = SubmitField('Delete Team')


class AdminAddPlayerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    number = StringField('Number', validators=[DataRequired()])
    email = StringField('Email', validators=[Email(), DataRequired()])

    birth_day = SelectField('Day',
                            choices=[(val, val) for idx, val in enumerate(range(1, 32))],
                            validators=[DataRequired()])
    birth_month = SelectField('Month',
                            choices=[(val, val) for idx, val in enumerate(range(1, 13))],
                            validators=[DataRequired()])
    birth_year = SelectField('Year',
                            choices=[(val, val) for idx, val in enumerate(range(1920, 2020))],
                            validators=[DataRequired()])
    
    image = FileField("Image", validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    team_dd = SelectField('Team', choices=[])
    
    submit = SubmitField('Submit Player')


class AdminUpdatePlayerForm(FlaskForm):
    player_dd = SelectField('Player', choices=[])

    name = StringField('Name', validators=[DataRequired()])
    number = StringField('Number', validators=[DataRequired()])
    email = StringField('Email', validators=[Email(), DataRequired()])

    birth_day = SelectField('Day',
                            choices=[(val, val) for idx, val in enumerate(range(1, 32))],
                            validators=[DataRequired()])
    birth_month = SelectField('Month',
                            choices=[(val, val) for idx, val in enumerate(range(1, 13))],
                            validators=[DataRequired()])
    birth_year = SelectField('Year',
                            choices=[(val, val) for idx, val in enumerate(range(1920, 2020))],
                            validators=[DataRequired()])
    
    image = FileField("Image", validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    team_dd = SelectField('Team', choices=[])
    
    submit = SubmitField('Submit Player')


class AdminDeletePlayerForm(FlaskForm):
    player_dd = SelectField('Player', choices=[])
    submit = SubmitField('Delete Player')


class AdminMatchForm(FlaskForm):
    host_team_dd = SelectField('Host Team', choices=[])
    guest_team_dd = SelectField('Guest Team', choices=[])

    birth_day = SelectField('Day',
                            choices=[(val, val) for idx, val in enumerate(range(1, 32))],
                            validators=[DataRequired()])
    birth_month = SelectField('Month',
                            choices=[(val, val) for idx, val in enumerate(range(1, 13))],
                            validators=[DataRequired()])
    birth_year = SelectField('Year',
                            choices=[(val, val) for idx, val in enumerate(range(1920, 2020))],
                            validators=[DataRequired()])    
    submit = SubmitField('Submit Match')


class AdminResultForm(FlaskForm):
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


class AdminStatsForm(FlaskForm):
    match = StringField('Match', validators=[DataRequired()])
    player = StringField('Player', validators=[DataRequired()])
    goals = StringField('Goals', validators=[DataRequired()])
    assists = StringField('Assists', validators=[DataRequired()])
    red = StringField('Red', validators=[DataRequired()])
    yellow = StringField('Yellow', validators=[DataRequired()])
    submit = SubmitField('Submit Statistics')
