"""
Write a function that calculates the number of Friday 13ths in a given year.

Input: a year after 1752
Output: int representing the number of Friday 13ths in that year

Rules:
- assume future years will still use Gregorian calendar

Algorithm:
1. Initialise count to 0
2. Iterate over the months
3. For each iteration build the date 13th of that month and the given year
4. Get the day of that date
5. If the day is a Friday, increment my count
6. Return the count
"""
import datetime

ISO_FRIDAY = 5

def friday_the_13ths(year):
    count = 0

    for month in range(1, 13):
        date = datetime.date(year, month, 13)
        day = date.isoweekday()
        if day == ISO_FRIDAY:
            count += 1

    return count


print(friday_the_13ths(1986) == 1)      # True
print(friday_the_13ths(2015) == 3)      # True
print(friday_the_13ths(2017) == 2)      # True