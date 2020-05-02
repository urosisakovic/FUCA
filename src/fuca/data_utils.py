from datetime import datetime
from fuca import db
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
        new_player.logo_image = image_file
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
    if image:
        image_file = save_image(image, str(new_team.id), "teams")
        new_team.logo_image = image_file
    db.session.add(new_team)
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


def add_result():
    pass


def update_result():
    pass


def delete_result():
    pass


def add_statistics():
    pass


def update_statistics():
    pass


def delete_statistics():
    pass
