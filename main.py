import duunitori_scraper
import db_handler



STARTING_PAGE = 1
ENDING_PAGE = 5


def main():
    DS = duunitori_scraper.Duunitori_Scraper()
    DB = db_handler.Database_Master()
    
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
