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


@app.route("/admin/statistics", methods=['GET', 'POST'])
def admin_statistics():
    form = AdminStatsForm()
    if form.validate_on_submit():
        print("Validated")
    else:
        print("Not Validated")

    return render_template('admin/statistics.html', form=form, title='Admin Statistics')
