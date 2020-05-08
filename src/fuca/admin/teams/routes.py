import os
from datetime import datetime

from flask import flash, redirect, render_template, request, url_for

from flask_login import current_user, login_required
from fuca import app, data_utils
from fuca.admin.teams.forms import (AdminAddTeamForm, AdminDeleteTeamForm,
                                    AdminUpdateTeamForm)
from fuca.models import Team
from flask import Blueprint

adminteams = Blueprint('adminteams', __name__)

@adminteams.route("/admin/teams", methods=['GET', 'POST'])
@login_required
def admin_teams():
    if not current_user.is_admin:
        return "Access forbiden"

    return render_template('admin/teams/layout.html', title='Admin Teams')


@adminteams.route("/admin/teams/add", methods=['GET', 'POST'])
@login_required
def admin_teams_add():
    if not current_user.is_admin:
        return "Access forbiden"

    form = AdminAddTeamForm()
    form.populate_dd()
    
    if request.method == 'POST':
        data_utils.add_team(name=form.name.data,
                            image=form.image.data)
        return redirect(url_for('teams.admin_teams_add'))

    return render_template('admin/teams/add.html', form=form, title='Admin Add Teams')


@adminteams.route("/admin/teams/update", methods=['GET', 'POST'])
@login_required
def admin_teams_update():
    if not current_user.is_admin:
        return "Access forbiden"

    form = AdminUpdateTeamForm()
    form.populate_dd()

    if request.method == 'POST':
        data_utils.update_team(id=form.teams_dd.data,
                                name=form.name.data,
                                image=form.image.data)
        return redirect(url_for('teams.admin_teams_update'))

    return render_template('admin/teams/update.html', form=form, title='Admin Update Teams')


@adminteams.route("/admin/teams/delete", methods=['GET', 'POST'])
@login_required
def admin_teams_delete():
    if not current_user.is_admin:
        return "Access forbiden"

    form = AdminDeleteTeamForm()
    form.populate_dd()

    if request.method == 'POST':
        data_utils.delete_team(id=form.teams_dd.data)
        return redirect(url_for('teams.admin_teams_delete'))

    return render_template('admin/teams/delete.html', form=form, title='Admin Delete Teams')
