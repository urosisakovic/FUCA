from datetime import datetime
from flask import redirect, render_template, request, url_for

from fuca import app, data_utils
from fuca.forms import (AdminAddMatchForm, AdminDeleteMatchForm,
                        AdminUpdateMatchForm)
from fuca.models import Match, Team


@app.route("/admin/matches", methods=['GET', 'POST'])
def admin_matches():
    return render_template('admin/matches/layout.html', title='Admin Matches')


@app.route("/admin/matches/add", methods=['GET', 'POST'])
def admin_matches_add():
    form = AdminAddMatchForm()
    form.populate_dd()

    if request.method == 'POST':
        data_utils.add_match(date_time=datetime(int(form.year.data),
                                                int(form.month.data), 
                                                int(form.day.data), 
                                                0, 0, 0),
                             host_team_id=form.host_team_dd.data,
                             guest_team_id=form.guest_team_dd.data)
        return redirect(url_for('admin_matches_add'))

    return render_template('admin/matches/add.html', form=form, title='Admin Add Matches')


@app.route("/admin/matches/update", methods=['GET', 'POST'])
def admin_matches_update():
    form = AdminUpdateMatchForm()
    form.populate_dd()

    if request.method == 'POST':
        data_utils.update_match(id=form.match_dd.data,
                                date_time=datetime(int(form.year.data),
                                                   int(form.month.data),
                                                   int(form.day.data),
                                                   0, 0, 0),
                                host_team_id=form.host_team_dd.data,
                                guest_team_id=form.guest_team_dd.data)
        return redirect(url_for('admin_matches_update'))

    return render_template('admin/matches/update.html', form=form, title='Admin Update Matches')


@app.route("/admin/matches/delete", methods=['GET', 'POST'])
def admin_matches_delete():
    form = AdminDeleteMatchForm()
    form.populate_dd()

    if request.method == 'POST':
        data_utils.delete_match(id=form.match_dd.data)
        return redirect(url_for('admin_matches_delete'))

    return render_template('admin/matches/delete.html', form=form, title='Admin Delete Matches')
