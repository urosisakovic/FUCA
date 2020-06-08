"""
Author: Igor Andrejic
"""
import os
from fuca import db, bcrypt
from fuca.models import *
from flask import current_app

def add_news(title, content):
    """
    Function which adds News to the database.

    Args:
        title(string): News title.
        content(string): News content.
    """
    new_news = News(title=title,
                    content=content)
    db.session.add(new_news)
    db.session.commit()


def update_news(id, new_title, new_content):
    """
    Function which updates News in the database.

    Args:
        title(string): News' new title.
        content(string): News' new content.
    """
    update_news = News.query.get(id)
    update_news.title = new_title
    update_news.content = new_content
    db.session.commit()


def delete_news(id):
    """
    Function which deletes News from the database.

    Args:
        id(int): News id.
    """
    news = News.query.filter_by(id=id).delete()
    db.session.commit()


def save_image(form_image, image_name, team_player):
    """
    Function which saves new image in the /static/image directory.

    Args:
        form_image(Image): Image object.
        image_name(string): Name of the image file to be saved.
        team_player(string): Denotes whether to save image in teams directory
                        or players directory. Can have values 'teams' or 'players'.
    """
    _, f_ext = os.path.splitext(form_image.filename)
    image_fn = image_name + f_ext
    image_path = os.path.join(current_app.root_path, 'static/images/{}/{}'.format(team_player, image_fn))
    form_image.save(image_path)
    return image_fn


def add_player(name, number, email, birthdate, team_id, image):
    """
    Function which adds Player to the database.

    Args:
        name(string): First and last name.
        number(int): Jersey number.
        birthdate(datetime): Date of birth.
        team_id(int): Id of the team he is playing for.
        image(string): Filepath to his profile image. 
    """
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
    """
    Function which updates a Player in the database.

    Args:
        name(string): New first and last name.
        number(int): New jersey number.
        birthdate(datetime): New date of birth.
        team_id(int): New id of the team he is playing for.
        image(string): New filepath to his profile image. 
    """
    update_player = Player.query.get(id)
    update_player.name = name
    update_player.number = number
    update_player.email = email
    update_player.birthdate = birthdate
    update_player.team_id = team_id
    if image:
        image_file = save_image(image, str(update_player.id), "players")
        update_player.logo_image = image_file
    db.session.commit()


def delete_player(id):
    """
    Function which deletes a Player from the database.

    Args:
        id(int): Player id.
    """
    Player.query.filter_by(id=id).delete()
    db.session.commit()

def add_team(name, image):
    """
    Function which adds Team to the database.

    Args:
        name(string): Team name.
        image(string): Filepath to the team's image.
    """
    new_team = Team(name=name)
    db.session.add(new_team)
    db.session.commit()
    if image:
        image_file = save_image(image, str(new_team.id), "teams")
        new_team.logo_image = image_file
    db.session.commit()


def update_team(id, name, image):
    """
    Function which updates Team in the database.

    Args:
        id(int): Team id.
        name(string): New Team name.
        image(string): New filepath to the team's image.
    """
    update_team = Team.query.get(id)
    update_team.name = name
    if image:
        image_file = save_image(image, str(update_team.id), "teams")
        update_team.logo_image = image_file
    db.session.commit()


def delete_team(id):
    """
    Function which deletes a Team from the database.

    Args:
        id(int): Team id.
    """
    Team.query.filter_by(id=id).delete()
    db.session.commit()


def add_match(date_time, host_team_id, guest_team_id):
    """
    Function which adds a Match to the database.

    Args:
        date_time(datetime): Date and time of the new Match.
        host_team_id(int): Host team's id.
        guest_team_id(int): Guest team's id.
    """
    new_match = Match(date_time=date_time,
                      host_team_id=host_team_id,
                      guest_team_id=guest_team_id)
    db.session.add(new_match)
    db.session.commit()


