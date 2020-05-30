"""
Author: Djodje Vucinic
"""
from datetime import datetime

from flask import Blueprint, render_template, url_for

from fuca.models import Match, Player, Team

teams = Blueprint('teams', __name__)

@teams.route("/team/<int:id>")
def team(id):
    team = Team.query.get_or_404(id)
    team.image = url_for('static', filename='images/teams/{}'.format(team.logo_image))
    return render_template('team/team.html', team=team, id=id, title=team.name)


@teams.route("/results/<int:id>")
def teamresults(id):
    Team.query.get_or_404(id)
    results = Match.query.filter(Match.date_time <= datetime.now()).filter(Match.guest_team_id == id).all() +\
        Match.query.filter(Match.date_time <= datetime.now()).filter(Match.host_team_id == id).all()
    for result in results:
        result.host_team_logo = url_for('static', filename='images/teams/{}'.format(result.host_team.logo_image))
        result.guest_team_logo = url_for('static', filename='images/teams/{}'.format(result.guest_team.logo_image))
    return render_template('team/team-results.html', results=results, id=id, title='Team Results')


@teams.route("/schedule/<int:id>")
def teamschedule(id):
    Team.query.get_or_404(id)
    schedules = Match.query.filter(Match.date_time >= datetime.now()).filter(Match.guest_team_id == id).all() +\
        Match.query.filter(Match.date_time >= datetime.now()).filter(Match.host_team_id == id).all()
    for schedule in schedules:
        schedule.host_team_logo = url_for('static', filename='images/teams/{}'.format(schedule.host_team.logo_image))
        schedule.guest_team_logo = url_for('static', filename='images/teams/{}'.format(schedule.guest_team.logo_image))
    return render_template('team/team-schedule.html', schedule=schedules, id=id, title='Team Schedule')


@teams.route("/squad/<int:id>")
def teamsquad(id):
    Team.query.get_or_404(id)
    players = Player.query.filter_by(team_id=id).all()
    for player in players:
        player.image = url_for('static', filename='images/players/{}'.format(player.image))
    return render_template('team/team-squad.html', players=players, id=id, title='Team Squad')
