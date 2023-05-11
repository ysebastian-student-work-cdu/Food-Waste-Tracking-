import random
from datetime import datetime, timedelta

def generate_dates():
    start_date = datetime.strptime("17-Apr-21", "%d-%b-%y")
    end_date = datetime.strptime("6-May-23", "%d-%b-%y")
    date_list = [start_date]
    while len(date_list) < 300 and date_list[-1] < end_date:
        days_to_add = int(random.expovariate(1/7)) + 1
        new_date = date_list[-1] + timedelta(days=days_to_add)
        num_duplicates = min(int(random.expovariate(1/2)), 10)
        date_list.extend([new_date] * num_duplicates)
        date_list.append(new_date)
    date_list = sorted(date_list)[:300] # truncate to 300 dates
    with open("dates.txt", "w") as f:
        for date in date_list:
            f.write(date.strftime("%d-%b-%y") + "\n")
    return date_list

generate_dates()