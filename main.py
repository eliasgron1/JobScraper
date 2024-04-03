import duunitori_scraper
#import db_handler



STARTING_PAGE = 1
ENDING_PAGE = 5


def main():
    DS = duunitori_scraper.Duunitori_Scraper()
    #DB = db_handler.Database_Master()
    
    for page in range(STARTING_PAGE,ENDING_PAGE):
        DS.set_page(page)
        print(f"\n\nPage={page}\n\n")

        page_html = DS.scrape_page_html()
        
        for element in page_html:
            company_name = DS.scrape_company_name(element)
            company_link = DS.scrape_listing_link(element)
            job_location = DS.scrape_listing_location(element)
            listing_date = DS.scrape_listing_date(element)
            
            print(listing_date)
            print(company_name)
            print(job_location)
            print(f"https://duunitori.fi/{company_link}\n\n")





if __name__ == "__main__":
    main()
