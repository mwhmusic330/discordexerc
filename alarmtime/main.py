"""

You’re setting an alarm for the next morning and know how long you want to sleep.
Your job is to figure out what time you need to go to bed to get that amount of sleep.

Each input has two parts:

    The alarm time (when you’ll wake up).

    The sleep duration (how long you want to sleep). 

Return the time you should go to bed — in 24-hour format ("HH:MM").

bedTime(["07:50", "07:50"])
output = ["00:00"]

bedTime(["06:15", "10:00"], ["08:00", "10:00"], ["09:30", "10:00"])
output = ["20:15", "22:00", "23:30"]


bedTime(["05:45", "04:00"], ["07:10", "04:30"])
output = ["01:45", "02:40"]

"""

def bedTime(*times) -> list[str]:
    result = []
    for alarm, duration in times:
        ah, am = alarm.split(":")
        alarm_minutes = int(ah) * 60 + int(am)

        dh, dm = duration.split(":")
        duration_minutes = int(dh) * 60 + int(dm)

        bed_minutes = (alarm_minutes - duration_minutes) % 1440

        bed_time = f"{bed_minutes // 60:02d}:{bed_minutes % 60:02d}"

        result.append(bed_time)

    return result 


def main():

    output = bedTime(["07:50", "07:50"])
    print(output)


    output = bedTime(["06:15", "10:00"], ["08:00", "10:00"], ["09:30", "10:00"])
    print(output)


    output = bedTime(["05:45", "04:00"], ["07:10", "04:30"])
    print(output)


if __name__ == '__main__':
    main()
