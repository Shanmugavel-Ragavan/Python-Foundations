# Date Time Functions in Python

# Python datetime module is provided in Python to work with dates and times. A date in Python is not a data type of its own, but we can import a module named datetime to work with dates as date objects. These classes provide a number of functions to deal with dates, times and time intervals.

# Here are some examples of common date and time-related functions in Python:

# datetime.now(): Returns the current date and time.
# datetime.date(): Returns date object of today's date.
# datetime.time(): Returns the current time.
# datetime.datetime(): Returns the current date and time as a datetime object.
# datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0): Represents the difference between two date or time values.
# The strftime() function is used to convert date and time objects to their string representation.
#       Syntax :
#            strftime ( format )


# List of format codes

# Directive	Description	Example
# %A	Weekday full name	Monday
# %a	Weekday short name	Mon
# %d	Day of month (1-31)	26
# %b	Month of short name	Dec
# %B	Month of full name	December
# %Y	Year of full version , without century	2022
# %y	Year of short version	22
# %w	Weekday as a number ( 0-Sun , 1-Mon , 2-Tue , 3-Wed , 4-Thu , 5-Fri , 6-Sat )	1(Monday)
# %W	Week number of Year ( Monday as the first day of week ( 00-53 ) )	48
# %m	Month as a Number ( 1(Jun) - 12(Dec) )	12(Dec)
# %H	Hours ( 00-23 )	15
# %M	Minute ( 00-59 )	50
# %S	Second ( 00-59 )	23
# %p	PM / AM	PM
# %c	Local version of date and time	Mon Dec 26 15 : 50 : 23 2022
# %X	Local version of time	15:50:23
# %x	Local version of date	12/26/22


# Date Time in Python

from datetime import date, datetime, time, timedelta

# Current Date
current_date = date.today()
print("Current Date:", current_date)

# Create a specific date
new_date = date(2025, 10, 10)
print("\nNew Date:", new_date)
print("Year:", new_date.year)
print("Month:", new_date.month)
print("Day:", new_date.day)

# Time Object
new_time = time(10, 45, 5, 555505)
print("\nTime:", new_time)
print("Hour:", new_time.hour)
print("Minute:", new_time.minute)
print("Second:", new_time.second)
print("Microsecond:", new_time.microsecond)

# Current DateTime
current_datetime = datetime.now()
print("\nCurrent DateTime:", current_datetime)

# Create Specific DateTime
specific_datetime = datetime(2024, 12, 28, 12, 2, 10)
print("\nSpecific DateTime:", specific_datetime)
print("Date part:", specific_datetime.date())
print("Time part:", specific_datetime.time())

# Difference Between Two Dates
current = datetime.now()
new_year = datetime(2025, 1, 1)
difference = new_year - current

print("\nTime Remaining Until New Year 2025:")
print(difference)

# You can also access:
print("Days:", difference.days)
print("Seconds:", difference.seconds)

# Formatting DateTime using strftime()
current = datetime.now()
formatted_date = current.strftime("%A, %B %d, %Y")
formatted_time = current.strftime("%I:%M:%S %p")

print("\nFormatted Date:", formatted_date)
print("Formatted Time:", formatted_time)

# Using timedelta
future_date = current + timedelta(days=10, hours=5)
print("\nFuture Date (After 10 days & 5 hours):", future_date)
