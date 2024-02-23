import datetime 
today = datetime.datetime.now()
somesecago = today - datetime.timedelta(seconds = 50)
diff = today - somesecago
print(diff)