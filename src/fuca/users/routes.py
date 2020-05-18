
from flask import Blueprint, flash, redirect, render_template, request, url_for

from flask_login import current_user, login_required, login_user, logout_user
from fuca import data_utils, db
from fuca.users.forms import LoginForm, RegisterForm, ChangePasswordForm
from fuca.models import Match, PlayingMatch

users = Blueprint('users', __name__)

@users.route("/login", methods=['GET', 'POST'])
def login():
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
    logout_user()
    flash('Successfully logged out!', 'success')
    return redirect(url_for('main.home'))


@users.route("/account", methods=['GET', 'POST'])
@login_required
def account():
    form = ChangePasswordForm()
    if form.validate_on_submit():
        data_utils.register_player(current_user.email, form.new_password.data)
        flash('You have successfully changed your password.', 'success')

    image_file = url_for('static', filename='images/players/{}'.format(current_user.image))
    return render_template('users/account.html', form=form, image_file=image_file, title='My Account')


@users.route("/myteam", methods=['GET'])
@login_required
def myteam():
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
