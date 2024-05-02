#https://cs50.harvard.edu/python/2022/psets/3/outdated/

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
while True:
    try:
        date = input("Date: ")
        if date.find("/") == -1:
            month, day, year = date.split(" ")
            if month in months and day.find(",") != -1:
                dd = day.replace(",", "").zfill(2)
                mm = str((months.index(month) + 1)).zfill(2)
                yyyy = int(year)
        else:
            month, day, year = date.split("/")
            dd = day.zfill(2)
            mm = month.zfill(2)
            yyyy = int(year)
        if int(dd) < 31 and int(mm) <= 12:
            break
    except (ValueError, NameError):
        pass
print(f"{yyyy}-{mm}-{dd}")


