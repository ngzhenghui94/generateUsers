import string
import time
import random
import csv
import names


emailDomain = ["@gmail.com", "@hotmail.com", "@outlook.com", "@yahoo.com"]


def randomPasswordGenerator(passwordLength):
    if passwordLength > 0:
        passwordChar = string.ascii_letters + string.digits + string.punctuation
        return ''.join(random.choice(passwordChar) for i in range(passwordLength))


def str_time_prop(start, end, format, prop):
    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)
    return time.strftime(format, time.localtime(ptime))


def random_date(start, end, prop):
    return str_time_prop(start, end, '%m/%d/%Y', prop)


with open('userTestData.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["id", "email", "fullName", "password",
                     "gender", "age", "country", "description"])
    id = 0
    tourid = 0
    for i in range(0, 200):
        # generate ID (incremental by 1)
        id = id + 1
        # generate Name and Gender
        ran = random.randint(1, 2)
        if ran == 1:
            fullName = names.get_full_name(gender='Male')
            gender = 'Male'
        else:
            fullName = names.get_full_name(gender='Female')
            gender = 'Female'
        # generate fake Email addresses
        ranEmailDomain = emailDomain[random.randint(0, 3)]
        email = fullName.replace(" ", "") + ranEmailDomain
        # generate Age
        ran = random.randint(18, 65)
        age = ran
        # generate password
        randomPasswordLength = random.randint(7, 12)
        password = randomPasswordGenerator(randomPasswordLength)
        # generate country of Origin
        ran = random.randint(1, 4)
        if ran == 1:
            country = "Singapore"
        elif ran == 2:
            country = "Malaysia"
        elif ran == 3:
            country = "Philipines"
        else:
            country = "Thailand"
        description = "I am a Python generated account."
        row = [id, email, fullName, password,
               gender, age, country, description]
        writer.writerow(row)
    csv_file.close()
