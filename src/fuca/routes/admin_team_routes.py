import os
from datetime import datetime

from flask import flash, redirect, render_template, request, url_for

from fuca import app, data_utils
from fuca.forms import (AdminAddTeamForm, AdminDeleteTeamForm,
                        AdminUpdateTeamForm)
from fuca.models import Team


@app.route("/admin/teams", methods=['GET', 'POST'])
def admin_teams():
    return render_template('admin/teams/layout.html', title='Admin Teams')


@app.route("/admin/teams/add", methods=['GET', 'POST'])
def admin_teams_add():
    form = AdminAddTeamForm()
    form.populate_dd()
    
    if request.method == 'POST':
        data_utils.add_team(name=form.name.data,
                            image=form.image.data)
        return redirect(url_for('admin_teams_add'))

    return render_template('admin/teams/add.html', form=form, title='Admin Add Teams')


@app.route("/admin/teams/update", methods=['GET', 'POST'])
def admin_teams_update():
    form = AdminUpdateTeamForm()
    form.populate_dd()

    if request.method == 'POST':
        data_utils.update_team(id=form.teams_dd.data,
                                name=form.name.data,
                                image=form.image.data)
        return redirect(url_for('admin_teams_update'))

    return render_template('admin/teams/update.html', form=form, title='Admin Update Teams')


@app.route("/admin/teams/delete", methods=['GET', 'POST'])
def admin_teams_delete():
    form = AdminDeleteTeamForm()
    form.populate_dd()

    if request.method == 'POST':
        data_utils.delete_team(id=form.teams_dd.data)
        return redirect(url_for('admin_teams_delete'))

    return render_template('admin/teams/delete.html', form=form, title='Admin Delete Teams')
