from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import (BooleanField, PasswordField, SelectField, StringField,
                     SubmitField)
from wtforms.validators import DataRequired, Email
from fuca.models import Team, Match, News, Player


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class AdminAddNewsForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('Add News')

    def populate_dd(self):
        pass


class AdminUpdateNewsForm(FlaskForm):
    news_dd = SelectField('News', choices=[])
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    submit = SubmitField('Update News')

    def populate_dd(self):
        news_db = News.query.all()
        news_list = [news.jinja_dict() for news in news_db]
        news_choices = [(news['id'], news['title'] + ' ' + news['date']) for news in news_list]
        self.news_dd.choices = news_choices


class AdminDeleteNewsForm(FlaskForm):
    news_dd = SelectField('News', choices=[])
    submit = SubmitField('Delete News')

    def populate_dd(self):
        news_db = News.query.all()
        news_list = [news.jinja_dict() for news in news_db]
        news_choices = [(news['id'], news['title'] + ' ' + news['date']) for news in news_list]
        self.news_dd.choices = news_choices


class AdminAddTeamForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = FileField("Team Image", validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Add Team')

    def populate_dd(self):
        pass


class AdminUpdateTeamForm(FlaskForm):
    teams_dd = SelectField('Teams', choices=[])
    name = StringField('Name', validators=[DataRequired()])
    image = FileField("Team Image", validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    submit = SubmitField('Update Team')

    def populate_dd(self):
        teams_db = Team.query.all()
        teams = [team.jinja_dict() for team in teams_db]
        team_choices = [(team['id'], team['name']) for team in teams]
        self.teams_dd.choices = team_choices


class AdminDeleteTeamForm(FlaskForm):
    teams_dd = SelectField('Teams', choices=[])
    submit = SubmitField('Delete Team')

    def populate_dd(self):
        teams_db = Team.query.all()
        teams = [team.jinja_dict() for team in teams_db]
        team_choices = [(team['id'], team['name']) for team in teams]
        self.teams_dd.choices = team_choices


class AdminAddPlayerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    number = StringField('Number', validators=[DataRequired()])
    email = StringField('Email', validators=[Email(), DataRequired()])

    birth_day = SelectField('Day',choices=[])
    birth_month = SelectField('Month',choices=[])
    birth_year = SelectField('Year', choices=[])
    
    image = FileField("Image", validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    team_dd = SelectField('Team', choices=[])
    
    submit = SubmitField('Submit Player')

    def populate_dd(self):
        self.birth_day.choices = [(val, val) for val in range(1, 32)]
        self.birth_month.choices = [(val, val) for val in range(1, 13)]
        self.birth_year.choices = [(val, val) for val in range(1920, 2020)]

        teams_db = Team.query.all()
        teams = [team.jinja_dict() for team in teams_db]
        team_choices = [(team['id'], team['name']) for team in teams]
        self.team_dd.choices = team_choices


class AdminUpdatePlayerForm(FlaskForm):
    player_dd = SelectField('Player', choices=[])

    name = StringField('Name', validators=[DataRequired()])
    number = StringField('Number', validators=[DataRequired()])
    email = StringField('Email', validators=[Email(), DataRequired()])

    birth_day = SelectField('Day',choices=[])
    birth_month = SelectField('Month',choices=[])
    birth_year = SelectField('Year', choices=[])
    
    image = FileField("Image", validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    team_dd = SelectField('Team', choices=[])
    
    submit = SubmitField('Submit Player')

    def populate_dd(self):
        self.birth_day.choices = [(val, val) for val in range(1, 32)]
        self.birth_month.choices = [(val, val) for val in range(1, 13)]
        self.birth_year.choices = [(val, val) for val in range(1920, 2020)]

        teams_db = Team.query.all()
        teams = [team.jinja_dict() for team in teams_db]
        team_choices = [(team['id'], team['name']) for team in teams]
        self.team_dd.choices = team_choices

        players_db = Player.query.all()
        players = [player.jinja_dict() for player in players_db]
        player_choices = [(player['team_id'], player['name']) for player in players]
        self.player_dd.choices = player_choices


class AdminDeletePlayerForm(FlaskForm):
    player_dd = SelectField('Player', choices=[])
    submit = SubmitField('Delete Player')

    def populate_dd(self):
        players_db = Player.query.all()
        players = [player.jinja_dict() for player in players_db]
        player_choices = [(player['team_id'], player['name']) for player in players]
        self.player_dd.choices = player_choices


class AdminAddMatchForm(FlaskForm):
    host_team_dd = SelectField('Host Team', choices=[])
    guest_team_dd = SelectField('Guest Team', choices=[])

    day = SelectField('Day',choices=[])
    month = SelectField('Month',choices=[])
    year = SelectField('Year', choices=[])
    submit = SubmitField('Add Match')

    def populate_dd(self):
        teams_db = Team.query.all()
        teams = [team.jinja_dict() for team in teams_db]
        team_choices = [(team['id'], team['name']) for team in teams]

        self.host_team_dd.choices = team_choices
        self.guest_team_dd.choices = team_choices

        self.day.choices = [(val, val) for val in range(1, 32)]
        self.month.choices = [(val, val) for val in range(1, 13)]
        self.year.choices = [(val, val) for val in range(1920, 2020)]


class AdminUpdateMatchForm(FlaskForm):
    match_dd = SelectField('Match', choices=[])

    host_team_dd = SelectField('Host Team', choices=[])
    guest_team_dd = SelectField('Guest Team', choices=[])

    day = SelectField('Day',choices=[])
    month = SelectField('Month',choices=[])
    year = SelectField('Year', choices=[])
    submit = SubmitField('Update Match')

    def populate_dd(self):
        matches_db = Match.query.all()
        matches = [match.jinja_dict() for match in matches_db]
        match_choices = [(match['id'], match['team1_name'] + ' vs ' + match['team2_name']) for match in matches]
        self.match_dd.choices = match_choices

        teams_db = Team.query.all()
        teams = [team.jinja_dict() for team in teams_db]
        team_choices = [(team['id'], team['name']) for team in teams]
        self.host_team_dd.choices = team_choices
        self.guest_team_dd.choices = team_choices

        self.day.choices = [(val, val) for val in range(1, 32)]
        self.month.choices = [(val, val) for val in range(1, 13)]
        self.year.choices = [(val, val) for val in range(1920, 2020)]


class AdminDeleteMatchForm(FlaskForm):
    match_dd = SelectField('Match', choices=[])
    submit = SubmitField('Delete Match')

    def populate_dd(self):
        matches_db = Match.query.all()
        matches = [match.jinja_dict() for match in matches_db]
        match_choices = [(match['id'], match['team1_name'] + ' vs ' + match['team2_name']) for match in matches]
        self.match_dd.choices = match_choices


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
