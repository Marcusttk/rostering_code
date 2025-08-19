from ics import Calendar  #pip3 install ics
import json
from datetime import date, datetime, timedelta

# Open the .ics file, adjust this accordingly
desktop_file_path = "C:/Users/ace-j/Downloads/" + "FG1 OOO Calendar.ics"
laptop_file_path = "C:/Users/User/Downloads/" + "FG1 OOO Calendar.ics"
with open(desktop_file_path, "r", encoding="utf-8") as f:
    calendar = Calendar(f.read())


def read_calendar(calendar_object):
    # Loop through events
    # sample:
    # Event: des medical appt
    # Start: 2025-09-11T00:00:00+00:00
    # End: 2025-09-12T00:00:00+00:00
    for event in calendar.events:
        print("Event:", event.name)
        print("Start:", event.begin)
        print("End:", event.end)
        print("-" * 40)


# If true it means the event is after today's date
def check_date(current_date, datetime_str):
    # format of datetime_str = 2025-09-11T00:00:00+00:00
    # Convert string to datetime object
    datetime_object = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S+00:00")
    if datetime_object < current_date:
        return False
    else:
        return True


def return_dates(start_date, end_date):
    start = datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S+00:00")
    end = datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%S+00:00")
    dates = [start + timedelta(days=i) for i in range((end - start).days + 1)]
    dates_str = []
    for date_entry in dates:
        date_value_str = date_entry.strftime("%Y-%m-%d")
        date_list = date_value_str.split("-")
        dates_str.append([date_list[0], date_list[1], date_list[2]])
    return dates_str


def create_year_month_entry(ooo_dict, person):
    year = date.today().year
    if person not in ooo_dict:
        # creates a year with months 1 to 12
        ooo_dict[person] = {year: {i: {} for i in range(1, 13)}}
    else:
        # this creates a new year entry for that person
        if year not in ooo_dict[person]:
            ooo_dict[person][year] = {i: {} for i in range(1, 13)}
    return ooo_dict


# dates should be a nested list [[year], [month], [days]]
def update_ooo_dict(dates, person, ooo_dict):
    # you want to pre create everything to eliminate the need to check for years or months
    ooo_dict = create_year_month_entry(ooo_dict, person)
    # format of entries = [year, month, day]
    for entries in dates:
        ooo_dict[person][entries[0]][entries[1]] = entries[2]
    return ooo_dict


def build_calendar_dict(people_dict, ooo_dict):
    now = date.today()
    for event in calendar.events:
        relevant_event = check_date(now, event.begin)
        if relevant_event:
            for names in people_dict:
                if names in event.name:
                    dates = return_dates(event.begin, event.end)
                    # calculate dates to put in ooo_dict
                    ooo_dict = update_ooo_dict(dates, names, ooo_dict)
                else:
                    print("no person indicated in: " + event.name)
    return ooo_dict


def calculate_rosters(roster, ooo_dict):
    print(1)


def main():
    # update all shorthands in the fg1_names.json also
    people_dict = json.load(open("./fg1_names.json"))
    ooo_dict = json.load(open("./people_ooo.json"))
    ooo_dict = build_calendar_dict(people_dict, ooo_dict)

    with open("./people_ooo.json", "w") as f:
        json.dump(ooo_dict, f, indent=4)
    # ics file is deleted so that you don't have to keep changing the name to the latest copy.


if __name__ is main():
    main()

