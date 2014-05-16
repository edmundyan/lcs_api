TEAMS = {
  49: 'SK',
  50: 'FNC',
  51: 'GMB',
  52: 'ALL',
  53: 'SHC',
  54: 'CW',
  55: 'ROC',
  56: 'MIL',
  57: 'TSM',
  58: 'CLG',
  59: 'DIG',
  60: 'CRS',
  61: 'C9',
  62: 'EG',
  63: 'COL',
  64: 'LMQ'
}

def team_lookup(id):
  return TEAMS[id]


def aggStatsByWeek(obj, irange, stat_key, type_key):
  total = 0
  for i in irange:
    total += obj[str(i)][stat_key][type_key]
  return total

