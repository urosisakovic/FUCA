from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Email

from fuca.models import Player, Team


class AdminAddPlayerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    number = StringField('Number', validators=[DataRequired()])
    email = StringField('Email', validators=[Email(), DataRequired()])

    birth_day = SelectField('Day',choices=[])
    birth_month = SelectField('Month',choices=[])
    birth_year = SelectField('Year', choices=[])
    
    image = FileField('Image', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    team_dd = SelectField('Team', choices=[])
    
    submit = SubmitField('Submit Player')

    def populate_dd(self):
        self.birth_day.choices = [(val, val) for val in range(1, 32)]
        self.birth_month.choices = [(val, val) for val in range(1, 13)]
        self.birth_year.choices = [(val, val) for val in range(1920, 2021)]

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
        self.birth_year.choices = [(val, val) for val in range(1920, 2021)]

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
