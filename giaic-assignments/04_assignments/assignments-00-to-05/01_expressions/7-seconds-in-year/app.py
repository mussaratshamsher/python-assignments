# Problem Statement
# Use Python to calculate the number of seconds in a year, and tell the user what the result is in a nice print statement that looks like this (of course the value 5 should be the calculated number instead):
# There are 5 seconds in a year!
# You should use constants for this exercise -- there are 365 days in a year, 24 hours in a day, 60 minutes in an hour, and 60 seconds per minute.

# solution

Days_in_year:int = 365
Hours_in_day:int = 24
Minutes_in_hour:int = 60
Seconds_in_minute:int = 60

def main():
    seconds_in_year:int = Days_in_year * Hours_in_day * Minutes_in_hour * Seconds_in_minute
    print(f"There are {seconds_in_year} seconds in a year❗")

main()
