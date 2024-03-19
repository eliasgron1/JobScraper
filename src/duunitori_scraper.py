import requests
from bs4 import BeautifulSoup

import defs



class Duunitori_scraper:
    def __init__(self):
        self.URLS = f"https://duunitori.fi/tyopaikat?filter_work_relation=summer_job"
        self.page = requests.get(self.URLS)
        self.soup = BeautifulSoup(self.page.content, "html.parser")
        


    def scraper(self):
        jobs = self.soup.find(class_="grid-sandbox grid-sandbox--tight-bottom grid-sandbox--tight-top")
        results = jobs.findAll(class_="job-box")
        for element in results:
            company_name = element.find('a').get('data-company')
            print(company_name)
        print(self.URLS)
        return results
    
    def set_page(self, page_num):
        self.page = page_num
        print(self.page)
        self.URLS = f"https://duunitori.fi/tyopaikat?filter_work_relation=summer_job&sivu={page_num}"
        self.page = requests.get(self.URLS)
        self.soup = BeautifulSoup(self.page.content, "html.parser")


def main():
    DS = Duunitori_scraper()
    for page in range(2,6):
        DS.scraper()
        DS.set_page(page)
    # print(results)





if __name__ == "__main__":
    main()
