from datetime import datetime

from flask import flash, redirect, render_template, url_for

from fuca import app, dummydata
from fuca.forms import (AdminMatchForm, AdminNewsForm, AdminPlayerForm,
                        AdminResultForm, AdminStatsForm, AdminTeamForm,
                        LoginForm)
from fuca.models import Match, News, Player, Statistics, Team


@app.route("/admin/news", methods=['GET', 'POST'])
def admin_news():
    form = AdminNewsForm()
    if form.validate_on_submit():
        print("Validated")
    else:
        print("Not Validated")

    return render_template('admin/admin-news.html', form=form, title='Admin News')


@app.route("/admin/teams", methods=['GET', 'POST'])
def admin_teams():
    form = AdminTeamForm()
    if form.validate_on_submit():
        print("Validated")
    else:
        print("Not Validated")

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