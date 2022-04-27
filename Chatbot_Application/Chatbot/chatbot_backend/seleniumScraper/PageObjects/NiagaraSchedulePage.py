from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Scraper organizes the page based on Date, sport
class  NiagaraSchedulePage:
    URL = 'https://cg2022.gems.pro/Result/Calendar.aspx?SetLanguage=en-CA&Grouping=DS' #Example URL

    def date_dropdown():
        """
        Saved path to the date_Dropdown

        :return: path for the date dropdown.
        :rtype: Tuple(By.XPath, string)
        """
        return (By.XPATH, '//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_selGameDay"]')

    def location_dropdown():
        """
        Saved path for the location dropdown.

        :return: path for the location dropdown.
        :rtype: Tuple(By.XPath, string)
        """
        return (By.XPATH, '//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_selGameDay"]')
    
    def sport_dropdown():
        """
        Saved path for the sport dropdown.

        :return: path for the sport dropdown.
        :rtype: Tuple(By.XPath, string)
        """
        return (By.XPATH, '//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_selSport"]')

    def contingent_dropdown():
        """
        Saved path for the contingent dropdown.

        :return: path for the contingent dropdown.
        :rtype: Tuple(By.XPath, string)
        """
        return (By.XPATH, '//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_selContingent"]')

    def Grouping():
        """
        Saved path for the Grouping dropdwon.

        :return: path for the dropdown.
        :rtype: Tuple(By.XPath, string)
        """
        return (By.XPATH, '//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_selGroup"]')
    
    def table_date_heading(headingNum):
        """
        Saved path for the main heading of the table.

        :param int headingNum: The index of the heading you want to access.

        :return: path for the main heading.
        :rtype: Tuple(By.XPath, string)
        """
        return (By.XPATH, f'//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_secGroup1_{headingNum}_secGroup1_{headingNum}_SectionLabel"]')

    def table_sport_headings(headingNum):
        """
        Gets the saved path of the sub heading.

        :param int headingNum: Index of the heading the subheading is under.

        :return: path for the subHeading.
        :rtype: Tuple(By.XPath, string)
        """
        return (By.XPATH, f'//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_secGroup1_1_secGroup1_1_SectionContent"]/tr[1]/td[@class="LM_FormSection"]')                 

    def table_sport_heading_specific(headingNum, sportNum):
        """
        Gets the saed path for the subheading name if you konw the index of the subhead.

        :param int headingNum: index of the heading which is the super to the sub.
        :param int  sportNum: index of the subheading under the main heading.

        :return: path for subheading.
        :rtype: Tuple(By.XPath, string)
        """
        return (By.XPATH, f'//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_secGroup1_{headingNum}_secGroup1_{headingNum}_SectionContent"]/tr[{sportNum}]/td[3]" and @class="LM_FormSection')

    def game_time_specific(headingNum, gameNum):
        """
        Gets the saved path for the game time of a row.

        :param int headingNum: index of the main heading for the game.
        :param int gameNum: index of the game under the heading.

        ::return: path for the dropdown.
        :rtype: Tuple(By.XPath, string)
        """
        return (By.XPATH, f'//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_secGroup1_{headingNum}_secGroup1_{headingNum}_SectionContent"]/tr[{gameNum}]/td[4]')             

    def game_times(headingNum):
        """
        Returns the saved path for all game time elements under the heading.

        :param int headingNum: index of the main heading for the game.

        :return: path for the gametimes.
        :rtype: Tuple(By.XPath, string)
        """
        return (By.XPATH, f'//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_secGroup1_1_secGroup1_1_SectionContent"]/tr/td[4]')

    def game_event_specific(headingNum, gameNum):
        """
        Gets the saved path to the event name of a row.

        :param int headingNum: index of the main heading for the game.
        :param int gameNum: index of the game under the heading.

        :return: path for the game event.
        :rtype: Tuple(By.XPath, string)
        """
        return (By.XPATH, f'//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_secGroup1_{headingNum}_secGroup1_{headingNum}_SectionContent"]/tr[{gameNum}]/td[5]')  

    def game_events(headingNum):
        """
        Returns the saved path for all game event elements under the heading.

        :param int headingNum: index of the main heading for the game.

        :return: path for the game events.
        :rtype: Tuple(By.XPath, string)
        """
        return (By.XPATH, f'//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_secGroup1_{headingNum}_secGroup1_{headingNum}_SectionContent"]/tr/td[5]')

    def game_name_specific(headingNum, gameNum):
        """
        Return the saved path for game name element under the heading.

        :param int headingNum: index of the main heading for the game.
        :param int gameNum: index of the game under the heading.

        :return: path for the game name.
        :rtype: Tuple(By.XPath, string)
        """
        return (By.XPATH, f'//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_secGroup1_{headingNum}_secGroup1_{headingNum}_SectionContent"]/tr[{gameNum}]/td[6]')

    def game_names(headingNum):
        """
        Returns the saved path for all game names elements under the heading.

        :param int headingNum: index of the main heading for the game.

        :return: path for the game names.
        :rtype: Tuple(By.XPath, string)
        """
        return (By.XPATH, f'//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_secGroup1_{headingNum}_secGroup1_{headingNum}_SectionContent"]/tr/td[6]')

    def game_location_specific(headingNum, gameNum):
        """
        Return the saved path for game location element under the heading.

        :param int headingNum: index of the main heading for the game.
        :param int gameNum: index of the game under the heading.

        :return: path for the game location.
        :rtype: Tuple(By.XPath, string)
        """
        return (By.XPATH, f'//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_secGroup1_{headingNum}_secGroup1_{headingNum}_SectionContent"]/tr[{gameNum}]/td[7]')

    def game_locations(headingNum):
        """
        Returns the saved path for all game locations elements under the heading.

        :param int headingNum: index of the main heading for the game.

        :return: path for the game names.
        :rtype: Tuple(By.XPath, string)
        """
        return (By.XPATH, f'//*[@id="ctl00_ctl00_ContentPlaceHolderBasicMaster_ContentPlaceHolder1_secGroup1_{headingNum}_secGroup1_{headingNum}_SectionContent"]/tr/td[7]')

    

        
    