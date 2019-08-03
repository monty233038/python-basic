import  datetime
import winsound
fr = 3200
dur = 10000
time_hr = (input('enter the hour for alarm'))
time_mi = (input('enter the minute for alarm'))
time_f = time_hr+':'+time_mi
now = datetime.datetime.now()
now_f = (now.strftime('%H:%M'))
while time_f != now_f:
    now = datetime.datetime.now()
    now_f = (now.strftime('%H:%M'))
    continue
else:
    winsound.Beep(fr, dur)
