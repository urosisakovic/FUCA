"""
Author: Uros Isakovic
"""
from datetime import datetime

from flask import redirect, render_template, request, url_for, abort, flash

from flask_login import current_user, login_required
from fuca import data_utils
from fuca.admin.matches.forms import (AdminAddMatchForm, AdminDeleteMatchForm,
                                      AdminUpdateMatchForm)
from fuca.models import Match
from flask import Blueprint

matches = Blueprint('matches', __name__)

@matches.route("", methods=['GET', 'POST'])
@login_required
def admin_matches():
    """
    Route reserved for admin access only.
    Used for administration of matches.
    """
    if not current_user.is_admin:
        abort(403)

    return render_template('admin/matches/layout.html', title='Admin Matches')


@matches.route("/add", methods=['GET', 'POST'])
@login_required
def admin_matches_add():
    """
    Route reserved for admin access only.
    Used for adding new matches.
    """
    if not current_user.is_admin:
        abort(403)

    form = AdminAddMatchForm()
    form.populate_dd()

    if request.method == 'POST':
        if form.validate():
            data_utils.add_match(date_time=datetime(int(form.year.data),
                                                    int(form.month.data), 
                                                    int(form.day.data), 
                                                    int(form.hours.data),
                                                    int(form.minutes.data),
                                                    0),
                                host_team_id=form.host_team_dd.data,
                                guest_team_id=form.guest_team_dd.data)
            flash('Successfully added a new match', 'success')
            return redirect(url_for('matches.admin_matches_add'))

    return render_template('admin/matches/add.html', form=form, title='Admin Add Matches')


@matches.route("/update", methods=['GET', 'POST'])
@login_required
def admin_matches_update():
    """
    Route reserved for admin access only.
    Used for updating matches.
    """
    if not current_user.is_admin:
        abort(403)

    form = AdminUpdateMatchForm()
    form.populate_dd()

    match_id = request.args.get('id', type=int)
    if request.method == 'GET' and match_id:
        if match_id >= 0:
            match = Match.query.get(match_id)
            form.match_dd.default = match_id
            form.host_team_dd.default = match.host_team_id
            form.guest_team_dd.default = match.guest_team_id
            form.day.default = match.date_time.day
            form.month.default = match.date_time.month
            form.year.default = match.date_time.year
            form.minutes.default = match.date_time.minute
            form.hours.default = match.date_time.hour
            form.process()
        else:
            form.match_dd.default = 0
            form.host_team_dd.default = 0
            form.guest_team_dd.default = 0
            form.day.default = 1
            form.month.default = 1
            form.year.default = 2020
            form.hours.default = 0
            form.minutes.default = 0
            form.process()

    if request.method == 'POST':
        if form.validate():
            data_utils.update_match(id=form.match_dd.data,
                                    date_time=datetime(int(form.year.data),
                                                    int(form.month.data),
                                                    int(form.day.data),
                                                    int(form.hours.data),
                                                    int(form.minutes.data),
                                                    0),
                                    host_team_id=form.host_team_dd.data,
                                    guest_team_id=form.guest_team_dd.data)
            flash('Successfully updated a match', 'success')
            return redirect(url_for('matches.admin_matches_update'))
        else:
            print(form.errors)

    return render_template('admin/matches/update.html', form=form, title='Admin Update Matches')


@matches.route("/delete", methods=['GET', 'POST'])
@login_required
def admin_matches_delete():
    """
    Route reserved for admin access only.
    Used for deleting matches.
    """
    if not current_user.is_admin:
        abort(403)

    form = AdminDeleteMatchForm()
    form.populate_dd()

    if request.method == 'POST':
        data_utils.delete_match(id=form.match_dd.data)
        flash('Successfully deleted a match', 'success')
        return redirect(url_for('matches.admin_matches_delete'))

    return render_template('admin/matches/delete.html', form=form, title='Admin Delete Matches')
