import time
from plyer import notification

if __name__ == "__main__":
    while True:
        
        #notify(title='', message='', app_name='', app_icon='', timeout=10, ticker='', toast=False)
        notification.notify(title = "Reminder : Drink Water",
                        message= "To prevent dehydration,Health authorities commonly recommend eight 8-ounce glasses, which equals about 2 liters, or half a gallon.",
                        app_name="WaterReminder",
                        #app_icon="water_drink_bottle_icon.ico",
                        timeout=10
                        )
        time.sleep(60*60)

#open Terminal -> run -> pythonw.exe ./WaterReminder.py
