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


@app.route("/admin/results", methods=['GET', 'POST'])
def admin_results():
    form = AdminResultForm()

    matches_db = Match.query.all()
    matches = [match.jinja_dict() for match in matches_db]
    match_choices = [(match['id'], match['team1_name'] + ' - ' + match['team2_name']) for match in matches]
    form.match_dd.choices = match_choices

    if form.validate_on_submit():
        print("Validated")
    else:
        print("Not Validated")

    return render_template('admin/results.html', form=form, title='Admin Results')