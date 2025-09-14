from ics import Calendar  # pip3 install ics
import json
from datetime import date, datetime, timedelta
import math
import random
import os

# Adjust this accordingly based on computer file path
desktop_file_path = "C:/Users/ace-j/Downloads/"
laptop_file_path = "C:/Users/User/Downloads/"
# check which file path exists so that you don't need to keep switching when working on desktop or laptop
if os.path.exists(desktop_file_path):
    file_path = desktop_file_path + "FG1 OOO Calendar.ics"
elif os.path.exists(laptop_file_path):
    file_path = laptop_file_path + "FG1 OOO Calendar.ics"
with open(file_path, "r", encoding="utf-8") as f:
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
    datetime_str = str(datetime_str).split("T")[0]
    datetime_object = datetime.strptime(str(datetime_str), "%Y-%m-%d")
    # Convert datetime to date
    date_only = datetime_object.date()
    if date_only < current_date:
        return False
    else:
        return True


def return_dates(start_date, end_date):
    start_str = str(start_date).split("T")[0]
    start = datetime.strptime(start_str, "%Y-%m-%d")
    end_str = str(end_date).split("T")[0]
    end = datetime.strptime(end_str, "%Y-%m-%d")
    dates = [start + timedelta(days=i) for i in range((end - start).days)]
    dates_str = []
    for date_entry in dates:
        date_value_str = date_entry.strftime("%Y-%m-%d")
        date_list = date_value_str.split("-")
        dates_str.append([int(date_list[0]), int(date_list[1]), int(date_list[2])])
    return dates_str


def create_year_month_entry(ooo_dict, person):
    year = date.today().year
    if person not in ooo_dict:
        ooo_dict[person] = {}
    for y in [year, year + 1]:
        if str(y) not in ooo_dict[person]:
            ooo_dict[person][str(y)] = {str(m): {} for m in range(1, 13)}
    return ooo_dict


# dates should be a nested list [[year], [month], [days]]
def update_ooo_dict(dates, person, ooo_dict):
    ooo_dict = create_year_month_entry(ooo_dict, person)
    for year, month, day in dates:
        year, month, day = str(year), str(month), str(day)
        if day not in ooo_dict[person][year][month]:
            ooo_dict[person][year][month][day] = 0
    return ooo_dict


def build_calendar_dict(people_dict, ooo_dict):
    now = date.today()
    for event in calendar.events:
        relevant_event = check_date(now, event.begin)
        if relevant_event:
            name_found = False
            for names in people_dict:
                if names in str(event.name).lower():
                    dates = return_dates(event.begin, event.end)
                    # calculate dates to put in ooo_dict
                    ooo_dict = update_ooo_dict(dates, people_dict[names], ooo_dict)
                    name_found = True
                    break
            if not name_found:
                print("no person indicated in: " + event.name)
    return ooo_dict


# TODO this algo needs to change
# this function runs when someone in their planned shift is unavailable
def roster_shuffle(order, people_to_swap, dates_list, people_ooo):
    while not people_to_swap:
        random.shuffle(order)
        people_to_swap = check_their_availability(order, dates_list, people_ooo)
    return order


# dates will be a list of [ [year, month, day], [year, month, day], ...]
def is_available(person, people_ooo, date):
    available = True
    if date[0] in people_ooo[person]:
        if date[1] in people_ooo[person][date[0]]:
            if date[2] in people_ooo[person][date[0]][date[1]]:
                available = False
    return available


# example usage:
# print(swap_with_nearest(items, 2, is_available))
# swaps item at index 2 ith nearest available (index 3)
def swap_with_nearest(order, target_index, people_ooo, dates):
    def check_and_arrange():
        availability = True
        for date1 in dates:
            availability = is_available(order[left], people_ooo, date1)
            if not availability:
                break
        if availability:
            order[target_index], order[left] = order[left], order[target_index]
        return order

    n = len(order)

    # Check outward from the target index
    for offset in range(1, n):
        left = target_index - offset
        right = target_index + offset
        if right >= n:  # to prevent index error when the count exceeds the max number of items
            right -= n - 1

        if left >= 0:
            order = check_and_arrange()

        if right < n:
            order = check_and_arrange()

    # No swap found
    return order


