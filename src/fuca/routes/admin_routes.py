import os
from datetime import datetime

from flask import flash, redirect, render_template, request, url_for

from fuca import app, db
from fuca.forms import (AdminAddNewsForm, AdminAddPlayerForm, AdminAddTeamForm,
                        AdminDeleteNewsForm, AdminDeletePlayerForm,
                        AdminDeleteTeamForm, AdminMatchForm, AdminResultForm,
                        AdminStatsForm, AdminUpdateNewsForm,
                        AdminUpdatePlayerForm, AdminUpdateTeamForm, LoginForm)
from fuca.models import Match, News, Player, Statistics, Team


@app.route("/admin")
def admin():
    return render_template('admin/layout.html',
                           title='Admin')


@app.route("/admin/news", methods=['GET', 'POST'])
def admin_news():
    return render_template('admin/news-layout.html',
                           title='Admin News')


@app.route("/admin/news/add", methods=['GET', 'POST'])
def admin_news_add():
    add_form = AdminAddNewsForm()
    if add_form.validate_on_submit():
        print("add news")
        newNews = News(title=add_form.title.data,
                       content=add_form.content.data)
        db.session.add(newNews)
        db.session.commit()

        return redirect(url_for('admin_news_add'))

    return render_template('admin/news-add.html',
                           form=add_form,
                           title='Admin Add News')

@app.route("/admin/news/update", methods=['GET', 'POST'])
def admin_news_update():
    update_form = AdminUpdateNewsForm()
    news_db = News.query.all()
    news_list = [news.jinja_dict() for news in news_db]
    news_choices = [(news['id'], news['title'] + ' ' + news['date']) for news in news_list]
    update_form.news_dd.choices = news_choices
    
    if request.method == 'POST':
        update_news = News.query.filter_by(id=update_form.news_dd.data).all()[0]
        update_news.title = update_form.title.data
        update_news.content = update_form.content.data
        update_news.date = datetime.utcnow()
        db.session.commit()

        return redirect(url_for('admin_news_update'))

    return render_template('admin/news-update.html',
                           form=update_form,
                           title='Admin Update News')

@app.route("/admin/news/delete", methods=['GET', 'POST'])
def admin_news_delete():
    delete_form = AdminDeleteNewsForm()

    news_db = News.query.all()
    news_list = [news.jinja_dict() for news in news_db]
    news_choices = [(news['id'], news['title'] + ' ' + news['date']) for news in news_list]
    delete_form.news_dd.choices = news_choices

    if request.method == 'POST':
        News.query.filter_by(id=delete_form.news_dd.data).delete()
        db.session.commit()

        return redirect(url_for('admin_news_delete'))

    return render_template('admin/news-delete.html',
                           form=delete_form,
                           title='Admin Delete News')



#TODO: Set image filename. 
def save_image(form_image, image_name, team_player):
    _, f_ext = os.path.splitext(form_image.filename)
    image_fn = image_name + f_ext
    image_path = os.path.join(app.root_path, 'static/images/{}/{}'.format(team_player, image_fn))
    form_image.save(image_path)
    return image_fn


#TODO: Check for unique team name.
@app.route("/admin/teams", methods=['GET', 'POST'])
def admin_teams():
    return render_template('admin/teams-layout.html', title='Admin Teams')


@app.route("/admin/teams/add", methods=['GET', 'POST'])
def admin_teams_add():
    form = AdminAddTeamForm()
    if form.validate_on_submit():
        new_team = Team(name=form.name.data)
        db.session.add(new_team)
        db.session.commit()

        if form.image.data:
            image_file = save_image(form.image.data, str(new_team.id), "teams")
            new_team.logo_image = image_file

        db.session.commit()

        return redirect(url_for('admin_teams_add'))

    return render_template('admin/teams-add.html', form=form, title='Admin Add Teams')


@app.route("/admin/teams/update", methods=['GET', 'POST'])
def admin_teams_update():
    update_form = AdminUpdateTeamForm()

    teams_db = Team.query.all()
    teams = [team.jinja_dict() for team in teams_db]
    team_choices = [(team['id'], team['name']) for team in teams]
    update_form.teams_dd.choices = team_choices

    if request.method == 'POST':
        update_team = Team.query.filter_by(id=update_form.teams_dd.data).all()[0]
        update_team.name = update_form.name.data
        if update_form.image.data:
            image_file = save_image(update_form.image.data, str(update_team.id), "teams")
            update_team.logo_image = image_file
        db.session.commit()
        return redirect(url_for('admin_teams_update'))

    return render_template('admin/teams-update.html', form=update_form, title='Admin Update Teams')


