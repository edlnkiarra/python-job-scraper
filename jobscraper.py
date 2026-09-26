import requests
from bs4 import BeautifulSoup
import csv

url = "https://realpython.github.io/fake-jobs/"
page = requests.get(url)
cont = BeautifulSoup(page.content, 'html.parser')

#Read all jobs card
jobs = cont.find_all("div", class_="card-content")

#Write to csv
with open("jobs.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Job Title", "Company Name", "Location", "URL"])

    for job in jobs:
        title = job.find("h2", class_="title").text.strip()
        company = job.find("h3", class_="company").text.strip()
        location = job.find("p", class_="location").text.strip()
        link = job.find("a")["href"]
        writer.writerow([title, company, location, link])
