from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class AdminNewsForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    content = StringField('Content', validators=[DataRequired()])
    date = StringField('Date', validators=[DataRequired()])
    submit = SubmitField('Submit News')


class AdminTeamForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    image = StringField('Image', validators=[DataRequired()])
    submit = SubmitField('Submit Team')


class AdminPlayerForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    number = StringField('Number', validators=[DataRequired()])
    team = StringField('Team', validators=[DataRequired()])
    birthdate = StringField('Birthdate', validators=[DataRequired()])
    image = StringField('Image', validators=[DataRequired()])
    email = StringField('Email', validators=[Email(), DataRequired()])
    submit = SubmitField('Submit Player')


class AdminMatchForm(FlaskForm):
    date_time = StringField('Date-Time', validators=[DataRequired()])
    host_team = StringField('Host Team', validators=[DataRequired()])
    guest_team = StringField('Guest Team', validators=[DataRequired()])
    submit = SubmitField('Submit Match')


class AdminStatsForm(FlaskForm):
    match = StringField('Match', validators=[DataRequired()])
    player = StringField('Player', validators=[DataRequired()])
    goals = StringField('Goals', validators=[DataRequired()])
    assists = StringField('Assists', validators=[DataRequired()])
    red = StringField('Red', validators=[DataRequired()])
    yellow = StringField('Yellow', validators=[DataRequired()])
    submit = SubmitField('Submit Statistics')
    