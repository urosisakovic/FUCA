from datetime import datetime

from flask import redirect, render_template, request, url_for, abort

from flask_login import current_user, login_required
from fuca import data_utils
from fuca.admin.matches.forms import (AdminAddMatchForm, AdminDeleteMatchForm,
                                      AdminUpdateMatchForm)
from fuca.models import Match, Team
from flask import Blueprint

matches = Blueprint('matches', __name__)

@matches.route("", methods=['GET', 'POST'])
@login_required
def admin_matches():
    if not current_user.is_admin:
        abort(403)

    return render_template('admin/matches/layout.html', title='Admin Matches')


@matches.route("/add", methods=['GET', 'POST'])
@login_required
def admin_matches_add():
    if not current_user.is_admin:
        abort(403)

    form = AdminAddMatchForm()
    form.populate_dd()

    if request.method == 'POST':
        data_utils.add_match(date_time=datetime(int(form.year.data),
                                                int(form.month.data), 
                                                int(form.day.data), 
                                                0, 0, 0),
                             host_team_id=form.host_team_dd.data,
                             guest_team_id=form.guest_team_dd.data)
        return redirect(url_for('matches.admin_matches_add'))

    return render_template('admin/matches/add.html', form=form, title='Admin Add Matches')


@matches.route("/update", methods=['GET', 'POST'])
@login_required
def admin_matches_update():
    if not current_user.is_admin:
        abort(403)

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
        return redirect(url_for('matches.admin_matches_update'))

    return render_template('admin/matches/update.html', form=form, title='Admin Update Matches')


@matches.route("/delete", methods=['GET', 'POST'])
@login_required
def admin_matches_delete():
    if not current_user.is_admin:
        abort(403)

    form = AdminDeleteMatchForm()
    form.populate_dd()

    if request.method == 'POST':
        data_utils.delete_match(id=form.match_dd.data)
        return redirect(url_for('matches.admin_matches_delete'))

    return render_template('admin/matches/delete.html', form=form, title='Admin Delete Matches')
