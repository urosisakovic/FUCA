from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, url_for

from fuca import dummydata
from fuca.models import Match, News, Player, Statistics, Team

scores = Blueprint('standings', __name__)

@scores.route("/")
def standings():
    teams_db = Team.query.all()
    teams = [team.jinja_dict() for team in teams_db]
    teams = sorted(teams, key=lambda team: team['points'])[::-1]
    for team in teams:
        team['logo'] = url_for('static', filename='images/teams/{}'.format(team['logo']))

    return render_template('standings/standings.html', teams=teams, title='Standings')


@scores.route("/bestplayers")
def bestplayers():
    players_db = Player.query.filter_by(is_admin=False).all()
    players = [player.jinja_dict() for player in players_db]
    players = sorted(players, key=lambda player: player['points'])[::-1]
    for player in players:
        player['image'] = url_for('static', filename='images/players/{}'.format(player['image']))
        player['team_id'] = player['team'].id
        player['team_name'] = player['team'].name
        player['team_logo'] = url_for('static', filename='images/teams/{}'.format(player['team'].logo_image))

    return render_template('standings/best-players.html', players=players, title='Best Players')


@scores.route("/bestscorers")
def bestscorers():
    players_db = Player.query.filter_by(is_admin=False).all()
    players = [player.jinja_dict() for player in players_db]
    players = sorted(players, key=lambda player: player['goals'])[::-1]
    for player in players:
        player['image'] = url_for('static', filename='images/players/{}'.format(player['image']))
        player['team_id'] = player['team'].id
        player['team_name'] = player['team'].name
        player['team_logo'] = url_for('static', filename='images/teams/{}'.format(player['team'].logo_image))

    return render_template('standings/best-scorers.html', players=players, title='Best Scorers')
