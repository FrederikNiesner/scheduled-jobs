# Apple Careers
import os
import requests
from bs4 import BeautifulSoup
import pandas as pd

careers_list = []

def request(x):
    search_term = 'Early'
    # url = (f'https://jobs.apple.com/en-us/search?search={search_term}&sort=relevance&location=united-states-USA&page={x}&team=apps-and-frameworks-SFTWR-AF+cloud-and-infrastructure-SFTWR-CLD+core-operating-systems-SFTWR-COS+devops-and-site-reliability-SFTWR-DSR+engineering-project-management-SFTWR-EPM+information-systems-and-technology-SFTWR-ISTECH+machine-learning-and-ai-SFTWR-MCHLN+security-and-privacy-SFTWR-SEC+software-quality-automation-and-tools-SFTWR-SQAT+wireless-software-SFTWR-WSFT')
    url = (f'https://jobs.apple.com/en-us/search?sort=newest&page={x}&key=python+data+ml+machine&location=germany-DEU&team=machine-learning-infrastructure-MLAI-MLI+deep-learning-and-reinforcement-learning-MLAI-DLRL+natural-language-processing-and-speech-technologies-MLAI-NLP+computer-vision-MLAI-CV+applied-research-MLAI-AR+acoustic-technologies-HRDWR-ACT+analog-and-digital-design-HRDWR-ADD+architecture-HRDWR-ARCH+battery-engineering-HRDWR-BE+camera-technologies-HRDWR-CAM+display-technologies-HRDWR-DISP+engineering-project-management-HRDWR-EPM+environmental-technologies-HRDWR-ENVT+health-technology-HRDWR-HT+machine-learning-and-ai-HRDWR-MCHLN+mechanical-engineering-HRDWR-ME+process-engineering-HRDWR-PE+reliability-engineering-HRDWR-REL+sensor-technologies-HRDWR-SENT+silicon-technologies-HRDWR-SILT+system-design-and-test-engineering-HRDWR-SDE+wireless-hardware-HRDWR-WT+apps-and-frameworks-SFTWR-AF+cloud-and-infrastructure-SFTWR-CLD+core-operating-systems-SFTWR-COS+devops-and-site-reliability-SFTWR-DSR+engineering-project-management-SFTWR-EPM+information-systems-and-technology-SFTWR-ISTECH+machine-learning-and-ai-SFTWR-MCHLN+security-and-privacy-SFTWR-SEC+software-quality-automation-and-tools-SFTWR-SQAT+wireless-software-SFTWR-WSFT+industrial-design-DESGN-ID+human-interface-design-DESGN-HID+communications-design-DESGN-CMD+business-intelligence-and-analytics-OPMFG-BIA+business-process-management-OPMFG-BPM+supply-demand-management-and-npi-readiness-OPMFG-SDMNR+retail-and-e-commerce-fulfillment-OPMFG-RECF+logistics-and-supply-chain-OPMFG-SCL+sales-planning-and-operations-OPMFG-SPO+procurement-OPMFG-PRC+manufacturing-and-operations-engineering-OPMFG-MFGE+quality-engineering-OPMFG-QE+supplier-responsibility-OPMFG-SR+program-management-OPMFG-PRMGMT+services-marketing-MKTG-SVCM+product-marketing-MKTG-PM+marketing-communications-MKTG-MKTCM+corporate-communications-MKTG-CRPCM+information-systems-and-technology-CORSV-IT+finance-CORSV-FIN+legal-CORSV-LEG+people-CORSV-HR+learning-and-development-CORSV-LRNDV+global-security-CORSV-GLSEC+information-security-CORSV-INFOSEC+environment-and-social-initiatives-CORSV-ENSI+policy-and-government-affairs-CORSV-GOV+real-estate-and-development-CORSV-REFAC+dining-and-food-services-CORSV-DFS+administration-CORSV-ADMIN+global-retail-support-CORSV-GRS+business-development-SLDEV-BUSDEV+account-management-SLDEV-CC+apple-store-sales-SLDEV-ARS+retail-partner-sales-SLDEV-CRC+sales-planning-and-operations-SLDEV-SO+field-and-solutions-engineering-SLDEV-FSE+online-support-CUST-ONSPT+technical-support-and-customer-support-CUST-ACCS+apple-store-support-CUST-ACRCC+applecare-business-development-CUST-SSBD+service-channel-management-and-operations-CUST-SCMO')
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup.find_all('tbody')


# Comment out after first run of script and file is successfully created. 
# with open('Apple-Careers-OFFLINE.html', 'w') as file: 
#    file.write(str(soup))
#    print('Offline file saved.')

def parse(jobs):
    for job in jobs:
        title = job.find('a').text
        link = 'https://jobs.apple.com' + str(job.a['href'])
        id = str(job.a['id'])
        location = job.find('td', class_= 'table-col-2').text
        department = job.find('span', class_= 'table--advanced-search__role').text
        date_added = job.find('span', class_= 'table--advanced-search__date').text

        career = {
            'id': id, 
            'title': title, 
            'department': department, 
            'location': location, 
            'date_added': date_added, 
            'link': link, 
        }

        careers_list.append(career)

def output():
    # copy to compare if new jobs came in (or old where dropped)
    os.system('cp jobs-scraper/apple/Apple-Careers-All.csv jobs-scraper/apple/Apple-Careers-All-cp.csv')
    
    # new jobs data
    df = pd.DataFrame(careers_list)
    df.to_csv('jobs-scraper/apple/Apple-Careers-All.csv')
    print('Saved items to CSV file.')

    # compare
    

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