import os
from datetime import datetime

from flask import flash, redirect, render_template, request, url_for

from fuca import app, db
from fuca.forms import (AdminAddTeamForm, AdminDeleteTeamForm,
                        AdminUpdateTeamForm)
from fuca.models import Team


def save_image(form_image, image_name, team_player):
    _, f_ext = os.path.splitext(form_image.filename)
    image_fn = image_name + f_ext
    image_path = os.path.join(app.root_path, 'static/images/{}/{}'.format(team_player, image_fn))
    form_image.save(image_path)
    return image_fn


#TODO: Check for unique team name.
@app.route("/admin/teams", methods=['GET', 'POST'])
def admin_teams():
    return render_template('admin/teams/layout.html', title='Admin Teams')


@app.route("/admin/teams/add", methods=['GET', 'POST'])
def admin_teams_add():
    form = AdminAddTeamForm()
    form.populate_dd()
    
    if form.validate_on_submit():
        new_team = Team(name=form.name.data)
        db.session.add(new_team)
        db.session.commit()

        if form.image.data:
            image_file = save_image(form.image.data, str(new_team.id), "teams")
            new_team.logo_image = image_file

        db.session.commit()

        return redirect(url_for('admin_teams_add'))

    return render_template('admin/teams/add.html', form=form, title='Admin Add Teams')


@app.route("/admin/teams/update", methods=['GET', 'POST'])
def admin_teams_update():
    form = AdminUpdateTeamForm()
    form.populate_dd()

    if request.method == 'POST':
        update_team = Team.query.filter_by(id=form.teams_dd.data).all()[0]
        update_team.name = form.name.data
        if form.image.data:
            image_file = save_image(form.image.data, str(update_team.id), "teams")
            update_team.logo_image = image_file
        db.session.commit()
        return redirect(url_for('admin_teams_update'))

    return render_template('admin/teams/update.html', form=form, title='Admin Update Teams')


@app.route("/admin/teams/delete", methods=['GET', 'POST'])
def admin_teams_delete():
    form = AdminDeleteTeamForm()
    form.populate_dd()

    if request.method == 'POST':
        Team.query.filter_by(id=form.teams_dd.data).delete()
        db.session.commit()

        return redirect(url_for('admin_teams_delete'))

    return render_template('admin/teams/delete.html', form=form, title='Admin Delete Teams')
