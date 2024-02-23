import datetime 
today = datetime.datetime.now()
yesterday = datetime.datetime.now() - datetime.timedelta(days = 1)
tomorrow = today + datetime.timedelta(days = 1)
print(yesterday)
print(today)
print(tomorrow)