from Chatbot_Application.Chatbot.autoScraper.PageObjects.CanadaGamesMedalsPage import CanadaGamesMedalPage
from seleniumScraper.PageObjects.CanadaGamePersonPage import CanadaGamesPersonPage
from seleniumScraper.PageObjects.NiagaraSchedulePage import NiagaraSchedulePage
from seleniumScraper.PageObjects.CanadaGamesPlayersPage import CanadaGamesPlayerPage
from seleniumScraper.PageObjects.CanadaGamePersonPage import CanadaGamesPersonPage
from selenium.webdriver.support.ui import Select

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Utilities:
    """
    This class provides methods to get elements using WebDriver.
    """
    def getHeading(driver, headingNum=1):
        """
        Gets the main table heading, 1 index

        :param WebDriver driver: Webdriver that has navigated to https://cg2022.gems.pro/Result/Calendar.aspx? ... page.
        :param int headingNum: The number heading you want to access, default is 1 if none is selected. 1-index.

        :return: The xpath and path.
        :rtype: Tuple(By.XPATH, Path)
        """
        element = NiagaraSchedulePage.table_date_heading(headingNum)
        return element

    def getSubHeading(driver, headingNum=1):
        """
        Gets the subheading of the headingNum param. This method does not adjust for multiple subheadings, one fix might be to use CSS Selector.
        
        :param WebDriver driver: Webdriver that has navigated to https://cg2022.gems.pro/Result/Calendar.aspx? ... page.
        :param int headingNum: The heading number which the subheading presides under.

        :return: The name of the subheading.
        :rtype: Tuple(By.XPATH, Path)
        """
        element = NiagaraSchedulePage.table_sport_headings(headingNum)
        return element

    def getGameTimes(driver, headingNum=1):
        """
        Gets the time of all games under the heading Num.

        :param WebDriver driver: Webdriver that has navigated to https://cg2022.gems.pro/Result/Calendar.aspx? ... page.
        :param int headingNum: The heading number which the game times presides under.

        :return: Returns xpath for all the game times.
        :rtype: List<tuple(By.Xpath, Path)>
        """
        element = NiagaraSchedulePage.game_times(headingNum)
        return element
    
    def getGameEvents(driver, headingNum=1):
        """
        Gets the event name of all games under the heading num.

        :param WebDriver driver: Webdriver that has navigated to https://cg2022.gems.pro/Result/Calendar.aspx? ... page.
        :param int headingNum: The heading number which the game events presides under.

        :return: Returns xpath for all the game events.
        :rtype: List<tuple(By.Xpath, Path)>
        """
        element = NiagaraSchedulePage.game_events(headingNum)
        return element

    def getGameNames(driver, headingNum=1):
        """
        Gets the name of all the games under the heading num.

        :param WebDriver driver: Webdriver that has navigated to https://cg2022.gems.pro/Result/Calendar.aspx? ... page.
        :param int headingNum: The heading number which the game names presides under.

        :return: Returns xpath for all the game names.
        :rtype: List<tuple(By.Xpath, Path)>
        """
        element = NiagaraSchedulePage.game_names(headingNum)
        return element

    def getGameLocations(driver, headingNum=1):
        """
        Gets the location of all games under the heading.

        :param WebDriver driver: Webdriver that has navigated to https://cg2022.gems.pro/Result/Calendar.aspx? ... page.
        :param int headingNum: The heading number which the game events presides under.

        :return: Returns xpath for all the game names.
        :rtype: List<tuple(By.Xpath, Path)>
        """
        element = NiagaraSchedulePage.game_locations(headingNum)
        return element

    def getEvent(self, driver, eventNum, headingNum=1,  subHeading=False):
        """
        DEPRECATED Gets the event name under the heading depending on it's index. 
        #subHeading variable decides if we look at the subheading or not.

        :param WebDriver driver: Webdriver that has navigated to https://cg2022.gems.pro/Result/Calendar.aspx? ... page.
        :param int EventNum: 1-index of the event in the table based on the heading num.
        :param int headingNum: The heading number which the event name presides under.
        :param bool subHeading: If the subheading is present this is true.

        :return: Returns the row for the event. E.g. the whole row for the game.
        :rtype: List<tuple(By.Xpath, Path)>
        """
        
        event = []

        headingXPATH = NiagaraSchedulePage.table_heading(headingNum)
        heading = self.getElementText(driver, headingXPATH)

        event.append(heading)

        if (subHeading):
            subHeadingXPATH = NiagaraSchedulePage.table_subheading(headingNum)
            subHeading = self.getElementText(driver, subHeadingXPATH)
            event.append(subHeading)
        
        eventTimeXPATH = NiagaraSchedulePage.event_time(headingNum, eventNum)
        eventTime = self.getElementText(driver, eventTimeXPATH)
        event.append(eventTime)
       
        eventGameTypeXPATH = NiagaraSchedulePage.event_gameType(headingNum, eventNum)
        eventGameType = self.getElementText(driver, eventGameTypeXPATH)
        event.append(eventGameType)

        eventRoundXPATH = NiagaraSchedulePage.event_round(headingNum, eventNum)
        eventRound = self.getElementText(driver, eventRoundXPATH)
        event.append(eventRound)

        eventLocationXPATH = NiagaraSchedulePage.event_location(headingNum, eventNum)
        eventLocation = self.getElementText(driver, eventLocationXPATH)
        event.append(eventLocation)

        return event

    def getElementText(driver, element):
        """Gets the text of an element using a path.
        
        :param WebDriver driver: Driver which has been navigated to a url.
        :param Tuple<By, string> element: Tuple of the element with the type and path.

        :return: Text of element.
        :rtype: string
        """


        return driver.find_element(*element).text

    def getContingentDropdown(driver):
        """
        Gets the web element by XPATH for the contingent dropdown on the Canada Summer Games page and finds the element.

        :param WebDriver driver: driver used to find element.

        :return : Element of the dropdown for contingents.
        :rtype: WebElement
        """
        element = CanadaGamesPlayerPage.contingent_dropdown()
        element = driver.find_element(*element)
        return element
    
    def getFindButton(driver):
        """
        Gets the XPATH for the Find button on the Canada summer games.

        :param WebDriver driver: Driver used to find element.

        :return WebElement: Element to be used.
        """
        element = CanadaGamesPlayerPage.find_button()
        element = driver.find_element(*element)

        return element
    
    def get_table_rows(driver):
        """
        Gets the list of rows from the players page.

        :param WebDriver driver: Webdriver that has navigated to https://cg2019.gems.pro/Result/ShowPerson_List.aspx? ... page.
        
        :return: all rows of table.
        :rtype: List<WebElement>
        """
        element = CanadaGamesPlayerPage.table_rows()
        elements = driver.find_elements(*element)

        return elements

    def getTableSport(driver, index):
        """
        Gets the sport element at the index given.

        :param WebDriver driver: Webdriver that has navigated to https://cg2019.gems.pro/Result/ShowPerson_List.aspx? ... page.
        :param int index: 1-index of the sport name in that row.

        :return: Cell of sport for the player in that row.
        :rtype: WebElement
        """
        element = CanadaGamesPlayerPage.table_row_sport(index)
        element = driver.find_element(*element)

        return element

    def getTablePlayer(driver, index):
        """
        :param WebDriver driver: Webdriver that has navigated to https://cg2019.gems.pro/Result/ShowPerson_List.aspx? ... page.
        :param int index: 1-index of the player name in that row.
        
        :return: Cell of name for the player in that row.
        :rtype: WebElement
        """
        element = CanadaGamesPlayerPage.table_row_player(index)
        element = driver.find_element(*element)

        return element

    def getHometown(driver):
        """
        Gets home town of person on personal page if the driver is on the correct page.
        
        :param WebDriver driver: Webdriver that has navigated to https://cg2019.gems.pro/Result/ShowPerson.aspx? ... page.

        :return: Element which has text of the hometown of the player.
        :rtype: WebElement
        """
        element = CanadaGamesPersonPage.person_hometown()
        WebDriverWait(driver, 2).until(EC.text_to_be_present_in_element(*element))
        element = driver.find_element(*element)

        return element

    def getName(driver):
        """
        Gets name of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Webdriver that has navigated to https://cg2019.gems.pro/Result/ShowPerson.aspx? ... page.

        :return: Element which has text of Name of the person on personal page.
        :rtype: WebElement
        """

        element = CanadaGamesPersonPage.person_name()
        element = driver.find_element(*element)

        return element

    def getContingent(driver):
        """
        Gets contingent of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Webdriver that has navigated to https://cg2019.gems.pro/Result/ShowPerson.aspx? ... page.

        :return: Element which has text of Name of contingent on personal page.
        :rtype: WebElement
        """

        element = CanadaGamesPersonPage.person_contingent()
        element = driver.find_element(*element)

        return element

    def getType(driver):
        """
        Gets type of person on personal page if the driver is on the correct page. Type is the persons role e.g. athlete/coach/trainer.

        :param WebDriver driver: Webdriver that has navigated to https://cg2019.gems.pro/Result/ShowPerson.aspx? ... page.

        :return: Element which has text of person type e.g. (coach, player etc.)
        :rtype: WebElement
        """

        element = CanadaGamesPersonPage.person_type()
        element = driver.find_element(*element)

        return element

    def getSport(driver):
        """
        Gets sport of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Webdriver that has navigated to https://cg2019.gems.pro/Result/ShowPerson.aspx? ... page.

        :return: Element which has text of sport name of person on personal page.
        :rtype: WebElement
        """

        element = CanadaGamesPersonPage.person_sport()
        element = driver.find_element(*element)

        return element

    def getAge(driver):
        """
        Gets age of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Webdriver that has navigated to https://cg2019.gems.pro/Result/ShowPerson.aspx? ... page.

        :Return: Element which has text of Age of person on personal page.
        :rtype: WebElement
        """

        element = CanadaGamesPersonPage.person_age()
        element = driver.find_element(*element)

        return element

    def getHeight(driver):
        """
        Gets height of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Webdriver that has navigated to https://cg2019.gems.pro/Result/ShowPerson.aspx? ... page.

        :Return: Element which has text of Height of person on personal page.
        :rtype: WebElement
        """

        element = CanadaGamesPersonPage.person_height()
        element = driver.find_element(*element)

        return element

    def getWeight(driver):
        """
        Gets weight of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Webdriver that has navigated to https://cg2019.gems.pro/Result/ShowPerson.aspx? ... page.

        :Return: Element which has text of Weight of person on personal page.
        :rtype: WebElement
        """

        element = CanadaGamesPersonPage.person_weight()
        element = driver.find_element(*element)

        return element

    def getClub(driver):
        """
        Gets Club or Team of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Webdriver that has navigated to https://cg2019.gems.pro/Result/ShowPerson.aspx? ... page.

        :Return: Element which has text of Club of person on personal page.
        :rtype: WebElement
        """

        element = CanadaGamesPersonPage.club_or_team_affiliation()
        element = driver.find_element(*element)

        return element

    def getCoachName(driver):
        """
        Gets name of coach of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Webdriver that has navigated to https://cg2019.gems.pro/Result/ShowPerson.aspx? ... page.

        :Return: Element which has text of name of coach on personal page.
        :rtype: WebElement
        """

        element = CanadaGamesPersonPage.name_of_coach()
        element = driver.find_element(*element)

        return element
    
    def getPosition(driver):
        """
        Gets position of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Webdriver that has navigated to https://cg2019.gems.pro/Result/ShowPerson.aspx? ... page.

        :Return: Element which has text of Position of person on personal page.
        :rtype: WebElement
        """

        element = CanadaGamesPersonPage.person_position()
        element = driver.find_element(*element)

        return element

    def getGoalsforTheGames(driver):
        """
        Gets 'my goals for the game' of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Webdriver that has navigated to https://cg2019.gems.pro/Result/ShowPerson.aspx? ... page.

        :Return: Element which has text of Persons personal goals for the Canada summer games events
        :rtype: WebElement
        """

        element = CanadaGamesPersonPage.my_goals_for_the_games()
        element = driver.find_element(*element)

        return element

    def getPersonalBestResultinEvent(driver):
        """
        Gets 'my personal best result in my event' of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Webdriver that has navigated to https://cg2019.gems.pro/Result/ShowPerson.aspx? ... page.

        :Return: Element which has text of persons personal best result in the event.
        :rtype: WebElement
        """

        element = CanadaGamesPersonPage.my_personal_best_result_in_my_event()
        element = driver.find_element(*element)

        return element

    def getAwardsorMajorAccomplishments(driver):
        """
        Gets 'awards or major accomplishments that I have received.' of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Webdriver that has navigated to https://cg2019.gems.pro/Result/ShowPerson.aspx? ... page.

        :Return: Element which has text of persons awards and accomplishments on personal page.
        :rtype: WebElement
        """

        element = CanadaGamesPersonPage.awards_or_major_accomplishments_that_I_have_received()
        element = driver.find_element(*element)

        return element

    def getMyPersonalRoleModel(driver):
        """
        Gets 'My personal role model' of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Webdriver that has navigated to https://cg2019.gems.pro/Result/ShowPerson.aspx? ... page.

        :Return: Element which has text of personal role model.
        :rtype: WebElement
        """

        element = CanadaGamesPersonPage.my_personal_role_model()
        element = driver.find_element(*element)

        return element
    
    def getOtherInformation(driver):
        """
        Gets 'Other information that could be of interest to the media' of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Webdriver that has navigated to https://cg2019.gems.pro/Result/ShowPerson.aspx? ... page.

        :Return: Element which has text of persons other information.
        :rtype: WebElement
        """

        element = CanadaGamesPersonPage.other_information_that_could_be_of_interest_to_the_media()
        element = driver.find_element(*element)

        return element

    def select_dropdown(webElement):
        """
        Will take the select dropdown element found by driver and create a Select object.

        :param WebElement webElement: An element found by selenium driver.

        :return: this will turn the object that will control the select object.
        :rtype: Select
        """
        drpdwn = Select(webElement)

        return drpdwn

    def select_dropdown_item_by_index(dropdown, index):
        """
        Will take the Select object and select an item by index.

        :param Select dropdown: Dropdown to be controlled.
        :param int index: the number item to be accessed.

        :return: True if item was selected successfully.
        :rtype: bool
        """

        dropdown.select_by_index(index)

        return True

    def select_dropdown_item_by_visible_text(dropdown, value):
        """
        Will take the Select object and select an item by value/text.

        :param Select dropdown: Dropdown to be controlled.
        :param string value: the number item to be accessed.

        :return: True if item was selected successfully.
        :rtype: bool
        """

        dropdown.select_by_visible_text(value)

        return True

    def click_element( element):
        """
        Clicks on the web element provided using the driver provided

        :param WebElement element: element to be clicked on and found by driver

        :return: true if click successful.
        :rtype: bool
        """

        element.click()

        return True

    def get_URL_from_element(webElement):
        """
        Takes the web element and finds the href which should ocntain the URL.

        :param WebElement webElement: the element which is a link to the URL

        :return: URL as string
        :rtype: string
        """
        url = webElement.get_attribute('href')

        return url

    def get_gold_medal_count_for_contingent(driver, contingentAbbrev):
        """
        Gets the gold medal element from the webpage.

        :param String contingentAbbrev: This is the abbreviation for the contingent.

        :return: Gold medal count element containing count.
        :rtype: string
        """

        element = CanadaGamesMedalPage.gold_medal_count_by_contingent(contingentAbbrev)
        element = driver.find_element(*element)
        return element

    def get_silver_medal_count_for_contingent(driver, contingentAbbrev):
        """
        Gets the silver medal element from the webpage.

        :param String contingentAbbrev: This is the abbreviation for the contingent.

        :return: Silver medal count element containing count.
        :rtype: string
        """

        element = CanadaGamesMedalPage.silver_medal_count_by_contingent(contingentAbbrev)
        element = driver.find_element(*element)
        return element

    def get_bronze_medal_count_for_contingent(driver, contingentAbbrev):
        """
        Gets the bronze medal element from the webpage.

        :param String contingentAbbrev: This is the abbreviation for the contingent.

        :return: Bronze medal count element containing count.
        :rtype: string
        """

        element = CanadaGamesMedalPage.bronze_medal_count_by_contingent(contingentAbbrev)
        element = driver.find_element(*element)
        return element

    def get_total_medal_count_for_contingent(driver, contingentAbbrev):
        """
        Gets the total medal element from the webpage.

        :param String contingentAbbrev: This is the abbreviation for the contingent.

        :return: Total medal count element containing count.
        :rtype: string
        """

        element = CanadaGamesMedalPage.total_medal_count_by_contingent(contingentAbbrev)
        element = driver.find_element(*element)
        return element




