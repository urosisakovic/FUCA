from flask_wtf import FlaskForm
from flask_wtf.file import FileAllowed, FileField
from wtforms import (BooleanField, PasswordField, SelectField, StringField,
                     SubmitField)
from wtforms.validators import DataRequired, Email
from fuca.models import Team, Match, News, Player


class AdminAddStatsForm(FlaskForm):
    match = StringField('Match', validators=[DataRequired()])
    player = StringField('Player', validators=[DataRequired()])
    goals = StringField('Goals', validators=[DataRequired()])
    assists = StringField('Assists', validators=[DataRequired()])
    red = StringField('Red', validators=[DataRequired()])
    yellow = StringField('Yellow', validators=[DataRequired()])
    submit = SubmitField('Submit Statistics')


class AdminUpdateStatsForm(FlaskForm):
    match = StringField('Match', validators=[DataRequired()])
    player = StringField('Player', validators=[DataRequired()])
    goals = StringField('Goals', validators=[DataRequired()])
    assists = StringField('Assists', validators=[DataRequired()])
    red = StringField('Red', validators=[DataRequired()])
    yellow = StringField('Yellow', validators=[DataRequired()])
    submit = SubmitField('Submit Statistics')


class AdminDeleteStatsForm(FlaskForm):
    match = StringField('Match', validators=[DataRequired()])
    player = StringField('Player', validators=[DataRequired()])
    goals = StringField('Goals', validators=[DataRequired()])
    assists = StringField('Assists', validators=[DataRequired()])
    red = StringField('Red', validators=[DataRequired()])
    yellow = StringField('Yellow', validators=[DataRequired()])
    submit = SubmitField('Submit Statistics')