from flask import redirect, render_template, request, url_for

from fuca import app, data_utils
from fuca.forms import (AdminAddResultForm, AdminDeleteResultForm,
                        AdminUpdateResultForm)
from fuca.models import Match


@app.route("/admin/results", methods=['GET', 'POST'])
def admin_results():
    return render_template('admin/results/layout.html', title='Admin Results')


@app.route("/admin/results/add", methods=['GET', 'POST'])
def admin_results_add():
    form = AdminAddResultForm()
    form.populate_dd()

    if request.method == 'POST':
        data_utils.add_result(id=form.match_dd.data, 
                              host_team_goals=form.host_team_goals.data,
                              host_team_yellow=form.host_team_yellow.data,
                              host_team_red=form.host_team_red.data,
                              host_team_shots=form.host_team_shots.data, 
                              guest_team_goals=form.guest_team_goals.data,
                              guest_team_yellow=form.guest_team_yellow.data,
                              guest_team_red=form.guest_team_red.data,
                              guest_team_shots=form.guest_team_shots.data)
        return redirect(url_for('admin_result_add'))

    return render_template('admin/results/add.html', form=form, title='Admin Add Results')


@app.route("/admin/results/update", methods=['GET', 'POST'])
def admin_results_update():
    form = AdminUpdateResultForm()
    form.populate_dd()

    if request.method == 'POST':
        data_utils.update_result(id=form.match_dd.data, 
                                 host_team_goals=form.host_team_goals.data,
                                 host_team_yellow=form.host_team_yellow.data,
                                 host_team_red=form.host_team_red.data,
                                 host_team_shots=form.host_team_shots.data, 
                                 guest_team_goals=form.guest_team_goals.data,
                                 guest_team_yellow=form.guest_team_yellow.data,
                                 guest_team_red=form.guest_team_red.data,
                                 guest_team_shots=form.guest_team_shots.data)
        return redirect(url_for('admin_result_update'))

    return render_template('admin/results/update.html', form=form, title='Admin Update Results')


@app.route("/admin/results/delete", methods=['GET', 'POST'])
def admin_results_delete():
    form = AdminDeleteResultForm()
    form.populate_dd()

    if request.method == 'POST':
        data_utils.delete_result(id=form.match_dd.data)
        return redirect(url_for('admin_result_delete'))

    return render_template('admin/results/delete.html', form=form, title='Admin Delete Results')