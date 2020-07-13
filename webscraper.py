from bs4 import BeautifulSoup
import csv
import urllib.request as rq

# if something happens to the page (12/07/2020) (D/M/Y)
# source = open("/inmates/inmates.html")

source = rq.urlopen("https://cartercountysheriff.us/inmates2.html").read()
soup = BeautifulSoup(source, "lxml")
name = ["Names"]
sex = ["Sex"]
race = ["Race"]
dob = ["DOB"]
booked_date = ["Booked Date"]
released_date = ["Released Date"]
# if I decide to deal with multiple strings in one span
# charge = []

# to see span id's
# for each in soup.find_all("td"):
#     print(each.span)

# just getting every text in spans and writing them on corresponding lists
for each in soup.find_all("span", id=lambda x: x.startswith("gvResult_lblInmateName")):
    # print(name.string)
    name.append(each.string.strip())

for each in soup.find_all("span", id=lambda x: x.startswith("gvResult_lblSex")):
    sex.append(each.string.strip())

for each in soup.find_all("span", id=lambda x: x.startswith("gvResult_lblRace")):
    race.append(each.string.strip())

for each in soup.find_all("span", id=lambda x: x.startswith("gvResult_lblDOB")):
    dob.append(each.string.strip())

for each in soup.find_all("span", id=lambda x: x.startswith("gvResult_lblBookedDate")):
    booked_date.append(each.string.strip())

for each in soup.find_all("span", id=lambda x: x.startswith("gvResult_lblReleasedDate")):
    try:
        released_date.append(each.string.strip())
    except AttributeError:
        released_date.append("")

# for each in soup.find_all("span", id=lambda x: x.startswith("gvResult_rptChargeResult")):
#     charge.append(each.string.strip())

rows = zip(name, sex, race, dob, booked_date, released_date)  # ,charge)

with open("/home/tfp/Programming/Python/webscrap/inmates.csv", "w") as f:
    writer = csv.writer(f)
    for row in rows:
        writer.writerow(row)

# file_path = open("/home/tfp/Programming/Python/webscrap/inmates.csv", "w")
# writer = csv.writer(file_path)
# writer.writerow(names)
