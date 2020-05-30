"""
Author: Uros Isakovic
"""

import os
import sys
sys.path.insert(0, os.path.dirname(os.path.realpath(__file__)) + '/..')
from datetime import datetime
from random import randint
from fuca import db, bcrypt, create_app
from fuca.models import Match, News, Player, Statistics, Team

# configu
NEWS_CNT = 6
TEAMS_CNT = 6
PLAYER_CNT = 30
assert PLAYER_CNT % TEAMS_CNT == 0, 'Every team must have the same number of players'


def print_array(arr, newlines=2):
    for el in arr:
        print(el)
    for nl in range(newlines):
        print('\n')


def init_empty_db():
    if os.path.exists('../fuca/site.db'):
        print("Removed site.db\n\n\n\n")
        os.remove('../fuca/site.db')

    db.create_all()


def add_news():
    news_titles = ['title_' + str(i) for i in range(NEWS_CNT)]
    news_contents = ['content_' + str(i) for i in range(NEWS_CNT)]
    news_arr = [News(title=news_titles[i], content=news_contents[i]) for i in range(NEWS_CNT)]

    for news in news_arr:
        db.session.add(news)
    db.session.commit()

    print_array(News.query.all())


# TODO: Add captain foreign key
def add_teams():
    team_names = ['team_name_' + str(i) for i in range(TEAMS_CNT)]
    teams = [Team(name=team_names[i]) for i in range(TEAMS_CNT)]

    for team in teams:
        db.session.add(team)
    db.session.commit()

    print_array(Team.query.all())


def add_admin():
    admin = Player(name='admin',
                   email='admin@admin.admin',
                   password=bcrypt.generate_password_hash('admin').decode('utf-8'),
                   registered=True,
                   is_admin=True,
                   birthdate=datetime.now(),
                   number=-1,
                   team_id=-1)
    db.session.add(admin)
    db.session.commit()
    

def add_players():
    player_names = ['player_name' + str(i) for i in range(PLAYER_CNT)]
    player_numbers = [0 for _ in range(PLAYER_CNT)]
    player_birthdates = [datetime.now() for _ in range(PLAYER_CNT)]
    player_images = ['default.jpg' for _ in range(PLAYER_CNT)]
    player_emails = ['player' + str(i) + '@gmail.com' for i in range(PLAYER_CNT)]
    player_passwords = ['password' + str(i) for i in range(PLAYER_CNT)]
    player_team_ids = [i % (PLAYER_CNT / TEAMS_CNT) + 1 for i in range(PLAYER_CNT)]

    players = [Player(name=player_names[i],
                      birthdate=player_birthdates[i],
                      number=player_numbers[i],
                      image=player_images[i],
                      email=player_emails[i],
                      password=player_passwords[i],
                      team_id = player_team_ids[i]) for i in range(PLAYER_CNT)]

    for player in players:
        db.session.add(player)
    db.session.commit()

    print_array(Player.query.all())


#TODO: Make Match table goals correspond to Statistics table goals.
def add_matches():
    def generate_timeslot():
        if randint(0, 2) % 2 == 0:
            ret = datetime(2019, 8, 20, 20, 0, 0)
        else:
            ret = datetime(2020, 5, 20, 19, 0, 0)

        return ret

    teams = Team.query.all()
    for host_team in teams:
        for guest_team in teams:
            if host_team != guest_team:
                match = Match(host_team=host_team,
                              guest_team=guest_team,
                              date_time=generate_timeslot(),
                              host_team_goals=randint(0, 7),
                              guest_team_goals=randint(0, 7))
                db.session.add(match)
    
    db.session.commit()
    print_array(Match.query.all())


def add_statistics():
    players = Player.query.all()
    matches = Match.query.all()

    for player in players:
        for match in matches:
            if player.team in [match.host_team, match.guest_team]:
                stats = Statistics(goals=randint(0, 5),
                                   assists=randint(0, 5),
                                   yellow=randint(0, 2),
                                   red=randint(0, 2),
                                   player=player,
                                   match=match)
                db.session.add(stats)

    db.session.commit()
    print_array(Statistics.query.all())


def main():
    app = create_app()
    with app.app_context():   
        db.init_app(app) 
        init_empty_db()
        add_news()
        add_admin()
        add_teams()
        add_players()
        add_matches()
        add_statistics()


if __name__ == '__main__':
    main()
