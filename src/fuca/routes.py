from flask import flash, redirect, render_template, url_for
from fuca import app, dummydata
from fuca.forms import LoginForm


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', newslist=dummydata.news)


@app.route("/results")
def results():
    return render_template('results.html', results=dummydata.results, title='Results')


@app.route("/player")
def player():
    return render_template('player.html', player=dummydata.player, title=dummydata.player['name'])


@app.route("/schedule")
def schedule():
    return render_template('schedule.html', schedule=dummydata.schedule, title='Schedule')


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


@app.route("/bestplayers")
def bestplayers():
    return "Best Players"


@app.route("/standings")
def standings():
    return "Standings"


@app.route("/bestscorers")
def bestscorers():
    return "Best Scorers"


@app.route("/teams")
def teams():
    return "Teams"


@app.route("/teamresults")
def teamresults():
    return "Team Results"


@app.route("/teamschedule")
def teamschedule():
    return "Team Schedule"


@app.route("/teamsquad")
def teamsquad():
    return "Team Squad"
