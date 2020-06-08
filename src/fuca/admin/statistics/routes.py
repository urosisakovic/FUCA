"""
Author: Uros Isakovic
"""
from flask import redirect, render_template, request, url_for, abort, flash

from flask_login import current_user, login_required
from fuca import data_utils
from fuca.admin.statistics.forms import (AdminAddStatisticsForm, AdminDeleteStatisticsForm,
                                         AdminUpdateStatisticsForm)
from fuca.models import Match, Player
from flask import Blueprint

statistics = Blueprint('statistics', __name__)

@statistics.route("", methods=['GET', 'POST'])
@login_required
def admin_statistics():
    """
    Route reserved for admin access only.
    Used for administration of statistics.
    """
    if not current_user.is_admin:
        abort(403)

    return render_template('admin/statistics/layout.html', title='Admin Statistics')


@statistics.route("/add", methods=['GET', 'POST'])
@login_required
def admin_statistics_add():
    """
    Route reserved for admin access only.
    Used for adding statistics.
    """
    if not current_user.is_admin:
        abort(403)

    form = AdminAddStatisticsForm()
    form.populate_dd()

    match_id = request.args.get('match_id', type=int)
    if request.method == 'GET' and match_id:
        if match_id >= 0:
            match = Match.query.get(match_id)
            form.match_dd.default = match_id
            players = Player.query.filter_by(team_id=match.host_team_id).all() + \
                Player.query.filter_by(team_id=match.guest_team_id).all()
            form.player_dd.choices = [(-1, '')] + [(player.id, '{} [{}]'.format(player.name, player.team.name)) for player in players]

            form.process()
    
    if request.method == 'POST':
        data_utils.add_statistics(match_id=form.match_dd.data,
                                    player_id=form.player_dd.data,
                                    goals=form.goals.data,
                                    assists=form.assists.data,
                                    yellow=form.yellow.data,
                                    red=form.red.data)
        flash('Successfully added a new statistics', 'success')
        return redirect(url_for('statistics.admin_statistics_add'))
    else:
        print(form.errors)

    return render_template('admin/statistics/add.html', form=form, title='Admin Add Statistics')


@statistics.route("/update", methods=['GET', 'POST'])
@login_required
def admin_statistics_update():
    """
    Route reserved for admin access only.
    Used for updating statistics.
    """
    if not current_user.is_admin:
        abort(403)

    form = AdminUpdateStatisticsForm()
    form.populate_dd()

    match_id = request.args.get('match_id', type=int)
    if request.method == 'GET' and match_id:
        if match_id >= 0:
            match = Match.query.get(match_id)
            form.match_dd.default = match_id
            players = Player.query.filter_by(team_id=match.host_team_id).all() + \
                Player.query.filter_by(team_id=match.guest_team_id).all()
            form.player_dd.choices = [(-1, '')] + [(player.id, '{} [{}]'.format(player.name, player.team.name)) for player in players]
            form.process()
        else:
            form.match_dd.default = 0
            form.player_dd.default = 0
            form.process()
        
    
    if request.method == 'POST':
        data_utils.update_statistics(match_id=form.match_dd.data,
                                    player_id=form.player_dd.data,
                                    goals=form.goals.data,
                                    assists=form.assists.data,
                                    yellow=form.yellow.data,
                                    red=form.red.data)
        flash('Successfully updated a statistics', 'success')
        return redirect(url_for('statistics.admin_statistics_update'))

    return render_template('admin/statistics/update.html', form=form, title='Admin Update Statistics')


@statistics.route("/remove", methods=['GET', 'POST'])
@login_required
def admin_statistics_delete():
    """
    Route reserved for admin access only.
    Used for deleting statistics.
    """
    if not current_user.is_admin:
        abort(403)
        
    form = AdminDeleteStatisticsForm()
    form.populate_dd()

    match_id = request.args.get('match_id', type=int)
    if request.method == 'GET' and match_id:
        if match_id >= 0:
            match = Match.query.get(match_id)
            form.match_dd.default = match_id
            players = Player.query.filter_by(team_id=match.host_team_id).all() + \
                Player.query.filter_by(team_id=match.guest_team_id).all()
            form.player_dd.choices = [(-1, '')] + [(player.id, '{} [{}]'.format(player.name, player.team.name)) for player in players]
            form.process()
        else:
            form.match_dd.default = 0
            form.player_dd.default = 0
            form.process()
    
    if request.method == 'POST':
        data_utils.delete_statistics(match_id=form.match_dd.data,
                                     player_id=form.player_dd.data)
        flash('Successfully deleted a statistics', 'success')
        return redirect(url_for('statistics.admin_statistics_delete'))

    return render_template('admin/statistics/delete.html', form=form, title='Admin Delete Statistics')
