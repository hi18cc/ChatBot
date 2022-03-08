from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Scraper organizes the page based on Date, sport
class  NiagaraSchedulePage:
    URL = 'https://cg2022.gems.pro/Result/Calendar.aspx?SetLanguage=en-CA&Grouping=DS' #Example URL

    def date_dropdown():
        return (By.XPATH, '//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_selGameDay"]')

    def location_dropdown():
        return (By.XPATH, '//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_selGameDay"]')
    
    def sport_dropdown():
        return (By.XPATH, '//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_selSport"]')

    def contingent_dropdown():
        return (By.XPATH, '//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_selContingent"]')

    def Grouping():
        return (By.XPATH, '//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_selGroup"]')
    
    def table_date_heading(headingNum): 
        return (By.XPATH, f'//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_secGroup1_{headingNum}_secGroup1_{headingNum}_SectionLabel"]')

    def table_sport_headings(headingNum):
        return (By.XPATH, f'//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_secGroup1_1_secGroup1_1_SectionContent"]/tr[1]/td[@class="LM_FormSection"]')                 

    def table_sport_heading_specific(headingNum, sportNum):
        return (By.XPATH, f'//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_secGroup1_{headingNum}_secGroup1_{headingNum}_SectionContent"]/tr[{sportNum}]/td[3]" and @class="LM_FormSection')

    def game_time_specific(headingNum, gameNum):
        return (By.XPATH, f'//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_secGroup1_{headingNum}_secGroup1_{headingNum}_SectionContent"]/tr[{gameNum}]/td[4]')             

    def game_times(headingNum):
        return (By.XPATH, f'//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_secGroup1_1_secGroup1_1_SectionContent"]/tr/td[4]')

    def game_event_specific(headingNum, gameNum):
        return (By.XPATH, f'//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_secGroup1_{headingNum}_secGroup1_{headingNum}_SectionContent"]/tr[{gameNum}]/td[5]')  

    def game_events(headingNum):
        return (By.XPATH, f'//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_secGroup1_{headingNum}_secGroup1_{headingNum}_SectionContent"]/tr/td[5]')

    def game_name_specific(headingNum, gameNum):
        return (By.XPATH, f'//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_secGroup1_{headingNum}_secGroup1_{headingNum}_SectionContent"]/tr[{gameNum}]/td[6]')

    def game_names(headingNum):
        return (By.XPATH, f'//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_secGroup1_{headingNum}_secGroup1_{headingNum}_SectionContent"]/tr/td[6]')

    def game_location_specific(headingNum, gameNum):
        return (By.XPATH, f'//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_secGroup1_{headingNum}_secGroup1_{headingNum}_SectionContent"]/tr[{gameNum}]/td[7]')

    def game_locations(headingNum):
        return (By.XPATH, f'//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_secGroup1_{headingNum}_secGroup1_{headingNum}_SectionContent"]/tr/td[7]')

    

        
    