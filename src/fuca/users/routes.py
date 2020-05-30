
"""
Author: Djodje Vucinic
"""
from flask import Blueprint, flash, redirect, render_template, request, url_for

from flask_login import current_user, login_required, login_user, logout_user
from fuca import data_utils, db, mail
from fuca.users.forms import (LoginForm, RegisterForm, ChangePasswordForm,
                                RequestResetForm, ResetPasswordForm)
from fuca.models import Match, PlayingMatch, Player
from flask_mail import Message

users = Blueprint('users', __name__)

@users.route("/login", methods=['GET', 'POST'])
def login():
    """
    Route function for login page.
    """
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = LoginForm()
    if form.validate_on_submit():
        valid, player = data_utils.exists_player(email=form.email.data,
                                                 password=form.password.data)

        print('Player: ', player)

        if valid:
            login_user(player, remember=form.remember_me.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('main.home'))
        else:
            flash('Login unsuccessful! Please check email and password.', 'danger')
                        
    return render_template('users/login.html', form=form, title='Login')


@users.route("/register", methods=['GET', 'POST'])
def register():
    """
    Route function for register page.
    """
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = RegisterForm()
    if form.validate_on_submit():
        player = data_utils.register_player(form.email.data, form.password.data)
        flash('Account for {} has been created! You are now able to log in.'.format(player.name), 'success')
        return redirect(url_for('users.login'))
    return render_template('users/register.html', form=form, title='Register')


@users.route("/logout")
def logout():
    """
    Route function for logout page.
    """
    logout_user()
    flash('Successfully logged out!', 'success')
    return redirect(url_for('main.home'))


@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    """
    Route function for account page.
    """
    form = ChangePasswordForm()
    if form.validate_on_submit():
        data_utils.register_player(current_user.email, form.new_password.data)
        flash('You have successfully changed your password.', 'success')

    image_file = url_for('static', filename='images/players/{}'.format(current_user.image))
    return render_template('users/account.html', form=form, image_file=image_file, title='My Account')


@users.route("/myteam", methods=['GET'])
@login_required
def myteam():
    """
    Route function for my-team page.
    """
    matches = Match.query.filter_by(host_team_id=current_user.team_id).all() +\
        Match.query.filter_by(guest_team_id=current_user.team_id).all()

    match_id = request.args.get('match', type=int)
    player_id = request.args.get('player', type=int)
    playing = request.args.get('playing', type=int)
    
    if request.method == 'GET' and \
    (match_id is not None) and \
    (player_id is not None) and \
    (player_id > 1) and \
    (playing is not None):
        if playing:
            print('playing=True')
            pm = PlayingMatch.query.filter_by(match_id=match_id).filter_by(player_id=player_id).first()
            if pm:
                pm.playing = True
            else:
                pm = PlayingMatch(match_id=match_id, player_id=player_id, playing=True)
                db.session.add(pm)
        else:
            print('playing=False')
            pm = PlayingMatch.query.filter_by(match_id=match_id).filter_by(player_id=player_id).first()
            if pm:
                pm.playing = False
            else:
                pm = PlayingMatch(match_id=match_id, player_id=player_id, playing=False)
                db.session.add(pm)

        db.session.commit()
        redirect(url_for('users.myteam'))

    for match in matches:
        match.playing = match.host_team_playing if \
                        current_user.team_id == match.host_team_id else \
                        match.guest_team_playing

        match.not_playing = match.host_team_not_playing if \
                            current_user.team_id == match.host_team_id else \
                            match.guest_team_not_playing

        match.pending = match.host_team.players_count if \
                        current_user.team_id == match.host_team_id else \
                        match.guest_team.players_count
        match.pending -= match.playing + match.not_playing

        match.current_user_yes = ''
        match.current_user_no = ''
        pm = PlayingMatch.query.filter_by(player_id=current_user.id).filter_by(match_id=match.id).first()
        if pm:
            if pm.playing == True:
                match.current_user_yes = 'checked'
            else:
                match.current_user_no = 'checked'

    return render_template('users/myteam.html',
                            matches=matches,
                            title='My Team')


def send_reset_email(player):
    """
    Route function for reset email page.
    """
    token = player.get_reset_token()
    msg = Message('Password Reset Request',
                  sender='noreply@fuca.com',
                  recipients=[player.email])

    msg.body = '''
To reset your password, visit the following link:
{}

If you did not make this request, then simply ignore this email and no changes will be made.
'''.format(url_for('users.reset_token', token=token, _external=True))

    mail.send(msg)


@users.route("/reset_password", methods=['GET', 'POST'])
def reset_request():
    """
    Route function for request reset page.
    """
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = RequestResetForm()

    if form.validate_on_submit():
        player = Player.query.filter_by(email=form.email.data).first()
        send_reset_email(player)
        flash('An email has been sent with instruction to reset your password', 'info')
        return redirect(url_for('users.login'))

    return render_template('users/reset_request.html',
                            form=form,
                            title='Reset Password')


@users.route("/reset_password/<token>", methods=['GET', 'POST'])
def reset_token(token):
    """
    Route function for validating reset password request page.
    """
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    player = Player.verify_reset_token(token)

    if player is None:
        flash('That is an invalid or expired token', 'warning')
        return redirect(url_for('users.reset_request'))

    form = ResetPasswordForm()
    if form.validate_on_submit():
        data_utils.register_player(player.email, form.new_password.data)
        flash('Your password has been updated! You are now able to log in!', 'success')
        return redirect(url_for('users.login'))

    return render_template('users/reset_token.html',
                            form=form,
                            title='Reset Password')
