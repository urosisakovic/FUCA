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
    for news in news_list:
        db.session.add(News(title=news['title'], content=news['content']))
    db.session.commit()
    print('Added News.')


def add_teams():
    teams_filepath = 'data/teams.json'
    with open(teams_filepath) as json_file:
        teams_list = json.load(json_file)['teams']
    for team in teams_list:
        db.session.add(Team(name=team['name'],
                            matches=team['matches'],
                            wins=team['wins'],
                            losses=team['losses'],
                            draws=team['draws'],
                            goal_diff=team['goal_diff'],
                            captain_id=team['captain_id']))
    db.session.commit()
    print('Added Teams')


def string_to_date(str_date):
    return datetime.strptime(str_date, '%m-%d-%Y')


def add_players():
    players_filepath = 'data/players.json'
    with open(players_filepath) as json_file:
        players_list = json.load(json_file)['players']
    for player in players_list:
        db.session.add(Player(name=player['name'],
                              birthdate=string_to_date(player['birthdate']),
                              number=player['number'],
                              email=player['email'],
                              team_id=player['team_id']))
    db.session.commit()
    print('Added Players.')


def add_matches():
    matches_filepath = 'data/matches.json'
    with open(matches_filepath) as json_file:
        matches_list = json.load(json_file)['matches']
    for match in matches_list:
        db.session.add(Match(date_time=string_to_date(match['date_time']),
                             host_team_id=match['host_team_id'],
                             guest_team_id=match['guest_team_id'],
                             host_team_goals=match.get('host_team_goals', 0),
                             guest_team_goals=match.get('guest_team_goals', 0),
                             host_team_yellow=match.get('host_team_yellow', 0),
                             guest_team_yellow=match.get('guest_team_yellow', 0),
                             host_team_red=match.get('host_team_red', 0),
                             guest_team_red=match.get('guest_team_red', 0),
                             host_team_shots=match.get('host_team_shots', 0),
                             guest_team_shots=match.get('guest_team_shots', 0)))
    db.session.commit()
    print('Added Matches.')


def add_statistics():
    stats_filepath = 'data/statistics.json'
    with open(stats_filepath) as json_file:
        stats_list = json.load(json_file)['statistics']
    for stats in stats_list:
        db.session.add(Statistics(player_id=stats['player_id'],
                                  match_id=stats['match_id'],
                                  red=stats['red'],
                                  yellow=stats['yellow'],
                                  goals=stats['goals'],
                                  assists=stats['assists']))
    db.session.commit()
    print('Added Statistics.')


def main():
    init_empty_db()
    add_news()
    add_teams()
    add_players()
    add_matches()
    add_statistics()


if __name__ == '__main__':
    main()
