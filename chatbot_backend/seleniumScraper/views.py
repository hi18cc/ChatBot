import os

from django.http import HttpResponse
from django.shortcuts import redirect, render
#selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from seleniumScraper.SQLMethods import SQLMethods
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
#Extras
from . import urls
from seleniumScraper.utils import Utilities
from seleniumScraper.KeyValues import KeyValues


database = r"./4P02 Chatbot Database.db"

chrome_options = Options()  
chrome_options.add_argument("--headless")  
driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
driver.implicitly_wait(2)
wait = WebDriverWait(driver, 5)
URL = 'https://cg2022.gems.pro/Result/Calendar.aspx?SetLanguage=en-CA&GameDay_GUID=3b285a03-5d46-4ae9-9da9-7eff7bcf6bef&Grouping=DS'
conn = SQLMethods.create_connection(database)


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
    getData()
    return HttpResponse("Done")

    # printout = navigate(URL)
    # header = Utilities.getHeading(driver)
    # data =getInfo(header)
    # print("Data returned")
    # return HttpResponse(data)


def index(request):
    return HttpResponse("Hello, world. You're at the poll index.")

    print("test")

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
                

            

                

                


                

            

                



            

