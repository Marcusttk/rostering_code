from ics import Calendar
import json

# update all shorthands in the fg1_names.json also
people_dict = json.load(open("./fg1_names.json"))
# Open the .ics file
with open("C:/Users/User/Downloads/FG1 OOO Calendar (1).ics", "r", encoding="utf-8") as f:
    calendar = Calendar(f.read())

def read_calendar(calendar_object):
    # Loop through events
    for event in calendar.events:
        print("Event:", event.name)
        print("Start:", event.begin)
        print("End:", event.end)
        print("Location:", event.location)
        print("-" * 40)


def build_calendar_dict(calendar_object):
    for event in calendar.events:

def update_calendar(calendar_dict):
    availability = json.load(open("./people_ooo.json"))


def main():
    print(1)


if __name__ is main():
    main()

