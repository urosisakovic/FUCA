from datetime import datetime

from flask import flash, redirect, render_template, url_for

from fuca import app, dummydata
from fuca.models import Match, News, Player, Statistics, Team


@app.route("/team/<int:id>")
def team(id):
    team = Team.query.get(id)
    if not team:
        return "404"
    team = team.jinja_dict()

    image_file = url_for('static', filename='images/teams/{}'.format(team['logo']))

    return render_template('team/team.html', team=team, id=id, title=team['name'], image_file=image_file)


#TODO: Add team name in title.
#TODO: Adress invalid id.
@app.route("/teamresults/<int:id>")
def teamresults(id):
    results_db = Match.query.filter(Match.date_time <= datetime.now()).filter(Match.guest_team_id == id).all() +\
        Match.query.filter(Match.date_time <= datetime.now()).filter(Match.host_team_id == id).all()
    results_list = [result.jinja_dict() for result in results_db]
    return render_template('team/team-results.html', results=results_list, id=id, title='Team Results')


#TODO: Add team name in title.
#TODO: Adress invalid id.
@app.route("/teamschedule/<int:id>")
def teamschedule(id):
    schedule_db = Match.query.filter(Match.date_time >= datetime.now()).filter(Match.guest_team_id == id).all() +\
        Match.query.filter(Match.date_time >= datetime.now()).filter(Match.host_team_id == id).all()
    schedule_list = [schedule.jinja_dict() for schedule in schedule_db]
    return render_template('team/team-schedule.html', schedule=schedule_list, id=id, title='Team Schedule')


#TODO: Add team name in title.
#TODO: Address invalid id.
@app.route("/teamsquad/<int:id>")
def teamsquad(id):
    players_db = Player.query.filter(Player.team_id == id).all()
    players = [player.jinja_dict() for player in players_db]
    return render_template('team/team-squad.html', players=players, id=id, title='Team Squad')