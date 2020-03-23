from flask import Flask, render_template
app = Flask(__name__)

app.config['SECRET_KEY'] = ''

#TODO: Use some date format insted of the string.
news = [
    {
        'news_title': 'Lorem1 title1',
        'content': 'lorem1 ipsum1 lorem1 ipsum1 lorem1 ipsum1 lorem1 ipsum1 lorem1 ipsum1',
        'date': '24-02-2020'
    },
    {
        'news_title': 'Lorem2 title2',
        'content': 'lorem2 ipsum2 lorem2 ipsum2 lorem2 ipsum2 lorem2 ipsum2 lorem2 ipsum2',
        'date': '28-02-2020'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', newslist=news)


@app.route("/results")
def results():
    return "Results"


@app.route("/player")
def player():
    return "Player"


@app.route("/schedule")
def schedule():
    return "Schedule"


@app.route("/login")
def login():
    return "Login"


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