duration = int(input('Введите число '))
one_min = 60
one_hour = one_min * 60
one_day = one_hour * 24
if duration < one_min:
    print(duration, "сек")
elif duration > one_min and duration < one_hour:
    min = duration//one_min
    sec = duration % one_min
    print(min, "мин", sec, "сек")
elif duration >= one_hour and duration < one_day:
    hour = duration//one_hour
    duration = duration % one_hour
    min = duration//one_min
    sec = duration % one_min
    print(hour, "час", min, "мин", sec, "сек")
elif duration >= one_day:
    day = duration // one_day
    duration = duration % one_day
    hour = duration//one_hour
    duration = duration % one_hour
    min = duration//one_min
    sec = duration % one_min
    print(day, "дн", hour, "час", min, "мин", sec, "сек")
