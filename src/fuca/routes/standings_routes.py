from datetime import datetime

from flask import flash, redirect, render_template, url_for

from fuca import app, dummydata
from fuca.models import Match, News, Player, Statistics, Team

@app.route("/standings")
def standings():
    teams_db = Team.query.all()
    teams = [team.jinja_dict() for team in teams_db]
    teams = sorted(teams, key=lambda team: team['points'])
    return render_template('standings/standings.html', teams=teams, title='Standings')


@app.route("/bestplayers")
def bestplayers():
    players_db = Player.query.all()
    players = [player.jinja_dict() for player in players_db]
    players = sorted(players, key=lambda player: player['points'])
    players = reversed(players)
    return render_template('standings/best-players.html', players=players, title='Best Players')


@app.route("/bestscorers")
def bestscorers():
    players_db = Player.query.all()
    players = [player.jinja_dict() for player in players_db]
    players = sorted(players, key=lambda player: player['goals'])
    players = reversed(players)
    return render_template('standings/best-scorers.html', players=players, title='Best Scorers')