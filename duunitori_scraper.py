import requests
from bs4 import BeautifulSoup



class Duunitori_Scraper:

    def __init__(self):
        self.URL = "https://duunitori.fi/tyopaikat?filter_work_relation=summer_job"
        self.page = requests.get(self.URL)
        self.soup = BeautifulSoup(self.page.content, "html.parser")

    def scrape_listing_link(self, listing):
        job_link = listing.find("a").get("href")
        return job_link
    

    def scrape_listing_location(self, listing):
        location = listing.find(class_="job-box__content")
        location_box = location.find(class_="job-box__job-location")
        location_text = location_box.get_text()
        return location_text.strip()


    def scrape_company_name(self, listing):
        company_name = listing.find('a').get('data-company')
        return company_name
    

    def scrape_listing_date(self, listing):
        listing_date = listing.find(class_="job-box__content").find(class_="job-box__job-posted").get_text()
        return listing_date


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





