
from flask import Blueprint, flash, redirect, render_template, request, url_for

from flask_login import current_user, login_required, login_user, logout_user
from fuca import data_utils
from fuca.users.forms import LoginForm, RegisterForm, ChangePasswordForm

users = Blueprint('users', __name__)

@users.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))

    form = LoginForm()
    if form.validate_on_submit():
        valid, player = data_utils.exists_player(email=form.email.data,
                                                 password=form.password.data)
            
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
