from flask import Flask
app = Flask(__name__)

app.config['SECRET_KEY'] = ''


@app.route("/")
@app.route("/home")
def home():
    return "Home"


@app.route("/results")
def results():
    return "Results"


@app.route("/player")
def player():
    return "Player"


@app.route("/schedule")
def schedule():
    return "Schedule"


@app.route("signin")
def signin():
    return "Sign In"


@app.route("/stats")
def stats():
    return "Stats"


@app.route("bestplayers")
def bestplayers():
    return "Best Players"


@app.route("standings")
def standings():
    return "Standings"


@app.route("bestscorers")
def bestscorers():
    return "Best Scorers"


@app.route("teams")
def teams():
    return "Teams"


@app.route("teamresults")
def teamresults():
    return "Team Results"


@app.route("teamschedule")
def teamschedule():
    return "Team Schedule"


@app.route("teamsquad")
def teamsquad():
    return "Team Squad"


if __name__ == '__main__':
    app.run(debug=True)