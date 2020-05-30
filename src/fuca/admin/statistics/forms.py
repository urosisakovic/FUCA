"""
Author: Uros Isakovic
"""
from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField
from wtforms.validators import DataRequired, ValidationError
from fuca.models import Match, Player


class AdminAddStatisticsForm(FlaskForm):
    match_dd = SelectField('Match', choices=[], coerce=int, id='select_match_add')
    player_dd = SelectField('Player', choices=[], coerce=int)

    goals = StringField('Goals', validators=[DataRequired()])
    assists = StringField('Assists', validators=[DataRequired()])
    red = StringField('Red', validators=[DataRequired()])
    yellow = StringField('Yellow', validators=[DataRequired()])
    submit = SubmitField('Add Statistics')

    def populate_dd(self):
        matches = Match.query.all()
        match_choices = [(-1, '')] + [(match.id, '{} vs {} at {}'.format(match.host_team.name,
                                                                         match.guest_team.name,
                                                                         match.date_time.strftime('%d. %m. %Y.'))) for match in matches]
        self.match_dd.choices = match_choices

    def validate_match_dd(self, match_dd):
        if match_dd.data == -1:
            raise ValidationError('You must choose a match.')

    def validate_player_dd(self, player_dd):
        if player_dd.data == -1:
            raise ValidationError('You must choose a player.')
            return

        player = Player.query.get(player_dd.data)
        match = Match.query.get(self.match_dd.data)

        if player and match: 
            if player.team_id not in [match.host_team_id, match.guest_team_id]:
                raise ValidationError('Player is not in the host or the guest team.') 
    

class AdminUpdateStatisticsForm(FlaskForm):
    match_dd = SelectField('Match', choices=[], id='select_match', coerce=int)
    player_dd = SelectField('Player', choices=[], coerce=int)

    goals = StringField('Goals', validators=[DataRequired()])
    assists = StringField('Assists', validators=[DataRequired()])
    red = StringField('Red', validators=[DataRequired()])
    yellow = StringField('Yellow', validators=[DataRequired()])
    submit = SubmitField('Update Statistics')

    def populate_dd(self):
        matches = Match.query.all()
        match_choices = [(-1, '')] + [(match.id, '{} vs {} at {}'.format(match.host_team.name,
                                                                         match.guest_team.name,
                                                                         match.date_time.strftime('%d. %m. %Y.'))) for match in matches]
        self.match_dd.choices = match_choices

    def validate_match_dd(self, match_dd):
        if match_dd.data == -1:
            raise ValidationError('You must choose a match.')

    def validate_player_dd(self, player_dd):
        if player_dd.data == -1:
            raise ValidationError('You must choose a player.')
            return

        player = Player.query.get(player_dd.data)
        match = Match.query.get(self.match_dd.data)

        if player and match: 
            if player.team_id not in [match.host_team_id, match.guest_team_id]:
                raise ValidationError('Player is not in the host or the guest team.') 


class AdminDeleteStatisticsForm(FlaskForm):
    match_dd = SelectField('Match', choices=[], coerce=int, id='select_match_delete')
    player_dd = SelectField('Player', choices=[], coerce=int)
    submit = SubmitField('Delete Statistics')

    def populate_dd(self):
        matches = Match.query.all()
        match_choices = [(-1, '')] + [(match.id, '{} vs {} at {}'.format(match.host_team.name,
                                                                         match.guest_team.name,
                                                                         match.date_time.strftime('%d. %m. %Y.'))) for match in matches]
        self.match_dd.choices = match_choices