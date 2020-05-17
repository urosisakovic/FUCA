from datetime import datetime

from flask import redirect, render_template, request, url_for, abort, flash

from flask_login import current_user, login_required
from fuca import data_utils
from fuca.admin.players.forms import (AdminAddPlayerForm, AdminDeletePlayerForm,
                                      AdminUpdatePlayerForm)
from fuca.models import Player
from flask import Blueprint

players = Blueprint('players', __name__)

@players.route("", methods=['GET', 'POST'])
@login_required
def admin_players():
    if not current_user.is_admin:
        abort(403)

    return render_template('admin/players/layout.html', title='Admin Players')


@players.route("/add", methods=['GET', 'POST'])
@login_required
def admin_players_add():
    if not current_user.is_admin:
        abort(403)

    form = AdminAddPlayerForm()
    form.populate_dd()

    if request.method == 'POST':
        if form.validate():
            data_utils.add_player(name=form.name.data,
                                  number=form.number.data,
                                  email=form.email.data,
                                  birthdate=datetime(int(form.birth_year.data),
                                                     int(form.birth_month.data),
                                                     int(form.birth_day.data),
                                                     0, 0, 0),
                                  team_id=form.team_dd.data,
                                  image=form.image.data)
            flash('Successfully added a new player', 'success')
            return redirect(url_for('players.admin_players_add'))

    return render_template('admin/players/add.html', form=form, title='Admin Add Players')


@players.route("/update", methods=['GET', 'POST'])
@login_required
def admin_players_update():
    if not current_user.is_admin:
        abort(403)

    form = AdminUpdatePlayerForm()
    form.populate_dd()

    player_id = request.args.get('id', type=int)
    if request.method == 'GET' and player_id:
        if player_id >= 0:
            player = Player.query.get(player_id)
            form.player_dd.default = player_id
            form.birth_day.default = int(player.birthdate.day)
            form.birth_month.default = int(player.birthdate.month)
            form.birth_year.default = int(player.birthdate.year)
            form.team_dd.default = player.team_id
            form.process()
            form.name.data = player.name
            form.number.data = player.number
            form.email.data = player.email          
        else:
            form.player_dd.default = 0
            form.birth_day.default = 1
            form.birth_month.default = 1
            form.birth_year.default = 1
            form.team_dd.data = 0
            form.process()
            form.name.data = ''
            form.number.data = ''
            form.email.data = ''
            

    if request.method == 'POST':
        form.player_id = int(form.player_dd.data)
        if form.validate():
            data_utils.update_player(id=form.player_dd.data,
                                     name=form.name.data,
                                     number=form.number.data,
                                     email=form.email.data,
                                     birthdate=datetime(int(form.birth_year.data),
                                                        int(form.birth_month.data),
                                                        int(form.birth_day.data),
                                                        0, 0, 0),
                                     team_id=form.team_dd.data,
                                     image=form.image.data)
            flash('Successfully updated a player', 'success')
            return redirect(url_for('players.admin_players_update'))
        
    return render_template('admin/players/update.html', form=form, title='Admin Update Players')


@players.route("/delete", methods=['GET', 'POST'])
@login_required
def admin_players_delete():
    if not current_user.is_admin:
        abort(403)

    form = AdminDeletePlayerForm()
    form.populate_dd()

    if request.method == 'POST':
        data_utils.delete_player(id=form.player_dd.data)
        flash('Successfully deleted a team', 'success')
        return redirect(url_for('players.admin_players_delete'))

    return render_template('admin/players/delete.html', form=form, title='Admin Delete Players')
