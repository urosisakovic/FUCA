from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError

from fuca import data_utils
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

    def validate_email(self, email):
        valid, player = data_utils.exists_player_with_email(email.data)
        if valid:
            raise ValidationError('Player with that email already exists!')


    def populate_dd(self):
        self.birth_day.choices = [(val, val) for val in range(1, 32)]
        self.birth_month.choices = [(val, val) for val in range(1, 13)]
        self.birth_year.choices = [(val, val) for val in range(2020, 1940, -1)]

        teams = Team.query.all()
        team_choices = [(team.id, team.name) for team in teams]
        self.team_dd.choices = team_choices


class AdminUpdatePlayerForm(FlaskForm):
    player_dd = SelectField('Player', choices=[], id='select_players')

    name = StringField('Name', validators=[DataRequired()])
    number = StringField('Number', validators=[DataRequired()])
    email = StringField('Email', validators=[Email(), DataRequired()])

    birth_day = SelectField('Day',choices=[])
    birth_month = SelectField('Month',choices=[])
    birth_year = SelectField('Year', choices=[])
    
    image = FileField("Image", validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    team_dd = SelectField('Team', choices=[])
    
    submit = SubmitField('Submit Player')

    player_id = -1

    def validate_email(self, email):
        if self.player_id > -1:
            player = Player.query.get(self.player_id)
            if player:
                valid, _ = data_utils.exists_player_with_email(email.data)
                if player.email != email.data and valid:             
                    raise ValidationError('Player with that email already exists!')

    def populate_dd(self):
        self.birth_day.choices = [(val, val) for val in range(1, 32)]
        self.birth_month.choices = [(val, val) for val in range(1, 13)]
        self.birth_year.choices = [(val, val) for val in range(2020, 1940, -1)]

        teams = Team.query.all()
        team_choices = [(-1, '')] + [(team.id, team.name) for team in teams]
        self.team_dd.choices = team_choices

        players = Player.query.filter_by(is_admin=False).all()
        player_choices = [(-1, '')] + [(player.id, player.name) for player in players]
        self.player_dd.choices = player_choices


class AdminDeletePlayerForm(FlaskForm):
    player_dd = SelectField('Player', choices=[])
    submit = SubmitField('Delete Player')

    def populate_dd(self):
        players = Player.query.filter_by(is_admin=False).all()
        player_choices = [(player.id, player.name) for player in players]
        self.player_dd.choices = player_choices
