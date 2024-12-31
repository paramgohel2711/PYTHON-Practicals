import datetime

dt = input("Enter Date In dd/MM/YYYY Format: ")
l = dt.split("/")
date = datetime.date(int(l[2]), int(l[1]), int(l[0]))
# Format the date to MM-DD-YYYY
fdate = date.strftime("%m-%d-%Y")
print(fdate)