@app.route("/admin/teams/delete", methods=['GET', 'POST'])
def admin_teams_delete():
    delete_form = AdminDeleteTeamForm()

    teams_db = Team.query.all()
    teams = [team.jinja_dict() for team in teams_db]
    team_choices = [(team['id'], team['name']) for team in teams]
    delete_form.teams_dd.choices = team_choices

    if request.method == 'POST':
        Team.query.filter_by(id=delete_form.teams_dd.data).delete()
        db.session.commit()

        return redirect(url_for('admin_teams_delete'))

    return render_template('admin/teams-delete.html', form=delete_form, title='Admin Delete Teams')


@app.route("/admin/players", methods=['GET', 'POST'])
def admin_players():
    return render_template('admin/players-layout.html', title='Admin Players')


@app.route("/admin/players/add", methods=['GET', 'POST'])
def admin_players_add():
    add_form = AdminAddPlayerForm()

    teams_db = Team.query.all()
    teams = [team.jinja_dict() for team in teams_db]
    team_choices = [(team['id'], team['name']) for team in teams]
    add_form.team_dd.choices = team_choices

    if request.method == 'POST':
        pass

    return render_template('admin/players-add.html', form=add_form, title='Admin Add Players')


@app.route("/admin/players/update", methods=['GET', 'POST'])
def admin_players_update():
    update_form = AdminUpdatePlayerForm()

    players_db = Player.query.all()
    players = [player.jinja_dict() for player in players_db]
    player_choices = [(player['team_id'], player['name']) for player in players]
    update_form.player_dd.choices = player_choices

    teams_db = Team.query.all()
    teams = [team.jinja_dict() for team in teams_db]
    team_choices = [(id, team['name']) for team in teams]
    update_form.team_dd.choices = team_choices

    if request.method == 'POST':
        update_player = Player.query.filter_by(id=update_form.player_dd.data).all()[0]
        update_player.name = update_form.name.data
        update_player.number = update_form.number.data
        update_player.email = update_form.email.data

        update_player.birthdate = datetime(int(update_form.birth_year.data), int(update_form.birth_month.data), int(update_form.birth_day.data), 0, 0, 0)
        update_player.team_id = update_form.team_dd.data

        if update_form.image.data:
            image_file = save_image(update_form.image.data, str(update_player.id), "players")
            update_player.logo_image = image_file
        db.session.commit()
        return redirect(url_for('admin_players_update'))

    return render_template('admin/players-update.html', form=update_form, title='Admin Update Players')


@app.route("/admin/players/delete", methods=['GET', 'POST'])
def admin_players_delete():
    delete_form = AdminDeletePlayerForm()

    players_db = Player.query.all()
    players = [player.jinja_dict() for player in players_db]
    player_choices = [(player['team_id'], player['name']) for player in players]
    delete_form.player_dd.choices = player_choices

    if request.method == 'POST':
        Player.query.filter_by(id=delete_form.player_dd.data).delete()
        db.session.commit()

        return redirect(url_for('admin_players_delete'))

    return render_template('admin/players-delete.html', form=delete_form, title='Admin Delete Players')


@app.route("/admin/matches", methods=['GET', 'POST'])
def admin_matches():
    form = AdminMatchForm()

    teams_db = Team.query.all()
    teams = [team.jinja_dict() for team in teams_db]
    team_choices = [(id, team['name']) for team in teams]

    form.host_team_dd.choices = team_choices
    form.guest_team_dd.choices = team_choices

    if form.validate_on_submit():
        print("Validated")
    else:
        print("Not Validated")

    return render_template('admin/matches.html', form=form, title='Admin Matches')


@app.route("/admin/results", methods=['GET', 'POST'])
def admin_results():
    form = AdminResultForm()

    matches_db = Match.query.all()
    matches = [match.jinja_dict() for match in matches_db]
    match_choices = [(match['id'], match['team1_name'] + ' - ' + match['team2_name']) for match in matches]
    form.match_dd.choices = match_choices

    if form.validate_on_submit():
        print("Validated")
    else:
        print("Not Validated")

    return render_template('admin/results.html', form=form, title='Admin Results')


@app.route("/admin/statistics", methods=['GET', 'POST'])
def admin_statistics():
    form = AdminStatsForm()
    if form.validate_on_submit():
        print("Validated")
    else:
        print("Not Validated")

    return render_template('admin/statistics.html', form=form, title='Admin Statistics')
