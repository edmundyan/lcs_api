import json
import sys

# local
import helper
def main():
  with open('data/riot.json') as fp:
    j = fp.read()

  obj = json.loads(j)

  players = obj['proPlayers']
  teams = obj['proTeams']
  teams_dict = {}

  for tid, team in teams.iteritems():
    t = Team()
    t.loadJson(team)
    teams_dict[tid] = t
    t.print_csv()



  for pid, player in players.iteritems():
    p = Player()
    p.loadJson(player)
    p.print_csv()


class Player(object):
  def __init__(self, attr={}):
    self.id = None
    self.name = None
    self.team = None
    self.position = None

    self.kills = None
    self.deaths = None
    self.assists = None
    self.minion_kills = None

  def loadJson(self, obj):
    self.id = obj['id']
    self.name = obj['name']
    self.team = helper.team_lookup(obj['proTeamId'])
    self.position = ','.join(obj['positions'])

    self.kills = helper.aggStatsByWeek(obj['statsByWeek'],
                                       range(1,12),
                                       'kills',
                                       'projectedValue')
    self.deaths = helper.aggStatsByWeek(obj['statsByWeek'],
                                       range(1,12),
                                       'deaths',
                                       'projectedValue')
    self.assists = helper.aggStatsByWeek(obj['statsByWeek'],
                                       range(1,12),
                                       'assists',
                                       'projectedValue')
    self.minion_kills = helper.aggStatsByWeek(obj['statsByWeek'],
                                       range(1,12),
                                       'minionKills',
                                       'projectedValue')

  def print_csv(self, out=sys.stdout):
    arr = [str(s) for s in [self.team, self.name, self.position, self.kills, self.deaths, self.assists, self.minion_kills]]
    print ", ".join(arr)

class Team(object):
  def __init__(self):
    self.id = None
    self.name = None
    self.short_name = None

    self.wins = None
    self.barons = None
    self.dragons = None
    self.f_bloods = None
    self.towers = None

  def loadJson(self, obj):
    self.id = obj['id']
    self.name = obj['name']
    self.short_name = obj['shortName']



  def print_csv(self, out=sys.stdout):
    print "%s: '%s'" %(self.id, self.short_name)









if __name__ == "__main__":
  main()

