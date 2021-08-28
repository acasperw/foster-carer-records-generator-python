from datetime import datetime, timedelta

def suffix(d):
    return 'th' if 11 <= d <= 13 else {1: 'st', 2: 'nd', 3: 'rd'}.get(d % 10, 'th')

def custom_strftime(t, includeYear):
  if(includeYear):
    format = '%B {S}, %Y'
  else:
    format = '{S} %B'
  return t.strftime(format).replace('{S}', str(t.day) + suffix(t.day))

##
# Python's program to get start and end of week
def getStartOfWeek(date_str):
  date_obj = datetime.strptime(date_str, '%Y-%m-%d')
 
  start_of_week = date_obj - timedelta(days=date_obj.weekday())  # Monday
  # end_of_week = start_of_week + timedelta(days=6)  # Sunday
  return start_of_week
