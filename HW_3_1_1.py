from datetime import datetime

def get_days_from_today(date):
    date_obj = datetime.strptime(date, '%Y-%m-%d')
    current_date = datetime.today()
    delta = current_date - date_obj
    return delta.days
date = '2024-02-01'
result = get_days_from_today(date)
print(f"Number of days between {date} and today: {result}")