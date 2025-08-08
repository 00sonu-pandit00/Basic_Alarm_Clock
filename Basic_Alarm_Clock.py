import datetime
import time
import os
try:
    import winsound
    beep = lambda: winsound.Beep(1000, 1000)
except ImportError:
    beep = lambda: print("\a")

alarm_time = input("Set alarm (HH:MM:SS): ")

while True:
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if current_time == alarm_time:
        print("Wake up!")
        beep()
        break
    time.sleep(1)
