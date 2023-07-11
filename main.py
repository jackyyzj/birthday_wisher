import smtplib
from datetime import datetime
import random
import pandas as pd

# outlook.office365.com
my_email = "yzjccy123456@gmail.com"
password = "dofasljcbkqclrni"
# my_email2 = "yzjccy123456@outlook.com"
# password2 = "jxeneujptkqmmosx"
port = 587


today = datetime.now()

today_tuple = (today.month, today.day)
data = pd.read_csv("birthdays.csv")

birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

#HINT 4: Then you could compare and see if today's month/day tuple matches one of the keys in birthday_dict like this:
# if (today_month, today_day) in birthdays_dict:

if today_tuple in birthdays_dict:
	birthdays_person = birthdays_dict[today_tuple]
	file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
	with open(file_path) as letter_file:
		contents = letter_file.read()
		contents = contents.replace("[NAME]",birthdays_person["name"])

	with smtplib.SMTP("smtp.gmail.com", port = port) as connection:
		connection.starttls()
		connection.login(user = my_email, password = password)
		connection.sendmail(from_addr= my_email, to_addrs= birthdays_person["email"],
							msg = f"Subject:Happy Birthday\n\n{contents}")