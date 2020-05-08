from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired

from fuca.models import Team


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