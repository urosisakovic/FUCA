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


@app.route("/admin/matches", methods=['GET', 'POST'])
def admin_matches():
    form = AdminMatchForm()

    teams_db = Team.query.all()
    teams = [team.jinja_dict() for team in teams_db]
    team_choices = [(id, team['name']) for team in teams]

    form.host_team_dd.choices = team_choices
    form.guest_team_dd.choices = team_choices

    if form.validate_on_submit():
        print("Validated")
    else:
        print("Not Validated")

    return render_template('admin/matches.html', form=form, title='Admin Matches')