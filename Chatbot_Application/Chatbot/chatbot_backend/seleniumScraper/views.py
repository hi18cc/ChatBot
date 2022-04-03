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
from . import Utilities
from . import KeyValues
from . import SQLMethods


database = r"./4P02 Chatbot Database.db"

chrome_options = Options()  
chrome_options.add_argument("--headless")  
chrome_options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
driver.implicitly_wait(2)
wait = WebDriverWait(driver, 5)
URL = 'https://cg2022.gems.pro/Result/Calendar.aspx?SetLanguage=en-CA&GameDay_GUID=3b285a03-5d46-4ae9-9da9-7eff7bcf6bef&Grouping=DS'
#conn = SQLMethods.create_connection(database)


def navigate(url):
    
        driver.get(url)
        title = driver.title
        print(driver.title)
        return title

def getInfo(element):
    print("finding element ====")
    number = 1
    info = driver.find_element(*element).text
    return info

    
def view_name(request):
    get_contingent_games()
    return HttpResponse("Done")


def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

    print("test")

def get_players():
    """
    """

    url = "https://cg2019.gems.pro/Result/ShowPerson_List.aspx?"
    driver.get(url)

    #Select contingent from SQL database
    conn = SQLMethods.create_connection(database)
    contingents = SQLMethods.sql_select_contingentName_from_contingents_table(conn)

    #Loop through all players, get player sport if not in database add sport and then add name
    for contingent in contingents:
        contingent_dropdown_webelement = Utilities.getContingentDropdown(driver)
        find_button = Utilities.getFindButton(driver)
        contingent_dropdown_select = Utilities.select_dropdown(contingent_dropdown_webelement, driver)
        Utilities.select_dropdown_item_by_visible_text(contingent_dropdown_select,contingent)
        Utilities.click_element(find_button)
        rows = Utilities.get_table_rows(driver)
        row_count = len(rows) -1
        row_range = range(1,row_count-1)

        for i in row_range:
            sport = Utilities.getTableSport(driver, i)
            sport = sport.text
            if not SQLMethods.sql_exists_for_sports_by_name(conn, sport):
                SQLMethods.insert_sports(conn, (sport,))
            person = Utilities.getTablePlayer(driver, i)
            personURL = Utilities.get_URL_from_element(person)
            person = person.text
            
            SQLMethods.insert_person_with_contingent_sportName_playerName(conn, contingent, sport, person, personURL)
      

def getData():
    dates = KeyValues.GameDay_Keys
    sports = KeyValues.Sport_Keys
    dateCount = range(len(dates))
    sportCount = range(len(sports))

    gameTimesXPath = Utilities.getGameTimes(driver)
    gameEventsXPath = Utilities.getGameEvents(driver)
    gameNamesXPath = Utilities.getGameNames(driver)
    gameLocationsXPath = Utilities.getGameLocations(driver)
    gameDateXPath = Utilities.getHeading(driver)
    sportNameXPath = Utilities.getSubHeading(driver)

    conn = SQLMethods.create_connection(database)
    
    for i in dateCount:
        for j in sportCount:
            url = KeyValues.getURL(dates[i][1],sports[j][1])
            driver.get(url)
            try:
                gameDate = driver.find_element(*gameDateXPath).text
            except Exception as e:
                print("----SKIP-----")
                continue
            sportName = driver.find_element(*sportNameXPath).text
            gameTimes = driver.find_elements(*gameTimesXPath)
            gameEvents = driver.find_elements(*gameEventsXPath)
            gameNames = driver.find_elements(*gameNamesXPath)
            gameLocations = driver.find_elements(*gameLocationsXPath)

            gameCount = range(len(gameTimes))

 
            for m in gameCount:
                gameTime = gameTimes[m].text
                gameEvent = gameEvents[m].text
                gameName = gameNames[m].text
                gameLocation = gameLocations[m].text
                with conn:
                    game = (gameName,sportName,gameLocation,gameEvent,gameDate,gameTime)
                    sport = (sportName,)
                    location = (gameLocation,)
                    sportLocation = (sportName, gameLocation)
                    SQLMethods.insert_sports(conn, sport)
                    SQLMethods.insert_games(conn, game)
                    SQLMethods.insert_locations(conn, location)
                    SQLMethods.insert_sportLocations(conn, sportLocation)

def fill_player_data():
    conn = SQLMethods.create_connection(database)

    persons = SQLMethods.sql_select_url_and_id_from_persons(conn)

    for person in persons:
        driver.get(person[1])

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
        
        print("ID is: " + str(person[0]))
        SQLMethods.sql_update_hometown_type_age_hieght_weight_club_coach_position_goals_for_games_personal_best_result_award_personal_role_model_other_info_for_person(
            conn, hometown, type, age, height, weight, club, coach, position, goals_for_games, 
            personal_best_result, personal_award,personal_role_model, other_info, person[0]
        )

def get_contingent_games():
    dates = KeyValues.GameDay_Keys
    sports = KeyValues.Sport_Keys
    contingents = KeyValues.Contingent_Keys
    dateCount = range(len(dates))
    sportCount = range(len(sports))
    contingentCount = range(6, len(contingents))

    gameTimesXPath = Utilities.getGameTimes(driver)
    gameNamesXPath = Utilities.getGameNames(driver)
    gameDateXPath = Utilities.getHeading(driver)
    sportNameXPath = Utilities.getSubHeading(driver)

    conn = SQLMethods.create_connection(database)
    for h in contingentCount:
        for i in dateCount:
            for j in sportCount:
                url = KeyValues.getURL(dates[i][1],sports[j][1], contingents[h][1])
                
                driver.get(url)
                try:
                    driver.find_element(*gameDateXPath).text
                except Exception as e:
                    print("----SKIP-----")
                    continue
                gameTimes = driver.find_elements(*gameTimesXPath)
                gameNames = driver.find_elements(*gameNamesXPath)
                sportName = driver.find_element(*sportNameXPath).text

                gameCount = range(len(gameTimes))
                print(url)
                contingents[h][0]
                for m in gameCount:
                    gameName = gameNames[m].text
                    with conn:
                        SQLMethods.insert_ContingentGames(conn, gameName,  contingents[h][0], sportName)


                

            

                

                


                

            

                



            

