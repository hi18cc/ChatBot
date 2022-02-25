from seleniumScraper.PageObjects.NiagaraSchedulePage import NiagaraSchedulePage

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




