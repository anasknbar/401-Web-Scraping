from bs4 import BeautifulSoup
import requests
import json

def job_scraper():
  print('Enter skill to search for')
  skill_to_search = input('>')
  print(f"searching for {skill_to_search}...")
  html_text = requests.get("https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&searchTextSrc=as&searchTextText=Python&txtKeywords=Python&txtLocation=").text

  soup = BeautifulSoup(html_text,'lxml')

  jobs = soup.find_all('li',class_='clearfix job-bx wht-shd-bx')

  jobs_list = []
  for job in jobs:
    job_date = job.find('span','sim-posted').text.strip()
    required_skills = job.find('span',class_='srp-skills').text.strip().replace(' ','')
    
    if skill_to_search in required_skills:
    
      company_name = job.find('h3',class_='joblist-comp-name').text.strip()
      required_skills = job.find('span',class_='srp-skills').text.strip().replace(' ','')
      job_link = job.header.h2.a['href']
    
      jobs_list.append({
        "company_name": company_name,
        "required_skills": required_skills,
        "job_date": job_date,
        "job_link": job_link

      })
      
  with open('jobs.json','w') as file:
    job_json = json.dumps(jobs_list,indent=4)
    file.write(f"{job_json}")
  
      


if __name__ == '__main__':
  job_scraper()