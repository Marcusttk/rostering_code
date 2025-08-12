from ics import Calendar

# Open the .ics file
with open("C:/Users/User/Downloads/FG1 OOO Calendar (1).ics", "r", encoding="utf-8") as f:
    calendar = Calendar(f.read())

# Loop through events
for event in calendar.events:
    print("Event:", event.name)
    print("Start:", event.begin)
    print("End:", event.end)
    print("Location:", event.location)
    print("-" * 40)