from datetime import date

# get user input
dob_str = input("Please enter your date of birth (MM/DD/YYYY): ")

# convert input string to date object
try:
    dob_month, dob_day, dob_year = map(int, dob_str.split("/"))
    dob = date(dob_year, dob_month, dob_day)
except ValueError:
    print("Error: Invalid date format. Please enter your date of birth in the format mm/dd/yyyy.")
    exit()

# get today's date
today = date.today()

# calculate age
age = today.year - dob.year
if today.month < dob.month or (today.month == dob.month and today.day < dob.day):
    age -= 1

# print results
print("Your age is:", age)

# convert date to European format and print
dob_eur = dob.strftime("%d/%m/%Y")
print("Your date of birth in European format is:", dob_eur)
