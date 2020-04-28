from flask import flash, redirect, render_template, url_for
from fuca import app, dummydata
from fuca.models import News, Team, Player, Match, Statistics
from fuca.forms import LoginForm
from datetime import datetime


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


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'uros@uros.rs' and form.password.data == 'uros':
            flash('Uros has been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Not Uros. Please be Uros!', 'danger')
    return render_template('login.html', title='Login', form=form)


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


@app.route("/team/<int:id>")
def team(id):
    team = Team.query.get(id)
    if not team:
        return "404"
    team = team.jinja_dict()
    return render_template('team.html', team=team, title=team['name'])


@app.route("/standings")
def standings():
    teams_db = Team.query.all()
    teams = [team.jinja_dict() for team in teams_db]
    teams = sorted(teams, key=lambda team: team['points'])
    return render_template('standings.html', teams=teams, title='Standings')


@app.route("/bestplayers")
def bestplayers():
    players_db = Player.query.all()
    players = [player.jinja_dict() for player in players_db]
    players = sorted(players, key=lambda player: player['points'])
    players = reversed(players)
    return render_template('best-players.html', players=players, title='Best Players')


@app.route("/bestscorers")
def bestscorers():
    players_db = Player.query.all()
    players = [player.jinja_dict() for player in players_db]
    players = sorted(players, key=lambda player: player['goals'])
    players = reversed(players)
    return render_template('best-scorers.html', players=players, title='Best Scorers')


#TODO: Add team name in title.
#TODO: Adress invalid id.
@app.route("/teamresults/<int:id>")
def teamresults(id):
    results_db = Match.query.filter(Match.date_time <= datetime.now()).filter(Match.guest_team_id == id).all() +\
        Match.query.filter(Match.date_time <= datetime.now()).filter(Match.host_team_id == id).all()
    results_list = [result.jinja_dict() for result in results_db]
    return render_template('team-results.html', results=results_list, id=id, title='Team Results')


#TODO: Add team name in title.
#TODO: Adress invalid id.
@app.route("/teamschedule/<int:id>")
def teamschedule(id):
    schedule_db = Match.query.filter(Match.date_time >= datetime.now()).filter(Match.guest_team_id == id).all() +\
        Match.query.filter(Match.date_time >= datetime.now()).filter(Match.host_team_id == id).all()
    schedule_list = [schedule.jinja_dict() for schedule in schedule_db]
    return render_template('team-schedule.html', schedule=schedule_list, id=id, title='Team Schedule')


#TODO: Add team name in title.
#TODO: Address invalid id.
@app.route("/teamsquad/<int:id>")
def teamsquad(id):
    players_db = Player.query.filter(Player.team_id == id).all()
    players = [player.jinja_dict() for player in players_db]
    return render_template('team-squad.html', players=players, id=id, title='Team Squad')
