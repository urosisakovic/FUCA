from datetime import datetime

from flask import flash, redirect, render_template, url_for

from fuca import app, dummydata
from fuca.forms import (AdminMatchForm, AdminNewsForm, AdminPlayerForm,
                        AdminResultForm, AdminStatsForm, AdminTeamForm,
                        LoginForm)
from fuca.models import Match, News, Player, Statistics, Team


@app.route("/")
@app.route("/home")
def home():
    news_db = News.query.all()
    news_list = [news.jinja_dict() for news in news_db]
    return render_template('home.html', newslist=news_list)


@app.route("/results")
def results():
    results_db = Match.query.filter(Match.date_time < datetime.now()).all()
    results_list = [result.jinja_dict() for result in results_db]
    return render_template('results.html', results=results_list, title='Results')


# TODO: If not such player exists, forward to some error page.
@app.route("/player/<int:id>")
def player(id):
    player = Player.query.get(id)
    if not player:
        return "404"
    player = player.jinja_dict()
    return render_template('player.html', player=player, title=player['name'])


@app.route("/schedule")
def schedule():
    schedule_db = Match.query.filter(Match.date_time >= datetime.now()).all()
    schedule_list = [schedule.jinja_dict() for schedule in schedule_db]
    return render_template('schedule.html', schedule=schedule_list, title='Schedule')


@app.route("/stats")
def stats():
    return render_template('stats.html',
                           title='Stats',
                           stats=dummydata.stats,
                           best_player=dummydata.stats_best_player,
                           scorers=dummydata.stats_scorers)


@app.route("/teams")
def teams():
    teams_db = Team.query.all()
    teams = [team.jinja_dict() for team in teams_db]
    return render_template('teams.html', teams=teams, title='Teams')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'uros@uros.rs' and form.password.data == 'uros':
            flash('Uros has been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Not Uros. Please be Uros!', 'danger')
    return render_template('login.html', form=form, title='Login')