def roster_shuffler(order, people_to_swap, dates_list, people_ooo):
    number_of_swaps = len(people_to_swap)
    if number_of_swaps > 0:
        if number_of_swaps == 1:
            target_index = order.index(people_to_swap[0])
            swap_with_nearest(order, target_index, people_ooo, date)
        elif number_of_swaps >= 2:
            print("See if they can swap with each other")
            print("if unable to, implement nearest neighbour swap for all of them")
    return order


# TODO can be optimised further, this is slow if there is one person who cannot make it
def check_their_availability(order, dates_list, people_ooo):
    count = 0
    people_who_need_to_swap = []
    for people in order:
        if people not in people_ooo:
            print(people + " is not in people_ooo")
        else:
            for dates in dates_list[count]:
                if str(dates[2]) in people_ooo[people][str(dates[0])][str(dates[1])]:
                    people_who_need_to_swap.append(people)
        count += 1
    return people_who_need_to_swap


def build_dates_list(start_date, days_of_the_week, repeats):
    all_days = []
    for times in range(repeats):
        days_this_week = []
        for days in days_of_the_week:
            new_date = start_date + timedelta(days=int(days))
            days_this_week.append([new_date.year, new_date.month, new_date.day])
        all_days.append(days_this_week)
        start_date += timedelta(days=int(7))
    return all_days


# duration needs to be measured in terms of weeks
def compute_repeats(people_involved, duration):
    count = len(people_involved)
    if count >= 12:
        repeats = count
    else:
        repeats = math.ceil(duration / count) * count
    return repeats


# TODO this function needs to be fixed, code is a bit messy
def create_schedule(order, all_dates, repeats):
    roster_solution = {}
    loops = int(repeats / len(order))
    for loop in range(loops):
        for count in range(len(order)):
            person = order[count]
            for date_list in all_dates[count * (loop + 1)]:
                date_list_str = str(date_list[2]) + "-" + str(date_list[1]) + "-" + str(date_list[0])
                roster_solution[date_list_str] = person
    # print(roster_solution)
    return roster_solution


# TODO right now the code doesn't account for the fact that 1 ooo in the week isn't a big deal.
# the roster should also be your fg1_rosters["team"]. It's specific to the team
# start date should be [year,month,day]
def calculate_rosters(roster, ooo_dict, start_date):
    date_to_check = datetime(start_date[0], start_date[1], start_date[2])
    if date_to_check.weekday() != 0:  # mon = 0 , sunday = 6
        print("Start date should be a monday!")
        exit()
    else:
        start_dt_str = str(start_date[0]) + "-" + str(start_date[1]) + "-" + str(start_date[2])
        start = datetime.strptime(start_dt_str, "%Y-%m-%d")
        # duration for now will be toggled to 3 months or 3 full cycles, whichever is longer
        # if it's longer than 3 months will round up to completion of next cycle.
        duration = 12  # number of weeks, can be adjusted
        repeats = compute_repeats(roster["order"], duration)
        all_days = build_dates_list(start, roster["applicable days"], repeats)
        people_to_swap = check_their_availability(roster["order"], all_days, ooo_dict)
        # only bother to run swapping algo if there is one person who is unable to make it.
        if people_to_swap:
            new_order = roster_shuffle(roster["order"], people_to_swap, all_days, ooo_dict)
        else:
            new_order = roster["order"]
        roster_solution = create_schedule(new_order, all_days, repeats)
        for items in roster_solution:
            roster["dates"][items] = roster_solution[items]
    return roster


def main():
    # update all shorthands in the fg1_names.json also
    people_dict = json.load(open("./fg1_names.json"))
    ooo_dict = json.load(open("./people_ooo.json"))
    rosters = json.load(open("./fg1_rosters.json"))
    ooo_dict = build_calendar_dict(people_dict["all"], ooo_dict)
    start_date = [2025, 9, 8]
    rosters["pnw"] = calculate_rosters(rosters["pnw"], ooo_dict, start_date)
    with open("./people_ooo.json", "w") as file:
        json.dump(ooo_dict, file, indent=4)
    with open("./fg1_rosters.json", "w") as file:
        json.dump(rosters, file, indent=4)
    # ics file is deleted so that you don't have to keep changing the name to the latest copy.


if __name__ is main():
    main()
