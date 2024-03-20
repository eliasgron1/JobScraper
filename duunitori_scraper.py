import requests
from bs4 import BeautifulSoup

STARTING_PAGE = 1
ENDING_PAGE = 5


class Duunitori_scraper:

    def __init__(self):
        self.URL = "https://duunitori.fi/tyopaikat?filter_work_relation=summer_job"
        self.page = requests.get(self.URL)
        self.soup = BeautifulSoup(self.page.content, "html.parser")

    def scrape_listing_link(self, listing):
        job_link = listing.find("a").get("href")
        return job_link


    def scrape_company_name(self, listing):
        company_name = listing.find('a').get('data-company')
        return company_name

            
    def scrape_page_html(self):
        jobs = self.soup.find(class_="grid-sandbox grid-sandbox--tight-bottom grid-sandbox--tight-top")
        page_html = jobs.findAll(class_="job-box")
        return page_html
        


    def scrape_listing_data(self, job_link):
        listing_page = requests.get(f"https://duunitori.fi/{job_link}")
        listing_soup = BeautifulSoup(listing_page.content, "html.parser")
        description = listing_soup.find(class_="description-box")
        description_text = description.find(class_="description--jobentry").get_text()
        return f"{description_text[:100]}..."

    

    def set_page(self, page_num):
        self.URL = f"https://duunitori.fi/tyopaikat?filter_work_relation=summer_job&sivu={page_num}"
        self.page = requests.get(self.URL)
        self.soup = BeautifulSoup(self.page.content, "html.parser")




def main():
    DS = Duunitori_scraper()

    
    for page in range(STARTING_PAGE,ENDING_PAGE):
        DS.set_page(page)
        print(f"\n\n{page}\n\n")

        page_html = DS.scrape_page_html()
        
        for element in page_html:
            company_name = DS.scrape_company_name(element)
            print(company_name)
            company_link = DS.scrape_listing_link(element)
            print(f"https://duunitori.fi/{company_link}")
            company_description = DS.scrape_listing_data(company_link)
            print(company_description)






if __name__ == "__main__":
    main()
