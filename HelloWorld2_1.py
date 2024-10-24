import sys
import datetime
import random 

#Version and Date stuff
print(sys.version)
DATE_CURRENT = str(datetime.datetime.now())
print(DATE_CURRENT)

#Creating year, month and day variables from DATE_CURRENT variable
YEAR_CURRENT = DATE_CURRENT[:4]
MONTHS_ALL = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
MONTH_CURRENT = MONTHS_ALL[(int(DATE_CURRENT[5:7])-1)]
DAY_CURRENT = DATE_CURRENT[8:10]

#A variable indicating current version of python and when it was released
VERSION_CURRENT = (str(sys.version))[:6]
VERSION_CURRENT_RELEASE_DATE_WIP = (str(sys.version))[30:41]

#Getting rid of extra space between the month and date in version release date
VERSION_CURRENT_RELEASE_DATE = VERSION_CURRENT_RELEASE_DATE_WIP[:4] + VERSION_CURRENT_RELEASE_DATE_WIP[5:]
 
#Outputting the date and version
print("Today is " + DAY_CURRENT + " of " + MONTH_CURRENT + ". The year is " + YEAR_CURRENT + ".\nThe version of Python that is used to print this code is " + VERSION_CURRENT + ", which was released in " + VERSION_CURRENT_RELEASE_DATE + ".")

