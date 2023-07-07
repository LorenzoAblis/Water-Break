import schedule
import time
from winotify import Notification

def notify_on_start():
    notification = Notification(app_id='Water Break Reminder', title='Time to Drink Water', msg='Water Break Script is running!', duration='long')
    notification.build().show()

def drink_water():
    notification = Notification(app_id='Water Break Reminder', title='Time to Drink Water', msg='Remember to drink water now!', duration='long')
    notification.build().show()

def notify_at_times():
    times = ["11:00", "12:00", "13:00", "14:00", "15:00", "16:00", "17:00", "18:00"]

    for t in times:
        schedule.every().day.at(t).do(drink_water)

    while True:
        schedule.run_pending()
        time.sleep(1)

notify_on_start()
notify_at_times()