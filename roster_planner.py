from ics import Calendar  #pip3 install ics
import json


# Open the .ics file, adjust this accordingly
desktop_file_path = "C:/`Users\ace-j/Downloads" + "FG1 OOO Calendar.ics"
laptop_file_path = "C:/Users/User/Downloads/" + "FG1 OOO Calendar.ics"
with open(laptop_file_path, "r", encoding="utf-8") as f:
    calendar = Calendar(f.read())

def read_calendar(calendar_object):
    # Loop through events
    for event in calendar.events:
        print("Event:", event.name)
        print("Start:", event.begin)
        print("End:", event.end)
        print("Location:", event.location)
        print("-" * 40)


def build_calendar_dict(calendar_object, people_dict):
    for event in calendar.events:

def update_calendar(calendar_dict):
    availability = json.load(open("./people_ooo.json"))


def main():
    # update all shorthands in the fg1_names.json also
    people_dict = json.load(open("./fg1_names.json"))
    print(1)
    # ics file is deleted so that you don't have to keep changing the name to the latest copy.


if __name__ is main():
    main()

