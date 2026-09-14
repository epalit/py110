"""
# Problem
input: string representing 24h time of day
output: int representing number of minutes before/after midnight

requirements:
- return value in the range 0 through 1439
- do not use datetime module

# Examples
print(before_midnight("00:00") == 0)    # True
print(before_midnight("12:34") == 686)  # True
print(before_midnight("24:00") == 0)    # True

# Data
convert string to ints then calculate

# Algorithm
1. Get mins from time:
  a. Split string on colon
  b. Convert hours and mins to ints
  c. Sum them and return
2. Convert negative for before
3. Normalise to range 1440
"""

MINS_IN_HOUR = 60
HOURS_IN_DAY = 24
MINS_IN_DAY = MINS_IN_HOUR * HOURS_IN_DAY

def get_mins_from_time(time_str):
    split_time = time_str.split(":")
    hours, mins = int(split_time[0]), int(split_time[1])
    total_mins = (hours * MINS_IN_HOUR) + mins
    return total_mins

def before_midnight(time_str):
    total_mins = -(get_mins_from_time(time_str))
    return total_mins % MINS_IN_DAY

def after_midnight(time_str):
    total_mins = get_mins_from_time(time_str)
    return total_mins % MINS_IN_DAY

print(after_midnight("00:00") == 0)     # True
print(before_midnight("00:00") == 0)    # True
print(after_midnight("12:34") == 754)   # True
print(before_midnight("12:34") == 686)  # True
print(after_midnight("24:00") == 0)     # True
print(before_midnight("24:00") == 0)    # True