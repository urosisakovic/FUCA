"""
Author: Uros Isakovic
"""
from flask import redirect, render_template, request, url_for, abort, flash

from flask_login import current_user, login_required
from fuca import data_utils
from fuca.admin.results.forms import (AdminAddResultForm, AdminDeleteResultForm,
                        AdminUpdateResultForm)
from fuca.models import Match
from flask import Blueprint

results = Blueprint('results', __name__)

@results.route("/", methods=['GET', 'POST'])
@login_required
def admin_results():
    if not current_user.is_admin:
        abort(403)
    return render_template('admin/results/layout.html', title='Admin Results')


@results.route("/add", methods=['GET', 'POST'])
@login_required
def admin_results_add():
    if not current_user.is_admin:
        abort(403)

    form = AdminAddResultForm()
    form.populate_dd()

    if request.method == 'POST':
        if form.validate():
            data_utils.add_result(id=form.match_dd.data, 
                                host_team_goals=form.host_team_goals.data,
                                host_team_yellow=form.host_team_yellow.data,
                                host_team_red=form.host_team_red.data,
                                host_team_shots=form.host_team_shots.data, 
                                guest_team_goals=form.guest_team_goals.data,
                                guest_team_yellow=form.guest_team_yellow.data,
                                guest_team_red=form.guest_team_red.data,
                                guest_team_shots=form.guest_team_shots.data)
            flash('Successfully added a new result', 'success')
            return redirect(url_for('results.admin_results_add'))

    return render_template('admin/results/add.html', form=form, title='Admin Add Results')


@results.route("/update", methods=['GET', 'POST'])
@login_required
def admin_results_update():
    if not current_user.is_admin:
        abort(403)

    form = AdminUpdateResultForm()
    form.populate_dd()

    result_id = request.args.get('id', type=int)
    if request.method == 'GET' and result_id:
        if result_id >= 0:
            match = Match.query.get(result_id)
            form.match_dd.default = result_id
            form.process()

            form.host_team_goals.data = match.host_team_goals
            form.host_team_yellow.data = match.host_team_yellow
            form.host_team_red.data = match.host_team_red
            form.host_team_shots.data = match.host_team_shots
            
            form.guest_team_goals.data = match.guest_team_goals
            form.guest_team_yellow.data = match.guest_team_yellow
            form.guest_team_red.data = match.guest_team_red
            form.guest_team_shots.data = match.guest_team_shots            
        else:
            form.match_dd.default = 0
            form.process()

            form.host_team_goals.data = ''
            form.host_team_yellow.data = ''
            form.host_team_red.data = ''
            form.host_team_shots.data = ''
            
            form.guest_team_goals.data = ''
            form.guest_team_yellow.data = ''
            form.guest_team_red.data = ''
            form.guest_team_shots.data = ''

    if request.method == 'POST':
        if form.validate():
            data_utils.update_result(id=form.match_dd.data, 
                                    host_team_goals=form.host_team_goals.data,
                                    host_team_yellow=form.host_team_yellow.data,
                                    host_team_red=form.host_team_red.data,
                                    host_team_shots=form.host_team_shots.data, 
                                    guest_team_goals=form.guest_team_goals.data,
                                    guest_team_yellow=form.guest_team_yellow.data,
                                    guest_team_red=form.guest_team_red.data,
                                    guest_team_shots=form.guest_team_shots.data)
            flash('Successfully updated a result', 'success')
            return redirect(url_for('results.admin_results_update'))

    return render_template('admin/results/update.html', form=form, title='Admin Update Results')


@results.route("/delete", methods=['GET', 'POST'])
@login_required
def admin_results_delete():
    if not current_user.is_admin:
        abort(403)

    form = AdminDeleteResultForm()
    form.populate_dd()

    if request.method == 'POST':
        data_utils.delete_result(id=form.match_dd.data)
        flash('Successfully deleted a result', 'success')
        return redirect(url_for('results.admin_results_delete'))

    return render_template('admin/results/delete.html', form=form, title='Admin Delete Results')
