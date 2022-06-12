import os

from django.http import HttpResponse
from django.shortcuts import redirect, render
#selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Extras
from . import urls
from seleniumScraper.Utilities import Utilities
from seleniumScraper.KeyValues import KeyValues
from seleniumScraper.SQLMethods import SQLMethods


database = r"./4P02 Chatbot Database.db"

chrome_options = Options()  
chrome_options.add_argument("--headless")  #makes the navigation windowless.
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging']) #used to prevent some errors.
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
driver.implicitly_wait(2) #we will wait only 2 seconds 
wait = WebDriverWait(driver, 5) #used for up to a 5 second wait.
URL = 'https://cg2022.gems.pro/Result/Calendar.aspx?SetLanguage=en-CA&GameDay_GUID=3b285a03-5d46-4ae9-9da9-7eff7bcf6bef&Grouping=DS'
#conn = SQLMethods.create_connection(database)


    
def view_name(request):
    conn = SQLMethods.create_connection(database)
    test =SQLMethods.sql_select_person_by_person_name_all_columns(conn,'Beaton')
    # update_medals()
    # print("Medals Done")
    # fill_player_data()
    return HttpResponse(str(test))


def get_players():
    """
    Adds players from https://cg2019.gems.pro to the database declared in database variable. This method gets webelement directly from Utilities.
    """

    url = "https://cg2019.gems.pro/Result/ShowPerson_List.aspx?"
    driver.get(url)

    #Select contingent from SQL database
    conn = SQLMethods.create_connection(database)
    contingents = SQLMethods.sql_select_contingentName_from_contingents_table(conn)

    #Loop through all players, get player sport if not in database add sport and then add name
    for contingent in contingents:
        contingent_dropdown_webelement = Utilities.getContingentDropdown(driver) # uses the driver to get WebElement
        find_button = Utilities.getFindButton(driver) #driver finds button element.
        contingent_dropdown_select = Utilities.select_dropdown(contingent_dropdown_webelement, driver) # Select dropdown
        Utilities.select_dropdown_item_by_visible_text(contingent_dropdown_select,contingent) # Will click the dropdown and select the contingent
        Utilities.click_element(find_button) # Hits the search button to pull up query.
        rows = Utilities.get_table_rows(driver) # gets the table ements for the rows.
        row_count = len(rows) -1
        row_range = range(1,row_count-1)

        for i in row_range:
            sport = Utilities.getTableSport(driver, i) # gets the webelement for the sport cell according to i.
            sport = sport.text #gets the text from the webelement.
            if not SQLMethods.sql_exists_for_sports_by_name(conn, sport): #if the sport doesn't exist we need to add it.
                SQLMethods.insert_sports(conn, (sport,)) # we insert the sport name into our SQL table.
            person = Utilities.getTablePlayer(driver, i) # We get the player name element based off i (the row we're looking at).
            personURL = Utilities.get_URL_from_element(person) # Gets URL text for the current person.
            person = person.text # Get text form the web element.
            
            SQLMethods.insert_person_with_contingent_sportName_personName(conn, contingent, sport, person, personURL)
      

def get_game_schedules():
    """
    Gets game data from the https://cg2022.gems.pro/ site and adds it to the database variable.
    This methods Utilities has to get the XPATH and then find elements unlike player.
    """
    dates = KeyValues.GameDay_Keys # Hard coded dates.
    sports = KeyValues.Sport_Keys # Hard coded sports.
    dateCount = range(len(dates)) # Gets number of dates to be used in for loop.
    sportCount = range(len(sports)) #Gets number of sports to be used in for loop.

    gameTimesXPath = Utilities.getGameTimes(driver) # These get the XPath but not the actual element unlike getPlayers()
    gameEventsXPath = Utilities.getGameEvents(driver)
    gameNamesXPath = Utilities.getGameNames(driver)
    gameLocationsXPath = Utilities.getGameLocations(driver)
    gameDateXPath = Utilities.getHeading(driver)
    sportNameXPath = Utilities.getSubHeading(driver)

    conn = SQLMethods.create_connection(database) # This uses the database path to connect and allow us to make changes.
    
    for i in dateCount: # for each date
        for j in sportCount: #we get the information for each sport.
            url = KeyValues.getURL(dates[i][1],sports[j][1]) # The URL's have a special key based on dates and sports so we use those to get access.
            driver.get(url) # We navigate to the URL.
            try: # We try to find the gamedate element
                gameDate = driver.find_element(*gameDateXPath).text
            except Exception as e: #If we don't find gameDate we can assume that there's no games for that sporto n that date.
                print("----SKIP-----")
                continue
            sportName = driver.find_element(*sportNameXPath).text #we find the elements and try and get the texts.
            gameTimes = driver.find_elements(*gameTimesXPath)
            gameEvents = driver.find_elements(*gameEventsXPath)
            gameNames = driver.find_elements(*gameNamesXPath)
            gameLocations = driver.find_elements(*gameLocationsXPath)

            gameCount = range(len(gameTimes)) # We get the number of games found.

 
            for m in gameCount: #For each game we navigate and then insert into the right spots.
                gameTime = gameTimes[m].text
                gameEvent = gameEvents[m].text
                gameName = gameNames[m].text
                gameLocation = gameLocations[m].text
                with conn: #this is where we do our inserts into the SQL.
                    game = (gameName,sportName,gameLocation,gameEvent,gameDate,gameTime)  
                    sport = (sportName,)
                    location = (gameLocation,)
                    sportLocation = (sportName, gameLocation)
                    SQLMethods.insert_sports(conn, sport)
                    SQLMethods.insert_games(conn, game)
                    SQLMethods.insert_locations(conn, location)
                    SQLMethods.insert_sportLocations(conn, sportLocation)

