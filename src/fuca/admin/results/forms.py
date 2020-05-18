from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from fuca.models import Match


class AdminAddResultForm(FlaskForm):
    match_dd = SelectField('Match', choices=[], coerce=int)

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
        match_choices = [(-1, '')] + [(match.id, '{} vs {} at {}'.format(match.host_team.name,
                                                                match.guest_team.name,
                                                                match.date_time.strftime('%d. %m. %Y.'))) for match in matches]
        self.match_dd.choices = match_choices

    def validate_match_dd(self, match_dd):
        if match_dd.data == -1:
            raise ValidationError("You must select a match.")

    def validate_host_team_goals(self, host_team_goals):
        try: 
            n = int(host_team_goals.data)
            if n < 0:
                raise ValidationError('Must be non-negative number!')
        except ValueError:
            raise ValidationError('Must be non-negative number!')

    def validate_host_team_yellow(self, host_team_yellow):
        try: 
            n = int(host_team_yellow.data)
            if n < 0:
                raise ValidationError('Must be non-negative number!')
        except ValueError:
            raise ValidationError('Must be non-negative number!')

    def validate_host_team_red(self, host_team_red):
        try: 
            n = int(host_team_red.data)
            if n < 0:
                raise ValidationError('Must be non-negative number!')
        except ValueError:
            raise ValidationError('Must be non-negative number!')

    def validate_host_team_shots(self, host_team_shots):
        try: 
            n = int(host_team_shots.data)
            if n < 0:
                raise ValidationError('Must be non-negative number!')
        except ValueError:
            raise ValidationError('Must be non-negative number!')

    def validate_guest_team_goals(self, guest_team_goals):
        try: 
            n = int(guest_team_goals.data)
            if n < 0:
                raise ValidationError('Must be non-negative number!')
        except ValueError:
            raise ValidationError('Must be non-negative number!')

    def validate_guest_team_yellow(self, guest_team_yellow):
        try: 
            n = int(guest_team_yellow.data)
            if n < 0:
                raise ValidationError('Must be non-negative number!')
        except ValueError:
            raise ValidationError('Must be non-negative number!')

    def validate_guest_team_red(self, guest_team_red):
        try: 
            n = int(guest_team_red.data)
            if n < 0:
                raise ValidationError('Must be non-negative number!')
        except ValueError:
            raise ValidationError('Must be non-negative number!')

    def validate_guest_team_shots(self, guest_team_shots):
        try: 
            n = int(guest_team_shots.data)
            if n < 0:
                raise ValidationError('Must be non-negative number!')
        except ValueError:
            raise ValidationError('Must be non-negative number!')


class AdminUpdateResultForm(FlaskForm):
    match_dd = SelectField('Result', choices=[], id='select_results', coerce=int)

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
        match_choices = [(-1, '')] + [(match.id, '{} vs {} at {}'.format(match.host_team.name,
                                                                         match.guest_team.name,
                                                                         match.date_time.strftime('%d. %m. %Y.'))) for match in matches]
        self.match_dd.choices = match_choices

    def validate_match_dd(self, match_dd):
        if match_dd.data == -1:
            raise ValidationError("You must select a match.")

    def validate_host_team_goals(self, host_team_goals):
        try: 
            n = int(host_team_goals.data)
            if n < 0:
                raise ValidationError('Must be non-negative number!')
        except ValueError:
            raise ValidationError('Must be non-negative number!')

    def validate_host_team_yellow(self, host_team_yellow):
        try: 
            n = int(host_team_yellow.data)
            if n < 0:
                raise ValidationError('Must be non-negative number!')
        except ValueError:
            raise ValidationError('Must be non-negative number!')

    def validate_host_team_red(self, host_team_red):
        try: 
            n = int(host_team_red.data)
            if n < 0:
                raise ValidationError('Must be non-negative number!')
        except ValueError:
            raise ValidationError('Must be non-negative number!')

    def validate_host_team_shots(self, host_team_shots):
        try: 
            n = int(host_team_shots.data)
            if n < 0:
                raise ValidationError('Must be non-negative number!')
        except ValueError:
            raise ValidationError('Must be non-negative number!')

    def validate_guest_team_goals(self, guest_team_goals):
        try: 
            n = int(guest_team_goals.data)
            if n < 0:
                raise ValidationError('Must be non-negative number!')
        except ValueError:
            raise ValidationError('Must be non-negative number!')

    def validate_guest_team_yellow(self, guest_team_yellow):
        try: 
            n = int(guest_team_yellow.data)
            if n < 0:
                raise ValidationError('Must be non-negative number!')
        except ValueError:
            raise ValidationError('Must be non-negative number!')

    def validate_guest_team_red(self, guest_team_red):
        try: 
            n = int(guest_team_red.data)
            if n < 0:
                raise ValidationError('Must be non-negative number!')
        except ValueError:
            raise ValidationError('Must be non-negative number!')

    def validate_guest_team_shots(self, guest_team_shots):
        try: 
            n = int(guest_team_shots.data)
            if n < 0:
                raise ValidationError('Must be non-negative number!')
        except ValueError:
            raise ValidationError('Must be non-negative number!')
        

class AdminDeleteResultForm(FlaskForm):
    match_dd = SelectField('Result', choices=[], coerce=int)
    submit = SubmitField('Delete Results')

    def populate_dd(self):
        matches = Match.query.all()
        match_choices = [(-1, '')] + [(match.id, '{} vs {} at {}'.format(match.host_team.name,
                                                            match.guest_team.name,
                                                            match.date_time.strftime('%d. %m. %Y.'))) for match in matches]
        self.match_dd.choices = match_choices