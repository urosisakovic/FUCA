from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, url_for

from fuca import dummydata
from fuca.models import Match, News, Player, Statistics, Team

scores = Blueprint('standings', __name__)

@scores.route("/")
def standings():
    teams = Team.query.all()
    teams = list(reversed(sorted(teams, key=lambda team: team.points)))
    for team in teams:
        team.logo = url_for('static', filename='images/teams/{}'.format(team.logo_image))

    return render_template('standings/standings.html', teams=teams, title='Standings')


@scores.route("/bestplayers")
def bestplayers():
    players = Player.query.filter_by(is_admin=False).all()
    players = list(reversed(sorted(players, key=lambda player: player.points)))
    for player in players:
        player.image = url_for('static', filename='images/players/{}'.format(player.image))
        player.team_name = player.team.name
        player.team_logo = url_for('static', filename='images/teams/{}'.format(player.team.logo_image))

    return render_template('standings/best-players.html', players=players, title='Best Players')


@scores.route("/bestscorers")
def bestscorers():
    players = Player.query.filter_by(is_admin=False).all()
    players = list(reversed(sorted(players, key=lambda player: player.goals)))
    for player in players:
        player.image = url_for('static', filename='images/players/{}'.format(player.image))
        player.team_name = player.team.name
        player.team_logo = url_for('static', filename='images/teams/{}'.format(player.team.logo_image))

    return render_template('standings/best-scorers.html', players=players, title='Best Scorers')
