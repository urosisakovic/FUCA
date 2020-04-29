from datetime import datetime

from flask import flash, redirect, render_template, url_for

from fuca import app, dummydata
from fuca.forms import (AdminMatchForm, AdminNewsForm, AdminPlayerForm,
                        AdminResultForm, AdminStatsForm, AdminTeamForm,
                        LoginForm)
from fuca.models import Match, News, Player, Statistics, Team


# TODO: Change endpoint to admin/news.
@app.route("/adminnews", methods=['GET', 'POST'])
def adminnews():
    form = AdminNewsForm()
    if form.validate_on_submit():
        print("Validated")
    else:
        print("Not Validated")

    return render_template('admin/admin-news.html', form=form, title='Admin News')


# TODO: Change endpoint to admin/teams.
@app.route("/adminteams", methods=['GET', 'POST'])
def adminteams():
    form = AdminTeamForm()
    if form.validate_on_submit():
        print("Validated")
    else:
        print("Not Validated")

    return render_template('admin/admin-teams.html', form=form, title='Admin Teams')


# TODO: Change endpoint to admin/players.
@app.route("/adminplayers", methods=['GET', 'POST'])
def adminplayers():
    form = AdminPlayerForm()
    if form.validate_on_submit():
        print("Validated")
    else:
        print("Not Validated")

    return render_template('admin/admin-players.html', form=form, title='Admin Players')


# TODO: Change endpoint to admin/adminmatches.
@app.route("/adminmatches", methods=['GET', 'POST'])
def adminmatches():
    form = AdminMatchForm()
    if form.validate_on_submit():
        print("Validated")
    else:
        print("Not Validated")

    return render_template('admin/admin-matches.html', form=form, title='Admin Matches')


# TODO: Change endpoint to admin/results.
@app.route("/adminresults", methods=['GET', 'POST'])
def adminresults():
    form = AdminResultForm()
    if form.validate_on_submit():
        print("Validated")
    else:
        print("Not Validated")

    return render_template('admin/admin-results.html', form=form, title='Admin Results')


# TODO: Change endpoint to admin/statistics.
@app.route("/adminstatistics", methods=['GET', 'POST'])
def adminstatistics():
    form = AdminStatsForm()
    if form.validate_on_submit():
        print("Validated")
    else:
        print("Not Validated")

    return render_template('admin/admin-statistics.html', form=form, title='Admin Statistics')