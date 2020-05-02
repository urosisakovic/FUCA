import os
from datetime import datetime

from flask import flash, redirect, render_template, request, url_for

from fuca import app, db
from fuca.forms import (AdminAddNewsForm, AdminAddPlayerForm, AdminAddTeamForm,
                        AdminDeleteNewsForm, AdminDeletePlayerForm,
                        AdminDeleteTeamForm, AdminMatchForm, AdminResultForm,
                        AdminStatsForm, AdminUpdateNewsForm,
                        AdminUpdatePlayerForm, AdminUpdateTeamForm, LoginForm)
from fuca.models import Match, News, Player, Statistics, Team


def save_image(form_image, image_name, team_player):
    _, f_ext = os.path.splitext(form_image.filename)
    image_fn = image_name + f_ext
    image_path = os.path.join(app.root_path, 'static/images/{}/{}'.format(team_player, image_fn))
    form_image.save(image_path)
    return image_fn


@app.route("/admin/players", methods=['GET', 'POST'])
def admin_players():
    return render_template('admin/players/layout.html', title='Admin Players')


@app.route("/admin/players/add", methods=['GET', 'POST'])
def admin_players_add():
    form = AdminAddPlayerForm()
    form.populate_dd()

    if request.method == 'POST':
        pass

    return render_template('admin/players/add.html', form=form, title='Admin Add Players')


@app.route("/admin/players/update", methods=['GET', 'POST'])
def admin_players_update():
    form = AdminUpdatePlayerForm()
    form.populate_dd()

    if request.method == 'POST':
        update_player = Player.query.filter_by(id=form.player_dd.data).all()[0]
        update_player.name = form.name.data
        update_player.number = form.number.data
        update_player.email = form.email.data
        update_player.birthdate = datetime(form.birth_year.data,
                                           form.birth_month.data, 
                                           form.birth_day.data, 
                                           0, 0, 0)
        update_player.team_id = form.team_dd.data

        if form.image.data:
            image_file = save_image(form.image.data, str(update_player.id), "players")
            update_player.logo_image = image_file
        db.session.commit()
        return redirect(url_for('admin_players_update'))

    return render_template('admin/players/update.html', form=form, title='Admin Update Players')


@app.route("/admin/players/delete", methods=['GET', 'POST'])
def admin_players_delete():
    form = AdminDeletePlayerForm()
    form.populate_dd()

    players_db = Player.query.all()
    players = [player.jinja_dict() for player in players_db]
    player_choices = [(player['team_id'], player['name']) for player in players]
    form.player_dd.choices = player_choices

    if request.method == 'POST':
        Player.query.filter_by(id=form.player_dd.data).delete()
        db.session.commit()

        return redirect(url_for('admin_players_delete'))

    return render_template('admin/players/delete.html', form=form, title='Admin Delete Players')
