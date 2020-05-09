from datetime import datetime

from flask import Blueprint, flash, redirect, render_template, request, url_for

from flask_login import current_user, login_required, login_user, logout_user
from fuca import data_utils, dummydata
from fuca.users.forms import LoginForm, RegisterForm
from fuca.models import Match, News, Player, Statistics, Team

main = Blueprint('main', __name__)

@main.route("/")
@main.route("/home")
def home():
    page = request.args.get('page', 1, type=int)
    news = News.query.order_by(News.date.desc()).paginate(page=page, per_page=5)
    return render_template('home/home.html', newslist=news)


@main.route("/results")
def results():
    results = Match.query.filter(Match.date_time < datetime.now()).all()
    for result in results:
        result.host_team_logo = url_for('static', filename='images/teams/{}'.format(result.host_team.logo_image))
        result.guest_team_logo = url_for('static', filename='images/teams/{}'.format(result.guest_team.logo_image))
    return render_template('home/results.html', results=results, title='Results')


@main.route("/schedule")
def schedule():
    schedules = Match.query.filter(Match.date_time >= datetime.now()).all()
    for schedule in schedules:
        schedule.host_team_logo = url_for('static', filename='images/teams/{}'.format(schedule.host_team.logo_image))
        schedule.guest_team_logo = url_for('static', filename='images/teams/{}'.format(schedule.guest_team.logo_image))
    return render_template('home/schedule.html', schedule=schedules, title='Schedule')


@main.route("/player/<int:id>")
def player(id):
    player = Player.query.get(id)
    if not player:
        return "404"
    image_file = url_for('static', filename='images/players/{}'.format(player.image))
    return render_template('home/player.html', player=player, image_file=image_file, title=player.name)


@main.route("/stats")
def stats():
    return render_template('home/stats.html',
                           title='Stats',
                           stats=dummydata.stats,
                           best_player=dummydata.stats_best_player,
                           scorers=dummydata.stats_scorers)


@main.route("/teams")
def teams():
    teams = Team.query.all()
    for team in teams:
        team.logo = url_for('static', filename='images/teams/{}'.format(team.logo_image))
    return render_template('home/teams.html', teams=teams, title='Teams')
