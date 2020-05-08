from datetime import datetime

from flask import flash, redirect, render_template, url_for

from fuca import app, dummydata, data_utils
from fuca.forms import LoginForm, RegisterForm
from fuca.models import Match, News, Player, Statistics, Team
from flask_login import login_user


@app.route("/")
@app.route("/home")
def home():
    news_db = News.query.all()
    news_list = [news.jinja_dict() for news in news_db]
    news_list = sorted(news_list, key=lambda news: news['raw_date'])[::-1]
    return render_template('home/home.html', newslist=news_list)


@app.route("/results")
def results():
    results_db = Match.query.filter(Match.date_time < datetime.now()).all()
    results_list = [result.jinja_dict() for result in results_db]
    for result in results_list:
        result['team1_logo'] = url_for('static', filename='images/teams/{}'.format(result['host_team'].logo_image))
        result['team2_logo'] = url_for('static', filename='images/teams/{}'.format(result['guest_team'].logo_image))
    return render_template('home/results.html', results=results_list, title='Results')


@app.route("/schedule")
def schedule():
    schedule_db = Match.query.filter(Match.date_time >= datetime.now()).all()
    schedule_list = [schedule.jinja_dict() for schedule in schedule_db]
    for schedule in schedule_list:
        schedule['team1_logo'] = url_for('static', filename='images/teams/{}'.format(schedule['host_team'].logo_image))
        schedule['team2_logo'] = url_for('static', filename='images/teams/{}'.format(schedule['guest_team'].logo_image))
    return render_template('home/schedule.html', schedule=schedule_list, title='Schedule')


# TODO: If not such player exists, forward to some error page.
@app.route("/player/<int:id>")
def player(id):
    player = Player.query.get(id)
    if not player:
        return "404"
    player = player.jinja_dict()

    image_file = url_for('static', filename='images/players/{}'.format(player['image']))

    return render_template('home/player.html', player=player, image_file=image_file, title=player['name'])


@app.route("/stats")
def stats():
    return render_template('home/stats.html',
                           title='Stats',
                           stats=dummydata.stats,
                           best_player=dummydata.stats_best_player,
                           scorers=dummydata.stats_scorers)


@app.route("/teams")
def teams():
    teams_db = Team.query.all()
    teams = [team.jinja_dict() for team in teams_db]
    for team in teams:
        team['logo'] = url_for('static', filename='images/teams/{}'.format(team['logo']))
    return render_template('home/teams.html', teams=teams, title='Teams')


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        valid, player = data_utils.exists_player(email=form.email.data,
                                                 password=form.password.data)
            
        if valid:
            login_user(player, remember=form.remember_me.data)
            flash('{} logged in!'.format(player.name), 'success')
            return redirect(url_for('home'))
        else:
            flash('Login unsuccessful! Please check email and password.', 'danger')
                        
    return render_template('home/login.html', form=form, title='Login')


#TODO: Add email verification.
@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        player = data_utils.register_player(form.email.data, form.password.data)
        flash('Account for {} has been created! You are now able to log in.'.format(player.name), 'success')
        return redirect(url_for('login'))
    return render_template('home/register.html', form=form, title='Register')