"""
Author: Djodje Vucinic
"""
from flask_wtf import FlaskForm
from fuca import data_utils
from wtforms import BooleanField, PasswordField, StringField, SubmitField
from wtforms.validators import DataRequired, Email, EqualTo, ValidationError, Length
from flask_login import current_user


class LoginForm(FlaskForm):
    """
    Class which implements user form for logging in.
    """
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    """
    Class which implements user form for registering.
    """
    email = StringField('Email', validators=[Email(), DataRequired()])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=8, max=30)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_email(self, email):
        valid, player = data_utils.exists_player_with_email(email.data)

        if not valid:
            raise ValidationError('This email is not registered to a FUCA player.')

        if data_utils.is_registered_player(email.data):
            raise ValidationError('This email is already used by another FUCA account.')

    def validate_password(self, password):
        rules = [lambda s: any(c.isupper() for c in s),
                 lambda s: any(c.islower() for c in s),
                 lambda s: any(c.isdigit() for c in s),
                 lambda s: any(not c.isalnum() for c in s)]
        if not all(rule(password.data) for rule in rules):
            raise ValidationError('Password must contain at least 1 uppecase character,\
                                  1 lowercase chacater, 1 digit and 1 special character.')


class ChangePasswordForm(FlaskForm):
    """
    Class which implements user form for changing password.
    """
    current_password = PasswordField('Current Password', 
                                     validators=[DataRequired()])
    new_password = PasswordField('Password',
                                validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[EqualTo('new_password')])
    submit = SubmitField('Change Password')

    def validate_current_password(self, current_password):
        valid, _ = data_utils.exists_player(current_user.email, current_password.data)
        if not valid:
            raise ValidationError('Current password is not correct.')

    def validate_new_password(self, password):
        rules = [lambda s: any(c.isupper() for c in s),
                 lambda s: any(c.islower() for c in s),
                 lambda s: any(c.isdigit() for c in s),
                 lambda s: any(not c.isalnum() for c in s)]
        if not all(rule(password.data) for rule in rules):
            raise ValidationError('Password must contain at least 1 uppecase character,\
                                  1 lowercase chacater, 1 digit and 1 special character.')


class RequestResetForm(FlaskForm):
    """
    Class which implements user form for requesting a password reset.
    """
    email = StringField('Email', validators=[Email(), DataRequired()])
    submit = SubmitField('Request Password Reset')

    def validate_email(self, email):
        valid, player = data_utils.exists_player_with_email(email.data)

        if not valid:
            raise ValidationError('This email is not registered to a FUCA player.')
            return

class ResetPasswordForm(FlaskForm):
    """
    Class which implements user form for validating a password reset.
    """
    new_password = PasswordField('New Password', validators=[DataRequired(), Length(min=8, max=30)])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('new_password')])
    submit = SubmitField('Reset Password')

    def validate_new_password(self, password):
        rules = [lambda s: any(c.isupper() for c in s),
                 lambda s: any(c.islower() for c in s),
                 lambda s: any(c.isdigit() for c in s),
                 lambda s: any(not c.isalnum() for c in s)]
        if not all(rule(password.data) for rule in rules):
            raise ValidationError('Password must contain at least 1 uppecase character,\
                                  1 lowercase chacater, 1 digit and 1 special character.')