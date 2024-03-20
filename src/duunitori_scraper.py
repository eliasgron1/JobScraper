import requests
from bs4 import BeautifulSoup

import defs

class Duunitori_scraper:
    def __init__(self):
        self.URLS = f"https://duunitori.fi/tyopaikat?filter_work_relation=summer_job"
        self.page = requests.get(self.URLS)
        self.soup = BeautifulSoup(self.page.content, "html.parser")


    def scrape_listing(self):
        jobs = self.soup.find(class_="grid-sandbox grid-sandbox--tight-bottom grid-sandbox--tight-top")
        results = jobs.findAll(class_="job-box")
        for element in results:
            company_name = element.find('a').get('data-company')
            job_link = element.find("a").get("href")
            self.print_data(company_name)
            main_html = self.scrape_listing_data(job_link)
            self.print_data(main_html)


        print(self.URLS)
        return results
    
    def scrape_listing_data(self, job_link):
        listing_page = requests.get(f"https://duunitori.fi/{job_link}")
        listing_soup = BeautifulSoup(listing_page.content, "html.parser")
        description = listing_soup.findAll(class_="description-box")
        for element in description:
            description_text = element.find("div").get_text()
            return description_text
        
    def print_data(self, data):
        print(f"{data}")
        print("\n\n\n")
    
    def set_page(self, page_num):
        self.page = page_num
        print(self.page)
        self.URLS = f"https://duunitori.fi/tyopaikat?filter_work_relation=summer_job&sivu={page_num}"
        self.page = requests.get(self.URLS)
        self.soup = BeautifulSoup(self.page.content, "html.parser")


def main():
    DS = Duunitori_scraper()
    for page in range(1,5):
        DS.scrape_listing()
        DS.set_page(page)
    # print(results)





if __name__ == "__main__":
    main()
