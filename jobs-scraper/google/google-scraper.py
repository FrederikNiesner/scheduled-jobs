# Google Careers

import requests
from bs4 import BeautifulSoup
import pandas as pd

careers_list = []

def request(x):
    search_term = ''  # optional
    url = (f'https://careers.google.com/jobs/results/page={x}')
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find_all('tbody')

def parse(jobs):
    for job in jobs:
        title = job.find('a').text
        link = 'https://careers.google.com' + str(job.a['href'])
        location = job.find('td', class_= 'table-col-2').text
        department = job.find('span', class_= 'table--advanced-search__role').text
        date_added = job.find('span', class_= 'table--advanced-search__date').text

        career = {
            'title': title, 
            'department': department, 
            'location': location, 
            'date_added': date_added, 
            'link': link, 
        }

        careers_list.append(career)

def output():
    df = pd.DataFrame(careers_list)
    df.to_csv('jobs-scraper/google/Google-Careers-All.csv')
    print('Saved items to CSV file.')

x = 1 
while True: 
    print(f'Getting page: {x}')
    jobs = request(x)
    x += 1
    if len(jobs) != 0:
        parse(jobs)
    else: 
        break

print('Completed. Total available job listings:', len(careers_list))
output()



# NOTES: