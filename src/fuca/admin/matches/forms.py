from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import ValidationError

from fuca.models import Match, Team


class AdminAddMatchForm(FlaskForm):
    host_team_dd = SelectField('Host Team', choices=[], coerce=int)
    guest_team_dd = SelectField('Guest Team', choices=[], coerce=int)

    hours = SelectField('Hours', choices=[], coerce=int)
    minutes = SelectField('Minutes', choices=[], coerce=int)
    day = SelectField('Day', choices=[], coerce=int)
    month = SelectField('Month', choices=[], coerce=int)
    year = SelectField('Year', choices=[], coerce=int)
    submit = SubmitField('Add Match')

    def populate_dd(self):
        teams = Team.query.all()
        team_choices = [(team.id, team.name) for team in teams]

        self.host_team_dd.choices = team_choices
        self.guest_team_dd.choices = team_choices

        self.minutes.choices = [(val, val) for val in range(0, 60, 5)]
        self.hours.choices = [(val, val) for val in range(0, 24)]
        self.day.choices = [(val, val) for val in range(1, 32)]
        self.month.choices = [(val, val) for val in range(1, 13)]
        self.year.choices = [(val, val) for val in range(2020, 2025)]

    def validate_guest_team_dd(self, guest_team_dd):
        if guest_team_dd.data == self.host_team_dd.data:
            raise ValidationError('Host and guest teams must be different.')


class AdminUpdateMatchForm(FlaskForm):
    match_dd = SelectField('Match', choices=[], id='select_matches', coerce=int)

    host_team_dd = SelectField('Host Team', choices=[], coerce=int)
    guest_team_dd = SelectField('Guest Team', choices=[], coerce=int)

    hours = SelectField('Hours', choices=[], coerce=int)
    minutes = SelectField('Minutes', choices=[], coerce=int)
    day = SelectField('Day',choices=[], coerce=int)
    month = SelectField('Month',choices=[], coerce=int)
    year = SelectField('Year', choices=[], coerce=int)
    submit = SubmitField('Update Match')

    def populate_dd(self):
        matches = Match.query.all()
        match_choices = [(-1, '')] + [(match.id, '{} vs {} at {}'.format(match.host_team.name,
                                                            match.guest_team.name,
                                                            match.date_time.strftime('%d. %m. %Y.'))) for match in matches]
        self.match_dd.choices = match_choices

        teams = Team.query.all()
        team_choices = [(-1, '')] + [(team.id, team.name) for team in teams]
        self.host_team_dd.choices = team_choices
        self.guest_team_dd.choices = team_choices

        self.minutes.choices = [(val, val) for val in range(0, 60, 5)]
        self.hours.choices = [(val, val) for val in range(0, 24)]
        self.day.choices = [(val, val) for val in range(1, 32)]
        self.month.choices = [(val, val) for val in range(1, 13)]
        self.year.choices = [(val, val) for val in range(2020, 2025)]

    def validate_match_dd(self, match_dd):
        if match_dd.data == -1:
            raise ValidationError('You must select a match.')

    def validate_guest_team_dd(self, guest_team_dd):
        if guest_team_dd.data == self.host_team_dd.data:
            raise ValidationError('Host and guest teams must be different.')


class AdminDeleteMatchForm(FlaskForm):
    match_dd = SelectField('Match', choices=[])
    submit = SubmitField('Delete Match')

    def populate_dd(self):
        matches = Match.query.all()
        match_choices = [(match.id, '{} vs {} at {}'.format(match.host_team.name,
                                                            match.guest_team.name,
                                                            match.date_time.strftime('%d. %m. %Y.'))) for match in matches]
        self.match_dd.choices = match_choices

