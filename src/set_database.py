import os
from datetime import datetime
from random import randint
from fuca import db
from fuca.models import Match, News, Player, Statistics, Team

# configu
NEWS_CNT = 6
TEAMS_CNT = 6
PLAYER_CNT = 30
assert PLAYER_CNT % TEAMS_CNT == 0, 'Every team must have the same number of players'


def print_array(arr, newlines=3):
    for el in arr:
        print(el)
    for nl in range(newlines):
        print('\n')


def init_empty_db():
    if os.path.exists('fuca/site.db'):
        print("Removed site.db")
        os.remove('fuca/site.db')

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


def add_players():
    player_names = ['player_name' + str(i) for i in range(PLAYER_CNT)]
    player_birthdates = [datetime.now() for _ in range(PLAYER_CNT)]
    player_images = ['image' + str(i) + '.png' for i in range(PLAYER_CNT)]
    player_emails = ['player' + str(i) + '@gmail.com' for i in range(PLAYER_CNT)]
    player_passwords = ['password' + str(i) for i in range(PLAYER_CNT)]
    player_team_ids = [i % (PLAYER_CNT / TEAMS_CNT) + 1 for i in range(PLAYER_CNT)]

    players = [Player(name=player_names[i],
                     birthdate=player_birthdates[i],
                     image=player_images[i],
                     email=player_emails[i],
                     password=player_passwords[i],
                     team_id = player_team_ids[i]) for i in range(PLAYER_CNT)]

    for player in players:
        db.session.add(player)
    db.session.commit()

    print_array(Player.query.all())


def add_matches():
    teams = Team.query.all()
    for host_team in teams:
        for guest_team in teams:
            if host_team != guest_team:
                match = Match(host_team=host_team, guest_team=guest_team)
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
                                   experience=randint(0, 100),
                                   yellow=randint(0, 2),
                                   red=randint(0, 2),
                                   player=player,
                                   match=match)
                db.session.add(stats)

    db.session.commit()
    print_array(Statistics.query.all())


def main():
    init_empty_db()
    add_news()
    add_teams()
    add_players()
    add_matches()
    add_statistics()


if __name__ == '__main__':
    main()
