from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class CanadaGamesPlayerPage:
    URL = 'https://cg2019.gems.pro/Result/ShowPerson_List.aspx?'

    def contingent_dropdown():
        """
        Element for the dropdown for contingent.

        :return: tuple with By.XPATH as the first item and the locator string as the 2nd item.
        :rtype: tuple
        """
        return (By.XPATH, "//td[@class='LM_MasterPageDataCell']//tr[4]//select[1]")

    def sport_dropdown():
        """
        Element for the dropdown for sport.

        :return: tuple with By.XPATH as the first item and the locator string as the 2nd item.
        """

        return (By.XPATH, "//td[@class='LM_MasterPageDataCell']//tr[4]//select[1]")

    def find_button():
        """
        Element for find button.

        :return::return: tuple with By.XPATH as the first item and the locator string as the 2nd item.
        """

        return (By.XPATH, ".LM_Button_Find")

    def table_row_sport(index):
        """
        Sport name in the 1-based index of the row.

        :param int index: the index of the player on the table. 1-based.
        
        :return: tuple of xpath and element for the sport regarding the player.
        :rtype: Tuple (By.XPATH, string)
        """

        return (By.XPATH, f"//table[@class='LM_ListTable']//tr[{index+1}]//div[@class='LM_SportName']")
    
    def table_row_player(index):
        """
        1-based index

        :param int index: the index of the player on the table. 1-based.
        
        :return: tuple of xpath and element for the name regarding the player.
        :rtype: Tuple (By.XPATH, string)
        """

        return (By.XPATH, f"//*[@class='LM_ListTable']/tbody/tr[{index+1}]/td[1]/a")

    def table_rows():
        """
        """

        return (By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_tblParticipant']/tbody/tr")



    def get_URL_from_element(webElement):
        """
        Takes the web element and finds the href which should ocntain the URL.

        :param WebElement webElement: the element which is a link to the URL

        :return: URL as string
        :rtype: string
        """
        url = webElement.get_attribute('href')

        return url
    







    

