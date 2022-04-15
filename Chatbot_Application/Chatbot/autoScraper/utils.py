from autoScraper.PageObjects.CanadaGamePersonPage import CanadaGamesPersonPage
from autoScraper.PageObjects.NiagaraSchedulePage import NiagaraSchedulePage
from autoScraper.PageObjects.CanadaGamesPlayersPage import CanadaGamesPlayerPage
from autoScraper.PageObjects.CanadaGamesMedalsPage import CanadaGamesMedalPage
from selenium.webdriver.support.ui import Select


class Utilities:
    def getHeading(driver, headingNum=1):
        element = NiagaraSchedulePage.table_date_heading(headingNum)
        print("Element heading returned")
        return element

    def getSubHeading(driver, headingNum=1):
        element = NiagaraSchedulePage.table_sport_headings(headingNum)
        print ("Element subheading returned")
        return element

    def getGameTimes(driver, headingNum=1):
        element = NiagaraSchedulePage.game_times(headingNum)
        return element
    
    def getGameEvents(driver, headingNum=1):
        element = NiagaraSchedulePage.game_events(headingNum)
        return element

    def getGameNames(driver, headingNum=1):
        element = NiagaraSchedulePage.game_names(headingNum)
        return element

    def getGameLocations(driver, headingNum=1):
        element = NiagaraSchedulePage.game_locations(headingNum)
        return element


    def getEvent(self, driver, eventNum, headingNum=1,  subHeading=False):
        #subHeading variable decides if we look at the subheading or not.
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
        #Selenium driver needs to be initialized to the right website first.
        return driver.find_element(*element).text


    def getContingentDropdown(driver):
        """
        gets the XPATH for the contingent dropdown on the Canada Summer Games page and finds the element.

        :param WebDriver driver: driver used to find element.

        :return WebElement: element to be used.
        """
        element = CanadaGamesPlayerPage.contingent_dropdown()
        element = driver.find_element(*element)
        return element
    
    def getFindButton(driver):
        """
        Gets the XPATH for the Find button on the Canada summer games.

        :param WebDriver driver: driver used to find element.

        :return WebElement: element to be used.
        """
        element = CanadaGamesPlayerPage.find_button()
        element = driver.find_element(*element)

        return element
    
    def get_table_rows(driver):
        """
        """
        element = CanadaGamesPlayerPage.table_rows()
        elements = driver.find_elements(*element)

        return elements

    def getTableSport(driver, index):
        """
        """
        element = CanadaGamesPlayerPage.table_row_sport(index)
        element = driver.find_element(*element)

        return element

    def getTablePlayer(driver, index):
        element = CanadaGamesPlayerPage.table_row_player(index)
        element = driver.find_element(*element)

        return element

    def getHometown(driver):
        """
        Gets home town of person on personal page if the driver is on the correct page.
        
        :param WebDriver driver: Driver used to search for element.

        :Return: WebElement.
        """
        element = CanadaGamesPersonPage.person_hometown()
        element = driver.find_element(*element)

        return element

    def getName(driver):
        """
        Gets name of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Driver used to search for element.

        :Return: WebElement
        """

        element = CanadaGamesPersonPage.person_name()
        element = driver.find_element(*element)

        return element

    def getContingent(driver):
        """
        Gets contingent of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Driver used to search for element.

        :Return: WebElement
        """

        element = CanadaGamesPersonPage.person_contingent()
        element = driver.find_element(*element)

        return element

    def getType(driver):
        """
        Gets type of person on personal page if the driver is on the correct page. Type is the persons role e.g. athlete/coach/trainer.

        :param WebDriver driver: Driver used to search for element.

        :Return: WebElement
        """

        element = CanadaGamesPersonPage.person_type()
        element = driver.find_element(*element)

        return element

    def getSport(driver):
        """
        Gets sport of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Driver used to search for element.

        :Return: WebElement
        """

        element = CanadaGamesPersonPage.person_sport()
        element = driver.find_element(*element)

        return element

    def getAge(driver):
        """
        Gets age of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Driver used to search for element.

        :Return: WebElement
        """

        element = CanadaGamesPersonPage.person_age()
        element = driver.find_element(*element)

        return element

    def getHeight(driver):
        """
        Gets height of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Driver used to search for element.

        :Return: WebElement
        """

        element = CanadaGamesPersonPage.person_height()
        element = driver.find_element(*element)

        return element

    def getWeight(driver):
        """
        Gets weight of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Driver used to search for element.

        :Return: WebElement
        """

        element = CanadaGamesPersonPage.person_weight()
        element = driver.find_element(*element)

        return element

    def getClub(driver):
        """
        Gets Club or Team of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Driver used to search for element.

        :Return: WebElement
        """

        element = CanadaGamesPersonPage.club_or_team_affiliation()
        element = driver.find_element(*element)

        return element

    def getCoachName(driver):
        """
        Gets name of coach of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Driver used to search for element.

        :Return: WebElement
        """

        element = CanadaGamesPersonPage.name_of_coach()
        element = driver.find_element(*element)

        return element
    
    def getPosition(driver):
        """
        Gets position of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Driver used to search for element.

        :Return: WebElement
        """

        element = CanadaGamesPersonPage.person_position()
        element = driver.find_element(*element)

        return element

    def getGoalsforTheGames(driver):
        """
        Gets 'my goals for the game' of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Driver used to search for element.

        :Return: WebElement
        """

        element = CanadaGamesPersonPage.my_goals_for_the_games()
        element = driver.find_element(*element)

        return element

    def getPersonalBestResultinEvent(driver):
        """
        Gets 'my personal best result in my event' of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Driver used to search for element.

        :Return: WebElement
        """

        element = CanadaGamesPersonPage.my_personal_best_result_in_my_event()
        element = driver.find_element(*element)

        return element

    def getAwardsorMajorAccomplishments(driver):
        """
        Gets 'awards or major accomplishments that I have received.' of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Driver used to search for element.

        :Return: WebElement
        """

        element = CanadaGamesPersonPage.awards_or_major_accomplishments_that_I_have_received()
        element = driver.find_element(*element)

        return element

    def getMyPersonalRoleModel(driver):
        """
        Gets 'My personal role model' of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Driver used to search for element.

        :Return: WebElement
        """

        element = CanadaGamesPersonPage.my_personal_role_model()
        element = driver.find_element(*element)

        return element
    
    def getOtherInformation(driver):
        """
        Gets 'Other information that could be of interest to the media' of person on personal page if the driver is on the correct page.

        :param WebDriver driver: Driver used to search for element.

        :Return: WebElement
        """

        element = CanadaGamesPersonPage.other_information_that_could_be_of_interest_to_the_media()
        element = driver.find_element(*element)

        return element

    

    def select_dropdown(webElement, driver):
        """
        Will take the select dropdown element found by driver and create a Select object.

        :param WebElement webElement: An element found by selenium driver.
        :param WebDriver driver: driver used to find webElement.

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

        :return: bool
        """

        dropdown.select_by_index(index)

        return True

    def select_dropdown_item_by_visible_text(dropdown, value):
        """
        Will take the Select object and select an item by value.

        :param Select dropdown: Dropdown to be controlled.
        :param string value: the number item to be accessed.

        :return: bool
        """

        dropdown.select_by_visible_text(value)

        return True

    def click_element( element):
        """
        Clicks on the web element provided using the driver provided
        :param WebElement element: element to be clicked on and found by driver

        :return: boolean
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

        :return: element
        :rtype: string
        """

        element = CanadaGamesMedalPage.gold_medal_count_by_contingent(contingentAbbrev)
        element = driver.find_element(*element)
        return element

    def get_silver_medal_count_for_contingent(driver, contingentAbbrev):
        """
        Gets the silver medal element from the webpage.

        :param String contingentAbbrev: This is the abbreviation for the contingent.

        :return: element
        :rtype: string
        """

        element = CanadaGamesMedalPage.silver_medal_count_by_contingent(contingentAbbrev)
        element = driver.find_element(*element)
        return element

    def get_bronze_medal_count_for_contingent(driver, contingentAbbrev):
        """
        Gets the bronze medal element from the webpage.

        :param String contingentAbbrev: This is the abbreviation for the contingent.

        :return: element
        :rtype: string
        """

        element = CanadaGamesMedalPage.bronze_medal_count_by_contingent(contingentAbbrev)
        element = driver.find_element(*element)
        return element

    def get_total_medal_count_for_contingent(driver, contingentAbbrev):
        """
        Gets the total medal element from the webpage.

        :param String contingentAbbrev: This is the abbreviation for the contingent.

        :return: element
        :rtype: string
        """

        element = CanadaGamesMedalPage.total_medal_count_by_contingent(contingentAbbrev)
        element = driver.find_element(*element)
        return element

    




