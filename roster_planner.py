from ics import Calendar  #pip3 install ics
import json
from datetime import date, datetime

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
    datetime_object = datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S")
    if datetime_object < current_date:
        return False
    else:
        return True


# dates should be a nested list [[year], [month], [days]]
def update_people_dict(dates, person, ooo_dict):
    if person not in ooo_dict:
        ooo_dict[person] = {}
    for years in dates[0]:
        if years not in ooo_dict[person]:
            ooo_dict[person][years] = {}
        for months


def build_calendar_dict(calendar_object, people_dict, ooo_dict):
    now = date.today()
    for event in calendar.events:
        relevant_event = check_date(now, event.begin)
        if relevant_event:
            for names in people_dict:
                if names in event.name:
                    # calculate dates to put in ooo_dict
                    print(1)
                    update_people_dict()
                else:
                    print("no person indicated in: " + event.name)


def update_calendar(calendar_dict):
    availability = json.load(open("./people_ooo.json"))


def main():
    # update all shorthands in the fg1_names.json also
    people_dict = json.load(open("./fg1_names.json"))
    ooo_dict = json.load(open("./people_ooo.json"))
    print(1)
    # ics file is deleted so that you don't have to keep changing the name to the latest copy.


if __name__ is main():
    main()

