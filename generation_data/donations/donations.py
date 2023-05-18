import random
import csv
import datetime

# set range for number of records to generate
num_records = random.randint(9000, 10000)

# set date range
start_date = datetime.date(2021, 4, 17)
end_date = datetime.date(2023, 5, 6)
delta = datetime.timedelta(days=1)

# create list of possible org IDs
org_ids = list(range(1, 135))

# create list to store records
records = []

# generate records
for i in range(num_records):
    # select random org ID
    org_id = random.choice(org_ids)

    # generate donation date
    if i == 0:
        donation_date = start_date
    else:
        # check 30% chance of same date as previous record
        if random.random() < 0.3:
            donation_date = records[-1]["donationDate"]
        else:
            donation_date = records[-1]["donationDate"] + delta

        # ensure donation date is within range
        if donation_date > end_date:
            break

    # add record to list
    records.append({"donationID": i+1, "orgID": org_id, "donationDate": donation_date})

# write records to CSV file
with open("donations.csv", "w", newline="") as csvfile:
    fieldnames = ["donationID", "orgID", "donationDate"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for record in records:
        writer.writerow(record)
