from datetime import datetime, timedelta

def get_upcoming_birthdays (d, weekday:int):

    days_ahead = weekday - d.weekday()
    if days_ahead < 0:
        days_ahead +=7
    return d + timedelta(days = days_ahead)

users = [
    {"name": "John Doe", "birthday": "1985.03.30"},
    {"name": "Jane Smith", "birthday": "1990.01.27"},
    {"name": "Will Smith", "birthday": "1995.03.31"},
    {"name": "Kate Smith", "birthday": "1987.04.02"},
    {"name": "Anna Smith", "birthday": "1997.05.17"}
]

new_users = []
for user in users:
    try:
        new_date = datetime.strptime(user['birthday'], '%Y.%m.%d').date()
        new_users.append({"name": user['name'], 'birthday': new_date})
    except ValueError:
        print(f'Некоректна дата народження для користувача {user["name"]}')

days = 7
today = datetime.today().date()

upcoming_birthdays = []
for user in new_users:
    birthday_this_year = user["birthday"].replace(year=today.year)

    if birthday_this_year < today:
        birthday_this_year = birthday_this_year.replace(year=today.year + 1)

    if 0 <= (birthday_this_year - today).days <= days:
        if birthday_this_year.weekday() >= 5:
            birthday_this_year = get_upcoming_birthdays(birthday_this_year, 0)

        congratulation_date_str = birthday_this_year.strftime('%Y.%m.%d')
        upcoming_birthdays.append({
            "name": user["name"],
            "congratulation_date": congratulation_date_str
        })

print(upcoming_birthdays)