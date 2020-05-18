from datetime import datetime

from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, ValidationError

from fuca import data_utils

from fuca.models import Player, Team


class AdminAddPlayerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    number = StringField('Jersey Number', validators=[DataRequired()])
    email = StringField('Email', validators=[Email(), DataRequired()])

    birth_day = SelectField('Day',choices=[], coerce=int)
    birth_month = SelectField('Month',choices=[], coerce=int)
    birth_year = SelectField('Year', choices=[], coerce=int)
    
    image = FileField('Image', validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    team_dd = SelectField('Team', choices=[], coerce=int)
    
    submit = SubmitField('Submit Player')

    def validate_email(self, email):
        valid, player = data_utils.exists_player_with_email(email.data)
        if valid:
            raise ValidationError('Player with that email already exists!')

    def validate_number(self, number):
        try: 
            n = int(number.data)
            if n >= 100 or n < 0:
                raise ValidationError('Invalid jersey number!')
        except ValueError:
            raise ValidationError('Invalid jersey number!')

        teammates = Player.query.filter_by(team_id=self.team_dd.data).all()
        teammates_numbers = [teammate.number for teammate in teammates]
        if int(number.data) in teammates_numbers:
            raise ValidationError('Other teammate already has that number!')


    def populate_dd(self):
        self.birth_day.choices = [(val, val) for val in range(1, 32)]
        self.birth_month.choices = [(val, val) for val in range(1, 13)]
        self.birth_year.choices = [(val, val) for val in range(2020, 2025)]

        teams = Team.query.all()
        team_choices = [(team.id, team.name) for team in teams]
        self.team_dd.choices = team_choices


class AdminUpdatePlayerForm(FlaskForm):
    player_dd = SelectField('Player', choices=[], id='select_players', coerce=int)

    name = StringField('Name', validators=[DataRequired()])
    number = StringField('Jersey Number', validators=[DataRequired()])
    email = StringField('Email', validators=[Email(), DataRequired()])

    birth_day = SelectField('Day',choices=[], coerce=int)
    birth_month = SelectField('Month',choices=[], coerce=int)
    birth_year = SelectField('Year', choices=[], coerce=int)
    
    image = FileField("Image", validators=[FileAllowed(['jpg', 'jpeg', 'png'])])
    team_dd = SelectField('Team', choices=[], coerce=int)
    
    submit = SubmitField('Submit Player')

    def validate_player_dd(self, player_dd):
        if player_dd.data == -1:
            raise ValidationError('You must select a player.')

    def validate_email(self, email):
        if self.player_dd.data > -1:
            update_player = Player.query.get(self.player_dd.data)
            valid, player = data_utils.exists_player_with_email(email.data)

            if valid and update_player.id != player.id:             
                raise ValidationError('Player with that email already exists!')

    def validate_number(self, number):
        try: 
            n = int(number.data)
            if n >= 100 or n < 0:
                raise ValidationError('Invalid jersey number!')
        except ValueError:
            raise ValidationError('Invalid jersey number!')

        teammates = Player.query.filter_by(team_id=self.team_dd.data).filter(Player.id != self.player_dd.data).all()
        teammates_numbers = [teammate.number for teammate in teammates]
        if int(number.data) in teammates_numbers:
            raise ValidationError('Other teammate already has that number!')

    def populate_dd(self):
        self.birth_day.choices = [(val, val) for val in range(1, 32)]
        self.birth_month.choices = [(val, val) for val in range(1, 13)]
        self.birth_year.choices = [(val, val) for val in range(2020, 2025)]

        teams = Team.query.all()
        team_choices = [(team.id, team.name) for team in teams]
        self.team_dd.choices = team_choices

        players = Player.query.filter_by(is_admin=False).all()
        player_choices = [(-1, '')] + [(player.id, player.name) for player in players]
        self.player_dd.choices = player_choices


class AdminDeletePlayerForm(FlaskForm):
    player_dd = SelectField('Player', choices=[])
    submit = SubmitField('Delete Player')

    def populate_dd(self):
        players = Player.query.filter_by(is_admin=False).all()
        player_choices = [(player.id, player.name + ' ' + str(player.number) + ' [' + player.team.name + ']') for player in players]
        self.player_dd.choices = player_choices
