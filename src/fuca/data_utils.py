import os
from datetime import datetime
from fuca import db, app
from fuca.models import *

def add_news(title, content):
    new_news = News(title=title,
                    content=content)
    db.session.add(newNews)
    db.session.commit()


def update_news(id, new_title, new_content):
    update_news = News.query.filter_by(id=id).first()
    update_news.title = form.title.data
    update_news.content = form.content.data
    update_news.date = datetime.utcnow()
    db.session.commit()


def delete_news(id):
    News.query.filter_by(id=id).delete()
    db.session.commit()


def save_image(form_image, image_name, team_player):
    _, f_ext = os.path.splitext(form_image.filename)
    image_fn = image_name + f_ext
    image_path = os.path.join(app.root_path, 'static/images/{}/{}'.format(team_player, image_fn))
    form_image.save(image_path)
    return image_fn


def add_player(name, number, email, birthdate, team_id, image):
    new_player = Player(name=name,
                        number=number,
                        email=email,
                        birthdate=birthdate,
                        team_id=team_id)
    db.session.add(new_player)
    db.session.commit()
    if image:
        image_file = save_image(image, str(new_player.id), "players")
        new_player.image = image_file
        db.session.commit()
    

def update_player(id, name, number, email, birthdate, team_id, image):
    update_player = Player.query.filter_by(id=id).first()
    update_player.name = name
    update_player.number = number
    update_player.email = email
    update_player.birthdate = birthdate
    update_player.team_id = form.team_dd.data
    if image:
        image_file = save_image(image, str(update_player.id), "players")
        update_player.logo_image = image_file
        db.session.commit()


def delete_player(id):
    Player.query.filter_by(id=id).delete()
    db.session.commit()


def add_team(name, image):
    new_team = Team(name=name)
    db.session.add(new_team)
    db.session.commit()
    if image:
        image_file = save_image(image, str(new_team.id), "teams")
        new_team.logo_image = image_file
    db.session.commit()


def update_team(id, name, image):
    update_team = Team.query.filter_by(id=id).first()
    update_team.name = name
    if image:
        image_file = save_image(image, str(update_team.id), "teams")
        update_team.logo_image = image_file
        db.session.commit()


def delete_team(id):
    Team.query.filter_by(id=id).delete()
    db.session.commit()


def add_match(date_time, host_team_id, guest_team_id):
    new_match = Match(date_time=date_time,
                      host_team_id=host_team_id,
                      guest_team_id=guest_team_id)
    db.session.add(new_match)
    db.session.commit()


def update_match(id, date_time, host_team_id, guest_team_id):
    update_match = Match.query.filter_by(id=id).first()
    update_match.host_team_id = host_team_id
    update_match.guest_team_id = guest_team_id
    update_match.date_time = date_time
    db.session.commit()


def delete_match(id):
    Match.query.filter_by(id=id).delete()
    db.session.commit()


def add_result(id, 
               host_team_goals,
               host_team_yellow,
               host_team_red,
               host_team_shots, 
               guest_team_goals, 
               guest_team_yellow, 
               guest_team_red, 
               guest_team_shots):
    match = Match.query.filter_by(id=id).first()
    
    match.host_team_goals = host_team_goals
    match.host_team_red = host_team_red
    match.host_team_yellow = host_team_yellow
    match.host_team_shots = host_team_shots

    match.guest_team_goals = guest_team_goals
    match.guest_team_red = guest_team_read
    match.guest_team_yellow = guest_team_yellow
    match.guest_team_shots = guest_team_shots

    db.session.commit()


def update_result(id, 
                  host_team_goals,
                  host_team_yellow,
                  host_team_red,
                  host_team_shots, 
                  guest_team_goals, 
                  guest_team_yellow, 
                  guest_team_red, 
                  guest_team_shots):
    add_result(id, 
               host_team_goals,
               host_team_yellow,
               host_team_red,
               host_team_shots, 
               guest_team_goals, 
               guest_team_yellow, 
               guest_team_red, 
               guest_team_shots)


def delete_result(id):
    add_result(id, 0, 0, 0, 0, 0, 0, 0, 0)


def add_statistics(player_id,
                   match_id,
                   goals,
                   assists,
                   yellow,
                   red):
    new_statistics = Statistics(player_id=player_id,
                                match_id=match_id,
                                goals=goals,
                                assists=assists,
                                yellow=yellow,
                                red=red)
    db.session.add(new_statistics)
    db.session.commit()


def update_statistics(player_id,
                      match_id,
                      goals,
                      assists,
                      yellow,
                      red):
    update_statistics = Statistics.query.filter_by(match_id=match_id).filter_by(player_id=player_id)
    update_statistics.player_id = player_id
    update_statistics.match_id = match_id
    update_statistics.goals = goals
    update_statistics.assists = assists
    update_statistics.yellow = yellow
    update_statistics.red = red
    db.session.commit()


def delete_statistics(match_id, player_id):
    Statistics.query.filter_by(match_id=match_id).filter_by(player_id=player_id).delete()
    db.session.commit()
