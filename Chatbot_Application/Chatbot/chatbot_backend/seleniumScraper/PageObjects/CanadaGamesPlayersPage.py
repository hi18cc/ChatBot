from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class CanadaGamesPlayerPage:
    URL = 'https://cg2019.gems.pro/Result/ShowPerson_List.aspx?'

    def contingent_dropdown():
        """
        Element for the dropdown for contingent.

        :return: XPath and path of dropdown for contingent selection.
        :rtype: tuple(By.XPATH, string)
        """
        return (By.XPATH, "//td[@class='LM_MasterPageDataCell']//tr[4]//select[1]")

    def sport_dropdown():
        """
        Element for the dropdown for sport.

        :return: XPath and path of dropdown for sport selection.
        :rtype: Tuple(By.XPATH, string)
        """

        return (By.XPATH, "//td[@class='LM_MasterPageDataCell']//tr[4]//select[1]")

    def find_button():
        """
        Element for find button.

        :return: XPath and path of the find button which completes the query and loads the url.
        :rtype: Tuple(By.XPATH, string)
        """

        return (By.CSS_SELECTOR, ".LM_Button_Find")

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
        Returns the path and type for all tables in the row.

        :return: XPath and path for all tables.
        :rtype: tuple(By.XPATH, string)
        """

        return (By.XPATH, "//*[@id='ctl00_ContentPlaceHolder1_tblParticipant']/tbody/tr")



    
    







    

