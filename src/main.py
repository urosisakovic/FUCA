from flask import Flask, render_template, flash, redirect, url_for
from forms import LoginForm
app = Flask(__name__)

import dummydata

#TODO: Generate real random key
app.config['SECRET_KEY'] = '1234'

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', newslist=dummydata.news)


@app.route("/results")
def results():
    return "Results"


@app.route("/player")
def player():
    return "Player"


@app.route("/schedule")
def schedule():
    return "Schedule"


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
    return "Stats"


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


if __name__ == '__main__':
    app.run(debug=True)