from datetime import datetime
import smtplib
import random
import pandas as pd

my_email = #Your mail
my_pass = # Your Passwowrd"


today = (datetime.now().month, datetime.now().day)
data = pd.read_csv('birthdays.csv')

birthday_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthday_dict:
    random_letter_number = random.randint(1,3)
    file_path = f"letter_templates/letter_{random_letter_number}.txt"
    birthday_person = birthday_dict[today]
    
    with open(file_path) as file:
        content = file.read()
        content = content.replace("[NAME]",birthday_person["name"])
        
    with smtplib.SMTP(host="smtp-mail.outlook.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_pass)
        connection.sendmail(from_addr=my_email, to_addrs=birthday_person["email"], \
            msg=f"Subject: Happy Birthday!\n\n{content}")
