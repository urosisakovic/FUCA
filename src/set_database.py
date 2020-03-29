import os
from datetime import datetime
from fuca import db
from fuca.models import Match, News, Player, Statistics, Team

# remove site.db
if os.path.exists('fuca/site.db'):
    print("Removed site.db")
    os.remove('fuca/site.db')

# create db
db.create_all()

# add news
news = News(title='t1', content='c1')
print(news)

db.session.add(news)
db.session.commit()

print(News.query.all())

# add teams
team1 = Team(name='rekreativo')
team2 = Team(name='ynwa')

db.session.add(team1)
db.session.add(team2)
db.session.commit()

print(Team.query.all())

# add players
player = Player(name='viki',
                birthdate=datetime.now(),
                image='default.jpg',
                email='viki@gmail.com',
                password='uros',
                team_id=1)
print(player)

db.session.add(player)
db.session.commit()

print(Player.query.all())

# add matches
match = Match(host_team=team1,
              guest_team=team2)

db.session.add(match)
db.session.commit()

print(Match.query.all())


# add statistics
stats = Statistics(goals=5,
                   assists=2,
                   experience=100,
                   yellow=1,
                   red=0,
                   player_id=1,
                   match_id=1)

db.session.add(stats)
db.session.commit()

print(Statistics.query.all())
