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
    submit = SubmitField('Submit News')


class AdminUpdateNewsForm(FlaskForm):
    pass


class AdminDeleteNewsForm(FlaskForm):
    news_db = News.query.all()
    news_list = [news.jinja_dict() for news in news_db]
    news_choices = [(id, news['title'] + ' ' + news['date']) for news in news_list]
    news_dd = SelectField('News', choices=news_choices, validators=[DataRequired()])
    submit = SubmitField('Delete News')


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

    birth_day = SelectField('Day',
                            choices=[(idx, val) for idx, val in enumerate(range(1, 32))],
                            validators=[DataRequired()])
    birth_month = SelectField('Month',
                            choices=[(idx, val) for idx, val in enumerate(range(1, 13))],
                            validators=[DataRequired()])
    birth_year = SelectField('Year',
                            choices=[(idx, val) for idx, val in enumerate(range(1920, 2020))],
                            validators=[DataRequired()])    
    submit = SubmitField('Submit Match')


class AdminResultForm(FlaskForm):
    matches_db = Match.query.all()
    matches = [match.jinja_dict() for match in matches_db]
    match_choices = [(id, match['team1_name'] + ' - ' + match['team2_name']) for match in matches]
    match_dd = SelectField('Match', choices=match_choices, validators=[DataRequired()])

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
