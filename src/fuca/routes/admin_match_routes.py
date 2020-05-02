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
        data_utils.add_match()

    return render_template('admin/matches/add.html', form=form, title='Admin Add Matches')


@app.route("/admin/matches/update", methods=['GET', 'POST'])
def admin_matches_update():
    form = AdminUpdateMatchForm()
    form.populate_dd()

    if request.method == 'POST':
        data_utils.update_match()

    return render_template('admin/matches/update.html', form=form, title='Admin Update Matches')


@app.route("/admin/matches/delete", methods=['GET', 'POST'])
def admin_matches_delete():
    form = AdminDeleteMatchForm()
    form.populate_dd()

    if request.method == 'POST':
        data_utils.delete_match()

    return render_template('admin/matches/delete.html', form=form, title='Admin Delete Matches')
