import os
from datetime import datetime

from flask import flash, redirect, render_template, url_for

from fuca import app, db
from fuca.forms import (AdminMatchForm, AdminNewsForm, AdminPlayerForm,
                        AdminResultForm, AdminStatsForm, AdminTeamForm,
                        LoginForm)
from fuca.models import Match, News, Player, Statistics, Team


@app.route("/admin/news", methods=['GET', 'POST'])
def admin_news():
    form = AdminNewsForm()
    if form.validate_on_submit():
        newNews = News(title=form.title.data,
                       content=form.content.data)
        db.session.add(newNews)
        db.session.commit()

    return render_template('admin/admin-news.html', form=form, title='Admin News')


#TODO: Set image filename. 
def save_image(form_image, image_name, team_player):
    _, f_ext = os.path.splitext(form_image.filename)
    image_fn = image_name + f_ext
    image_path = os.path.join(app.root_path, 'static/images/{}/{}'.format(team_player, image_fn))
    form_image.save(image_path)
    return image_fn


#TODO: Check for unique team name.
@app.route("/admin/teams", methods=['GET', 'POST'])
def admin_teams():
    form = AdminTeamForm()
    if form.validate_on_submit():
        newTeam = Team(name=form.name.data)
        db.session.add(newTeam)
        db.session.commit()

        if form.image.data:
            image_file = save_image(form.image.data, str(newTeam.id), "teams")

        newTeam.logo_image = image_file
        db.session.commit()

    return render_template('admin/admin-teams.html', form=form, title='Admin Teams')


@app.route("/admin/players", methods=['GET', 'POST'])
def admin_players():
    form = AdminPlayerForm()
    if form.validate_on_submit():
        print("Validated")
    else:
        print("Not Validated")

    return render_template('admin/admin-players.html', form=form, title='Admin Players')


@app.route("/admin/matches", methods=['GET', 'POST'])
def admin_matches():
    form = AdminMatchForm()
    if form.validate_on_submit():
        print("Validated")
    else:
        print("Not Validated")

    return render_template('admin/admin-matches.html', form=form, title='Admin Matches')


@app.route("/admin/results", methods=['GET', 'POST'])
def admin_results():
    form = AdminResultForm()
    if form.validate_on_submit():
        print("Validated")
    else:
        print("Not Validated")

    return render_template('admin/admin-results.html', form=form, title='Admin Results')


@app.route("/admin/statistics", methods=['GET', 'POST'])
def admin_statistics():
    form = AdminStatsForm()
    if form.validate_on_submit():
        print("Validated")
    else:
        print("Not Validated")

    return render_template('admin/admin-statistics.html', form=form, title='Admin Statistics')
