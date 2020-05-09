from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, url_for

from fuca import dummydata
from fuca.models import Match, News, Player, Statistics, Team

teams = Blueprint('teams', __name__)

@teams.route("/team/<int:id>")
def team(id):
    team = Team.query.get(id)
    if not team:
        return "404"
    image_file = url_for('static', filename='images/teams/{}'.format(team.logo_image))
    return render_template('team/team.html', team=team, id=id, title=team.name, image_file=image_file)


#TODO: Add team name in title.
#TODO: Adress invalid id.
@teams.route("/results/<int:id>")
def teamresults(id):
    results = Match.query.filter(Match.date_time <= datetime.now()).filter(Match.guest_team_id == id).all() +\
        Match.query.filter(Match.date_time <= datetime.now()).filter(Match.host_team_id == id).all()
    for result in results:
        result.host_team_logo = url_for('static', filename='images/teams/{}'.format(result.host_team.logo_image))
        result.guest_team_logo = url_for('static', filename='images/teams/{}'.format(result.guest_team.logo_image))
    return render_template('team/team-results.html', results=results, id=id, title='Team Results')


#TODO: Add team name in title.
#TODO: Adress invalid id.
@teams.route("/schedule/<int:id>")
def teamschedule(id):
    schedules = Match.query.filter(Match.date_time >= datetime.now()).filter(Match.guest_team_id == id).all() +\
        Match.query.filter(Match.date_time >= datetime.now()).filter(Match.host_team_id == id).all()
    for schedule in schedules:
        schedule.host_team_logo = url_for('static', filename='images/teams/{}'.format(schedule.host_team.logo_image))
        schedule.guest_team_logo = url_for('static', filename='images/teams/{}'.format(schedule.guest_team.logo_image))
    return render_template('team/team-schedule.html', schedule=schedules, id=id, title='Team Schedule')


#TODO: Add team name in title.
#TODO: Address invalid id.
@teams.route("/squad/<int:id>")
def teamsquad(id):
    players = Player.query.filter_by(team_id=id).all()
    for player in players:
        player.image = url_for('static', filename='images/players/{}'.format(player.image))
    return render_template('team/team-squad.html', players=players, id=id, title='Team Squad')
