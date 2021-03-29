import datetime

def calc_age(barth_day, today):
        barth_day = datetime.datetime.strptime(barth_day, '%Y/%m/%d')
        barth_day = barth_day.date()
        age = today.year - barth_day.year
        if (today.month, today.day) < (barth_day.month, barth_day.day):
            age -= 1
        return age