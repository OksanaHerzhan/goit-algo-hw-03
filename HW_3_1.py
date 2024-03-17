# завдання_1 з використанням функції

from datetime import datetime

def get_days_from_today(first_date:datetime)->int:
    date_nows = datetime.today()
    return date_nows.toordinal()-first_date.toordinal()

incur_input = True
while incur_input:
    user_date_str = input("Input date as YYYY.MM.DD:  ")
    try:
        user_date = datetime.strptime(user_date_str, "%Y.%m.%d")
        incur_input = False
    except ValueError:
        print("Error - Incorect data input")
        incur_input = True

date_diff = get_days_from_today(user_date)
print(f"Days from today: {date_diff}")


# завдання_1 без використання функції

from datetime import datetime
first_date = datetime (year=1989, month=5, day=2)
date_nows = datetime.today()

days_since = date_nows.toordinal() - first_date.toordinal()
print (days_since)