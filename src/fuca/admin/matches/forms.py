from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import ValidationError

from fuca.models import Match, Team


class AdminAddMatchForm(FlaskForm):
    host_team_dd = SelectField('Host Team', choices=[])
    guest_team_dd = SelectField('Guest Team', choices=[])

    day = SelectField('Day',choices=[])
    month = SelectField('Month',choices=[])
    year = SelectField('Year', choices=[])
    submit = SubmitField('Add Match')

    def populate_dd(self):
        teams = Team.query.all()
        team_choices = [(team.id, team.name) for team in teams]

        self.host_team_dd.choices = team_choices
        self.guest_team_dd.choices = team_choices

        self.day.choices = [(val, val) for val in range(1, 32)]
        self.month.choices = [(val, val) for val in range(1, 13)]
        self.year.choices = [(val, val) for val in range(2020, 1940, -1)]

    def validate_guest_team_dd(self, guest_team_dd):
        if guest_team_dd.data == self.host_team_dd.data:
            raise ValidationError('Host and guest teams must be different.')


class AdminUpdateMatchForm(FlaskForm):
    match_dd = SelectField('Match', choices=[], id='select_matches')

    host_team_dd = SelectField('Host Team', choices=[])
    guest_team_dd = SelectField('Guest Team', choices=[])

    day = SelectField('Day',choices=[])
    month = SelectField('Month',choices=[])
    year = SelectField('Year', choices=[])
    submit = SubmitField('Update Match')

    def populate_dd(self):
        matches = Match.query.all()
        match_choices = [(-1, '')] + [(match.id, match.host_team.name + ' vs ' + match.guest_team.name) for match in matches]
        self.match_dd.choices = match_choices

        teams = Team.query.all()
        team_choices = [(-1, '')] + [(team.id, team.name) for team in teams]
        self.host_team_dd.choices = team_choices
        self.guest_team_dd.choices = team_choices

        self.day.choices = [(val, val) for val in range(1, 32)]
        self.month.choices = [(val, val) for val in range(1, 13)]
        self.year.choices = [(val, val) for val in range(2020, 1940, -1)]


class AdminDeleteMatchForm(FlaskForm):
    match_dd = SelectField('Match', choices=[])
    submit = SubmitField('Delete Match')

    def populate_dd(self):
        matches = Match.query.all()
        match_choices = [(match.id, match.host_team.name + ' vs ' + match.guest_team.name) for match in matches]
        self.match_dd.choices = match_choices
