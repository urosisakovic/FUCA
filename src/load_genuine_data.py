import json
import os
from datetime import datetime

from fuca import db
from fuca.models import Match, News, Player, Statistics, Team


def print_array(arr, newlines=2):
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
    news_filepath = 'data/news.json'
    with open(news_filepath) as json_file:
        news_list = json.load(json_file)['news']

    cnt = 0
    for news in news_list:
        db.session.add(News(title=news['title'], content=news['content']))
        cnt += 1
    db.session.commit()
    print('Added {} entries to table News.'.format(cnt))


def add_teams():
    teams_filepath = 'data/teams.json'
    with open(teams_filepath) as json_file:
        teams_list = json.load(json_file)['teams']
    
    cnt = 0
    for team in teams_list:
        db.session.add(Team(name=team['name'],
                            matches=team['matches'],
                            wins=team['wins'],
                            losses=team['losses'],
                            draws=team['draws'],
                            goal_diff=team['goal_diff'],
                            captain_id=int(team['captain_id'])+1))
        cnt += 1
    db.session.commit()

    print('Added {} entries to table Teams'.format(cnt))


def string_to_date(str_date):
    return datetime.strptime(str_date, '%m-%d-%Y')


def add_players():
    players_filepath = 'data/players.json'
    with open(players_filepath) as json_file:
        players_list = json.load(json_file)['players']

    cnt = 0
    for player in players_list:
        db.session.add(Player(name=player['name'],
                              birthdate=string_to_date(player['birthdate']),
                              number=player['number'],
                              email=player['email'],
                              team_id=int(player['team_id'])+1))
        cnt += 1

    db.session.commit()
    print('Added {} entries to table Players.'.format(cnt))


def add_matches():
    matches_filepath = 'data/matches.json'
    with open(matches_filepath) as json_file:
        matches_list = json.load(json_file)['matches']

    cnt = 0
    for match in matches_list:
        db.session.add(Match(date_time=string_to_date(match['date_time']),
                             host_team_id=int(match['host_team_id'])+1,
                             guest_team_id=int(match['guest_team_id'])+1,
                             host_team_goals=match.get('host_team_goals', 0),
                             guest_team_goals=match.get('guest_team_goals', 0),
                             host_team_yellow=match.get('host_team_yellow', 0),
                             guest_team_yellow=match.get('guest_team_yellow', 0),
                             host_team_red=match.get('host_team_red', 0),
                             guest_team_red=match.get('guest_team_red', 0),
                             host_team_shots=match.get('host_team_shots', 0),
                             guest_team_shots=match.get('guest_team_shots', 0)))
        cnt += 1

    db.session.commit()
    print('Added {} entries to table Matches.'.format(cnt))


def add_statistics():
    stats_filepath = 'data/statistics.json'
    with open(stats_filepath) as json_file:
        stats_list = json.load(json_file)['statistics']

    cnt = 0
    for stats in stats_list:
        db.session.add(Statistics(player_id=int(stats['player_id'])+1,
                                  match_id=int(stats['match_id'])+1,
                                  red=stats['red'],
                                  yellow=stats['yellow'],
                                  goals=stats['goals'],
                                  assists=stats['assists']))
        cnt += 1

    db.session.commit()
    print('Added {} entries to table Statistics.'.format(cnt))


def main():
    init_empty_db()
    add_news()
    add_teams()
    add_players()
    add_matches()
    add_statistics()


if __name__ == '__main__':
    main()
