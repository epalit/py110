"""
# Problem
- input: integer (positive or negative)
- output: string format hh:mm

requirements:
- return the time in the format hh:mm
- use 24hr format
- convert from minutes before/after midnight
- do not use datetime module
- positive means after midnight
- negative means before midnight
- 0 means midnight

# Examples
print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True

# Data
calculate with numbers, then format to string

# Algorithm
1. Adjust the mins to be within the mins range of a 24hr day
2. Calculate the hours
3. Calculate mins
3. Format result to be HH:MM
5. Return result
"""

HOURS_IN_DAY = 24
MINS_IN_HOUR = 60
MINS_IN_24_HRS = HOURS_IN_DAY * MINS_IN_HOUR

def get_day_adjusted_mins(mins):
    return mins % MINS_IN_24_HRS

def get_hours_and_mins(mins):
    hours = mins // MINS_IN_HOUR
    remaining_mins = mins % MINS_IN_HOUR
    return hours, remaining_mins

def format_time(hours, mins):
    return f"{hours:02d}:{mins:02d}"

def time_of_day(mins):
    adjusted_mins = get_day_adjusted_mins(mins)
    hours, mins = get_hours_and_mins(adjusted_mins)

    return format_time(hours, mins)


print(time_of_day(0) == "00:00")        # True
print(time_of_day(-3) == "23:57")       # True
print(time_of_day(35) == "00:35")       # True
print(time_of_day(-1437) == "00:03")    # True
print(time_of_day(3000) == "02:00")     # True
print(time_of_day(800) == "13:20")      # True
print(time_of_day(-4231) == "01:29")    # True