def fill_player_data():
    """
    This fills the bio for the person on their bio page. It uses SQL update to change from null to data.
    """
    conn = SQLMethods.create_connection(database)
    driver.implicitly_wait(1)
    
    persons = SQLMethods.sql_select_url_and_id_from_persons(conn)

    for person in persons: #we try to insert what we can.
        driver.get(person[1]) #this provides the link for each person.

        #Multiple try and catch to insert data.
        try:
            hometown = Utilities.getHometown(driver).text
        except Exception as e:
            hometown = 'NULL'

        try:
            type = Utilities.getType(driver).text
        except Exception as e:
            type = 'NULL'

        try:
            age = Utilities.getAge(driver).text
        except Exception as e:
            age = 'NULL'

        try:
            height = Utilities.getHeight(driver).text
        except Exception as e:
            height = 'NULL'
        
        try:
            weight = Utilities.getWeight(driver).text
        except Exception as e:
            weight = 'NULL'

        try:
            club = Utilities.getClub(driver).text
        except Exception as e:
            club = 'NULL'

        try:
            coach = Utilities.getCoachName(driver).text
        except Exception as e:
            coach = 'NULL'

        try:
            position = Utilities.getPosition(driver).text
        except Exception as e:
            position = 'NULL' 

        try:
            goals_for_games = Utilities.getGoalsforTheGames(driver).text
        except Exception as e:
            goals_for_games = 'NULL'

        try:
            personal_best_result = Utilities.getPersonalBestResultinEvent(driver).text
        except Exception as e:
            personal_best_result = 'NULL'

        try:
            personal_award = Utilities.getAwardsorMajorAccomplishments(driver).text
        except Exception as e:
            personal_award = 'NULL'

        try:
            personal_role_model = Utilities.getMyPersonalRoleModel(driver).text
        except Exception as e:
            personal_role_model = 'NULL'

        try:
            other_info = Utilities.getOtherInformation(driver).text
        except Exception as e:
            other_info = 'NULL'
        
        #finally we update using SQL
        SQLMethods.sql_update_hometown_type_age_hieght_weight_club_coach_position_goals_for_games_personal_best_result_award_personal_role_model_other_info_for_person(
            conn, hometown, type, age, height, weight, club, coach, position, goals_for_games, 
            personal_best_result, personal_award,personal_role_model, other_info, person[0]
        )

def get_contingent_games():
    """
    This matches the games to the contingents in the SQL table ContingentGames.
    """
    
    dates = KeyValues.GameDay_Keys # Hard coded array of values.
    sports = KeyValues.Sport_Keys  # Hard coded array of values.
    contingents = KeyValues.Contingent_Keys # Hard coded array of values.
    dateCount = range(len(dates)) # number of dates to loop.
    sportCount = range(len(sports)) # number of sports to loop.
    contingentCount = range(6, len(contingents)) # number of contingents to loop through

    gameTimesXPath = Utilities.getGameTimes(driver)  #these methods get the XPATH but not the webelement.
    gameNamesXPath = Utilities.getGameNames(driver)
    gameDateXPath = Utilities.getHeading(driver)
    sportNameXPath = Utilities.getSubHeading(driver)

    conn = SQLMethods.create_connection(database) # connects to the databse variable.
    for h in contingentCount:
        for i in dateCount:
            for j in sportCount:
                url = KeyValues.getURL(dates[i][1],sports[j][1], contingents[h][1])
                
                driver.get(url)
                try: # We try to find the gameDate element but if it doesn't exist we skip.
                    driver.find_element(*gameDateXPath).text 
                except Exception as e:
                    print("----SKIP-----")
                    continue
                gameTimes = driver.find_elements(*gameTimesXPath) # We find the elements on the page.
                gameNames = driver.find_elements(*gameNamesXPath)
                sportName = driver.find_element(*sportNameXPath).text

                gameCount = range(len(gameTimes)) # Number of games available.
                contingents[h][0] #h is the contingnet number we're looking at
                for m in gameCount:
                    gameName = gameNames[m].text #m is the row number.
                    with conn:
                        SQLMethods.insert_ContingentGames(conn, gameName,  contingents[h][0], sportName) #we insert.

def update_medals():
    """
    Updates the medal count in the SQL database.
    """       

    url = "https://cg2019.gems.pro/Result/MedalList.aspx?SetLanguage=en-CA"
    
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.implicitly_wait(1)
    driver.get(url)
    

    conn = SQLMethods.create_connection(database) # connects to our database

    for x in KeyValues.Contingent_Acronym: # we use the contingent acronym to find the row and add.
        cAbbrev = x[0]
        gold = Utilities.get_gold_medal_count_for_contingent(driver, cAbbrev).text # finds element and it's text.
        silver = Utilities.get_silver_medal_count_for_contingent(driver, cAbbrev).text
        bronze = Utilities.get_bronze_medal_count_for_contingent(driver, cAbbrev).text
        total = Utilities.get_total_medal_count_for_contingent(driver, cAbbrev).text

        SQLMethods.sql_update_medals(conn, gold, silver, bronze, total, cAbbrev)
            

    

                


                

            

                



            

