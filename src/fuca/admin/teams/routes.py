
"""
Author: Uros Isakovic
"""
from flask import redirect, render_template, request, url_for, abort, flash

from flask_login import current_user, login_required
from fuca import data_utils
from fuca.admin.teams.forms import (AdminAddTeamForm, AdminDeleteTeamForm,
                                    AdminUpdateTeamForm)
from fuca.models import Team
from flask import Blueprint

adminteams = Blueprint('adminteams', __name__)

@adminteams.route("/", methods=['GET', 'POST'])
@login_required
def admin_teams():
    """
    Route reserved for admin access only.
    Used for administration of teams.
    """
    if not current_user.is_admin:
        abort(403)

    return render_template('admin/teams/layout.html', title='Admin Teams')


@adminteams.route("/add", methods=['GET', 'POST'])
@login_required
def admin_teams_add():
    """
    Route reserved for admin access only.
    Used for adding teams.
    """
    if not current_user.is_admin:
        abort(403)

    form = AdminAddTeamForm()
    form.populate_dd()
    
    if request.method == 'POST':
        if form.validate():
            data_utils.add_team(name=form.name.data,
                                image=form.image.data)
            flash('Successfully added a new team', 'success')
            return redirect(url_for('adminteams.admin_teams_add'))

    return render_template('admin/teams/add.html', form=form, title='Admin Add Teams')


@adminteams.route("/update", methods=['GET', 'POST'])
@login_required
def admin_teams_update():
    """
    Route reserved for admin access only.
    Used for updating teams.
    """
    if not current_user.is_admin:
        abort(403)

    form = AdminUpdateTeamForm()
    form.populate_dd()

    team_id = request.args.get('id', type=int)
    if request.method == 'GET' and team_id:
        if team_id >= 0:
            team = Team.query.get(team_id)
            form.teams_dd.default = team_id
            form.process()
            form.name.data = team.name
        else:
            form.news_dd.default = 0
            form.process()
            form.name.data = ''

    if request.method == 'POST':
        if form.validate():
            data_utils.update_team(id=form.teams_dd.data,
                                   name=form.name.data,
                                   image=form.image.data)
            flash('Successfully updated a team', 'success')
            return redirect(url_for('adminteams.admin_teams_update'))

    return render_template('admin/teams/update.html', form=form, title='Admin Update Teams')


@adminteams.route("/delete", methods=['GET', 'POST'])
@login_required
def admin_teams_delete():
    """
    Route reserved for admin access only.
    Used for deleting teams.
    """
    if not current_user.is_admin:
        abort(403)

    form = AdminDeleteTeamForm()
    form.populate_dd()

    if request.method == 'POST':
        data_utils.delete_team(id=form.teams_dd.data)
        flash('Successfully deleted a team', 'success')
        return redirect(url_for('adminteams.admin_teams_delete'))

    return render_template('admin/teams/delete.html', form=form, title='Admin Delete Teams')
