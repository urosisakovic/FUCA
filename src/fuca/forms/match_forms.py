from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField

from fuca.models import Match, Team


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
        self.year.choices = [(val, val) for val in range(1920, 2021)]


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
        self.year.choices = [(val, val) for val in range(1920, 2021)]


class AdminDeleteMatchForm(FlaskForm):
    match_dd = SelectField('Match', choices=[])
    submit = SubmitField('Delete Match')

    def populate_dd(self):
        matches_db = Match.query.all()
        matches = [match.jinja_dict() for match in matches_db]
        match_choices = [(match['id'], match['team1_name'] + ' vs ' + match['team2_name']) for match in matches]
        self.match_dd.choices = match_choices
