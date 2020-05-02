import os
from datetime import datetime

from flask import redirect, render_template, request, url_for

from fuca import app, data_utils
from fuca.forms import (AdminAddPlayerForm, AdminDeletePlayerForm,
                        AdminUpdatePlayerForm)
from fuca.models import Player


@app.route("/admin/players", methods=['GET', 'POST'])
def admin_players():
    return render_template('admin/players/layout.html', title='Admin Players')


@app.route("/admin/players/add", methods=['GET', 'POST'])
def admin_players_add():
    form = AdminAddPlayerForm()
    form.populate_dd()

    if request.method == 'POST':
        data_utils.add_player(name=form.name.data,
                              number=form.number.data,
                              email=form.email.data,
                              birthdate=datetime(form.birth_year.data,
                                                    form.birth_month.data, 
                                                    form.birth_day.data, 
                                                    0, 0, 0),
                              team_id=form.team_dd.data,
                              image=form.image.data)
        return redirect(url_for('admin_players_add'))

    return render_template('admin/players/add.html', form=form, title='Admin Add Players')


@app.route("/admin/players/update", methods=['GET', 'POST'])
def admin_players_update():
    form = AdminUpdatePlayerForm()
    form.populate_dd()

    if request.method == 'POST':
        data_utils.update_player(id=form.player_dd.data,
                                 name=form.name.data,
                                 number=form.number.data,
                                 email=form.email.data,
                                 birthdate=datetime(form.birth_year.data,
                                                    form.birth_month.data, 
                                                    form.birth_day.data, 
                                                    0, 0, 0),
                                 team_id=form.team_dd.data,
                                 image=form.image.data)
        return redirect(url_for('admin_players_update'))

    return render_template('admin/players/update.html', form=form, title='Admin Update Players')


@app.route("/admin/players/delete", methods=['GET', 'POST'])
def admin_players_delete():
    form = AdminDeletePlayerForm()
    form.populate_dd()

    if request.method == 'POST':
        data_utils.delete_player(id=form.player_dd.data)
        return redirect(url_for('admin_players_delete'))

    return render_template('admin/players/delete.html', form=form, title='Admin Delete Players')
