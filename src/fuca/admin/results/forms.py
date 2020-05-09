from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired
from fuca.models import Team, Match


class AdminAddResultForm(FlaskForm):
    match_dd = SelectField('Match', choices=[])

    host_team_goals = StringField('Host Team Goals', validators=[DataRequired()])
    host_team_yellow = StringField('Host Team Yellow', validators=[DataRequired()])
    host_team_red = StringField('Host Team Red', validators=[DataRequired()])
    host_team_shots = StringField('Host Team Shots', validators=[DataRequired()])

    guest_team_goals = StringField('Guest Team Goals', validators=[DataRequired()])
    guest_team_yellow = StringField('Guest Team Yellow', validators=[DataRequired()])
    guest_team_red = StringField('Guest Team Red', validators=[DataRequired()])
    guest_team_shots = StringField('Guest Team Shots', validators=[DataRequired()])

    submit = SubmitField('Add Results')

    def populate_dd(self):
        matches = Match.query.all()
        match_choices = [(match.id, match.host_team.name + ' vs ' + match.guest_team.name) for match in matches]
        self.match_dd.choices = match_choices


class AdminUpdateResultForm(FlaskForm):
    match_dd = SelectField('Result', choices=[], id='select_results')

    host_team_goals = StringField('Host Team Goals', validators=[DataRequired()])
    host_team_yellow = StringField('Host Team Yellow', validators=[DataRequired()])
    host_team_red = StringField('Host Team Red', validators=[DataRequired()])
    host_team_shots = StringField('Host Team Shots', validators=[DataRequired()])

    guest_team_goals = StringField('Guest Team Goals', validators=[DataRequired()])
    guest_team_yellow = StringField('Guest Team Yellow', validators=[DataRequired()])
    guest_team_red = StringField('Guest Team Red', validators=[DataRequired()])
    guest_team_shots = StringField('Guest Team Shots', validators=[DataRequired()])

    submit = SubmitField('Update Results')

    def populate_dd(self):
        matches = Match.query.all()
        match_choices = [(-1, '')] + [(match.id, match.host_team.name + ' vs ' + match.guest_team.name) for match in matches]
        self.match_dd.choices = match_choices


class AdminDeleteResultForm(FlaskForm):
    match_dd = SelectField('Result', choices=[])
    submit = SubmitField('Delete Results')

    def populate_dd(self):
        matches = Match.query.all()
        match_choices = [(match.id, match.host_team.name + ' vs ' + match.guest_team.name) for match in matches]
        self.match_dd.choices = match_choices