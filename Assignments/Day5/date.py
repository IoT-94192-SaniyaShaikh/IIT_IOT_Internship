#  Write a Python program that:
# Imports the datetime module
# Displays the current date and time
# Prints the day of the week for the current date

import datetime
now = datetime.datetime.now()
print("current date and time is:",now)
print("Day of the week:", now.strftime("%A"))