def update_match(id, date_time, host_team_id, guest_team_id):
    """
    Function which updates a Match in the database.

    Args:
        id(int): Match's id.
        date_time(datetime): New date and time of the new Match.
        host_team_id(int): New host team's id.
        guest_team_id(int): New guest team's id.
    """
    update_match = Match.query.get(id)
    update_match.host_team_id = host_team_id
    update_match.guest_team_id = guest_team_id
    update_match.date_time = date_time
    db.session.commit()


def delete_match(id):
    """
    Function which delets a Match from the database.

    Args:
        id(int): Match's id.
    """
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
    """
    Function which adds a Result to the database.

    Args:
        host_team_goals(int): Host team goals.
        host_team_yellow(int): Host team yellow.
        host_team_red(int): Host team red.
        host_team_shots(int): Host team shots.
        guest_team_goals(int): Guest team goals.
        guest_team_yellow(int): Guest team yellows.
        guest_team_red(int): Guest team red.
        guest_team_shots(int): Guest team shots.
    """
    match = Match.query.get(id)
    
    match.host_team_goals = host_team_goals
    match.host_team_red = host_team_red
    match.host_team_yellow = host_team_yellow
    match.host_team_shots = host_team_shots

    match.guest_team_goals = guest_team_goals
    match.guest_team_red = guest_team_red
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
    """
    Function which updates a Result in the database.

    Args:
        id(int): Matche's id.
        host_team_goals(int): New host team goals.
        host_team_yellow(int): New host team yellow.
        host_team_red(int): New host team red.
        host_team_shots(int): New host team shots.
        guest_team_goals(int): New guest team goals.
        guest_team_yellow(int): New guest team yellows.
        guest_team_red(int): New guest team red.
        guest_team_shots(int): New guest team shots.
    """
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
    """
    Function which deletes a Result from the database.

    Args:
        id(int): Matche's id.
    """
    add_result(id, 0, 0, 0, 0, 0, 0, 0, 0)


def add_statistics(player_id,
                   match_id,
                   goals,
                   assists,
                   yellow,
                   red):
    """
    Function which adds a Statistics to the database.

    Args:
        player_id(int): Player id.
        match_id(int): Match id.
        goals(int): Goals scored.
        assists(int): Assists.
        yellow(int): Yellow cards.
        red(int): Red cards.
    """
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
    """
    Function which updates a Statistics in the database.

    Args:
        player_id(int): New Player id.
        match_id(int): New Match id.
        goals(int): New Goals scored.
        assists(int): New Assists.
        yellow(int): New Yellow cards.
        red(int): New Red cards.
    """
    update_statistics = Statistics.query.filter_by(match_id=match_id).filter_by(player_id=player_id).first()
    update_statistics.player_id = player_id
    update_statistics.match_id = match_id
    update_statistics.goals = goals
    update_statistics.assists = assists
    update_statistics.yellow = yellow
    update_statistics.red = red
    db.session.commit()


def delete_statistics(match_id, player_id):
    """
    Function which deletes a Statistics from the database.

    Args:
        player_id(int): New Player id.
        match_id(int): New Match id.
    """
    Statistics.query.filter_by(match_id=match_id).filter_by(player_id=player_id).delete()
    db.session.commit()


def register_player(email, password):
    """
    Function which registers a player. Email is expected to be valid.

    Args:
        email(string): Player email.
        password(string): Player password.
    """
    player = Player.query.filter_by(email=email).first()
    player.password = bcrypt.generate_password_hash(password).decode('utf-8')
    player.registered = True
    db.session.commit()
    return player


def is_registered_player(email):
    """
    Function which checks whether a player with a 
    given email is registered.

    Args:
        email(string): Player's email.
    """
    player = Player.query.filter_by(email=email).first()
    return player.registered


def exists_player_with_email(email):
    """
    Function which checks whether a player with a 
    given email exists.

    Args:
        email(string): Player's email.
    """
    player = Player.query.filter_by(email=email).first()
    if player:
        return True, player
    else:
        return False, player


def exists_player(email, password):
    """
    Function which checks whether a player with
    given email and password exists.

    Args:
        email(string): Player's email.
    """
    player = Player.query.filter_by(email=email).first()
    if player and bcrypt.check_password_hash(player.password, password):
        return True, player
    return False, player