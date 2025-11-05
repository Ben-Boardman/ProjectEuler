
MONTHS = {
    "January"  :31,
    "February" :28,
    "March"    :31,
    "April"    :30,
    "May"      :31,
    "June"     :30,
    "July"     :31,
    "August"   :31,
    "September":30,
    "October"  :31,
    "November" :30,
    "December" :31
    }

DAYS = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
    ]

def count_day_occurance() -> int:
    day = 1
    count = 0
    for year in range(1900,2001):

        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            MONTHS["February"] = 29
        else:
            MONTHS["February"] = 28

        for month in MONTHS:
            if DAYS[(day % 7)-7] == "Sunday":
                if year > 1900:
                    count += 1
            print(str(day)+" "+month+" "+str(year)+" Count: "+str(count))
            day += MONTHS[month]

print(count_day_occurance())