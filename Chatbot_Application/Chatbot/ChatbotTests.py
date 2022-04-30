import unittest
from bot import chat

class TestAskingForCanadaGamesWebsite (unittest.TestCase):
	def testCorrectSpelling (self):
		response = chat ("What is the Canada games website")
		assert any([response == "The link to the Canada Game website is https://niagara2022games.ca", response == "You can get to the Canada Game website by using this link: https://niagara2022games.ca"]),"Correct spelling failure. The output recieved was not the expected response, response = " + response
    
	def testAbbriviation (self):
		response = chat ("Th Canada Games web")
		assert any([response == "The link to the Canada Game website is https://niagara2022games.ca", response == "You can get to the Canada Game website by using this link: https://niagara2022games.ca"]),"Abbriviation spelling failure. The output recieved was not the expected response, response = " + response
	
	def testRandomInput (self):
		response = chat ("The sky is blue")
		assert all([response != "You can get to the Canada Game website by using this link: https://niagara2022games.ca/?gclid=Cj0KCQiA-qGNBhD3ARIsAO_o7ym4JMO1oHPSmRfiX047qNfEf9FtK22b_Y8FrkJQxEMnOcZFlv3MbCEaAtQiEALw_wcB", response != "The link to the Canada Game website is https://niagara2022games.ca/?gclid=Cj0KCQiA-qGNBhD3ARIsAO_o7ym4JMO1oHPSmRfiX047qNfEf9FtK22b_Y8FrkJQxEMnOcZFlv3MbCEaAtQiEALw_wcB"]),"Random input failure. The input called the ask for website function, response = " + response
		
	
	def testIncorrectSpelling (self):
		response = chat ("Th Kanade Geams web")
		assert all([response != "You can get to the Canada Game website by using this link: https://niagara2022games.ca/?gclid=Cj0KCQiA-qGNBhD3ARIsAO_o7ym4JMO1oHPSmRfiX047qNfEf9FtK22b_Y8FrkJQxEMnOcZFlv3MbCEaAtQiEALw_wcB", response != "The link to the Canada Game website is https://niagara2022games.ca/?gclid=Cj0KCQiA-qGNBhD3ARIsAO_o7ym4JMO1oHPSmRfiX047qNfEf9FtK22b_Y8FrkJQxEMnOcZFlv3MbCEaAtQiEALw_wcB"]),"Incorrect spelling failure. The output recieved was a string containing link to canada games url, response = " + response
	
class TestAksingAboutTransit (unittest.TestCase):
	
	def testCorrectSpelling (self):
		response = chat ("What transport options are available.")
		assert response == "Niagara Region Transit information is available here: https://www.niagararegion.ca/transit/", "Incorrect response returned, something other than a response from function. Response = " + response
	
	def testAlternateInput (self):
		response = chat ("How can I get there.")
		assert response == "Niagara Region Transit information is available here: https://www.niagararegion.ca/transit/", "Did not return expected ouput from function. Response = " + response
	
	def testRandomInput (self):
		response = chat ("What car do I drive.")
		assert response != "Niagara Region Transit information is available here: https://www.niagararegion.ca/transit/", "Inorrect input error, function response returned. Response = " + response
	
	def testIncorrectSpelling (self):
		response = chat ("trainsport options")
		assert response != "Niagara Region Transit information is available here: https://www.niagararegion.ca/transit/", "Incorrect input error, function response returned. Response = " + response
	
	
class TestAskingAboutTransitApp (unittest.TestCase):
	
	def testCorrectSpelling (self):
		response = chat ("Is there an app for buses?")
		assert response == "The Niagara Reigon Transit app for Android is avaiable here https://play.google.com/store/apps/details?id=com.thetransitapp.droid and a version for iOS is available here https://apps.apple.com/ca/app/transit-bus-train-times/id498151501", "Correct spelling error. Function did not return proper output, response = " + response
	
	def testAbbriviation (self):
		response = chat ("bus app")
		assert response == "The Niagara Reigon Transit app for Android is avaiable here https://play.google.com/store/apps/details?id=com.thetransitapp.droid and a version for iOS is available here https://apps.apple.com/ca/app/transit-bus-train-times/id498151501", "Abbriviation spelling error. Function did not return proper output, response = " + response
	
	def testRandomInput (self):
		response = chat ("what colour is the road?")
		assert response != "The Niagara Reigon Transit app for Android is avaiable here https://play.google.com/store/apps/details?id=com.thetransitapp.droid and a version for iOS is available here https://apps.apple.com/ca/app/transit-bus-train-times/id498151501", "Random input error. Function returned output for the function, response = " + response
	
	def testIncorrectSpelling (self):
		response = chat ("bis apy")
		assert response != "The Niagara Reigon Transit app for Android is avaiable here https://play.google.com/store/apps/details?id=com.thetransitapp.droid and a version for iOS is available here https://apps.apple.com/ca/app/transit-bus-train-times/id498151501", "Inorrect spelling error. Function returned output, response = " + response
	
	
class TestAksingTourism(unittest.TestCase):
	
	def testCorrectSpelling (self):
		response = chat ("What can you do in Niagara region?")
		assert response == "The Niagara Falls Tourism website provided here https://www.niagarafallstourism.com/niagara-region/ has information about what you can see and do in the region", "Correct input error. Function did not return expected output, response = " + response
	
	def testAbbriviation (self):
		response = chat ("Niagara region")
		assert response == "The Niagara Falls Tourism website provided here https://www.niagarafallstourism.com/niagara-region/ has information about what you can see and do in the region", "Abbriviation input error. Function did not return expected output, response = " + response
	
	def testRandomInput (self):
		response = chat ("Any arcades")
		assert response != "The Niagara Falls Tourism website provided here https://www.niagarafallstourism.com/niagara-region/ has information about what you can see and do in the region", "Random input error. Function returned function output, response = " + response
	
	def testIncorrectSpelling (self):
		response = chat ("turism nia ragion")
		assert response != "The Niagara Falls Tourism website provided here https://www.niagarafallstourism.com/niagara-region/ has information about what you can see and do in the region", "Inorrect input error. Function did not return expected output, response = " + response
		
class TestAksingHotels(unittest.TestCase):
	
	def testCorrectSpelling (self):
		response = chat ("Where can you stay in Niagara Region?")
		assert response == "The Niagara Falls Tourism website provided here https://www.niagarafallstourism.com/niagara-region/ has information about accommodations in the Niagara Region ", "Correct input error. Function did not return expected output, response = " + response
	
	def testAbbriviation (self):
		response = chat ("Niagara region")
		assert response == "The Niagara Falls Tourism website provided here https://www.niagarafallstourism.com/niagara-region/ has information about what you can see and do in the region", "Abbriviation input error. Function did not return expected output, response = " + response
	
	def testRandomInput (self):
		response = chat ("five star")
		assert response != "The Niagara Falls Tourism website provided here https://www.niagarafallstourism.com/niagara-region/ has information about what you can see and do in the region", "Random input error. Function returned function output, response = " + response
	
	def testIncorrectSpelling (self):
		response = chat ("ware kan u sty in Nagra Rejin")
		assert response != "The Niagara Falls Tourism website provided here https://www.niagarafallstourism.com/niagara-region/ has information about what you can see and do in the region", "Inorrect input error. Function did not return expected output, response = " + response
  
		
class TestAksingCovid19(unittest.TestCase):
	
	def testCorrectSpelling (self):
		response = chat ("What are the COVID-19 restrictions like in Niagara?")
		assert response == "The Niagara region COVID-19 information can be found here https://www.niagararegion.ca/health/covid-19/", "Correct input error. Function did not return expected output, response = " + response
	
	def testAbbriviation (self):
		response = chat ("Covid-19")
		assert response == "The Niagara region COVID-19 information can be found here https://www.niagararegion.ca/health/covid-19/", "Abbriviation input error. Function did not return expected output, response = " + response
	
	def testDifferentInput (self):
		response = chat ("i'm sick")
		assert response == "The Niagara region COVID-19 information can be found here https://www.niagararegion.ca/health/covid-19/default.aspx?topic=1", "Random input error. Function returned function output, response = " + response
		
class TestAksingStartDate(unittest.TestCase):
	
	def testCorrectSpelling (self):
		response = chat ("How long until Canada games starts?")
		assert response == "Saturday, August 6, 2022", "Correct input error. Function did not return expected output, response = " + response
	
	def testAbbriviation (self):
		response = chat ("start")
		assert response == "Saturday, August 6, 2022", "Abbriviation input error. Function did not return expected output, response = " + response

			
class TestAksingNews(unittest.TestCase):
	
	def testCorrectSpelling (self):
		response = chat ("What’s new with the Canada games?")
		assert response == "The Canada Games news is available here https://niagara2022games.ca/news/", "Correct input error. Function did not return expected output, response = " + response
	
	def testAbbriviation (self):
		response = chat ("News Canada games?")
		assert response == "The Canada Games news is available here https://niagara2022games.ca/news/", "Abbriviation input error. Function did not return expected output, response = " + response
	
	def testJustNews (self):
		response = chat ("News")
		assert response == "The Canada Games news is available here https://niagara2022games.ca/news/", "Abbriviation input error. Function did not return expected output, response = " + response
	
class TestAksingLocation(unittest.TestCase):
	
	def testCorrectSpelling (self):
		response = chat ("Where is the Canada games?")
		assert response == "The Canada Games events will be taking place in various locations across the Niagara region, locations for specific sports can be found here https://niagara2022games.ca/sports/", "Correct input error. Function did not return expected output, response = " + response
	
	def testAbbriviation (self):
		response = chat ("Where")
		assert response == "The Canada Games events will be taking place in various locations across the Niagara region, locations for specific sports can be found here https://niagara2022games.ca/sports/", "Abbriviation input error. Function did not return expected output, response = " + response
	
	def testIncorrectSpelling (self):
		response = chat ("ware Kanade gaems?")
		assert response != "The Canada Games news is available here https://niagara2022games.ca/news/", "Inorrect input error. Function did not return expected output, response = " + response
	
class TestAthlete(unittest.TestCase):
	
	def testValidInput (self):
		response = chat ("Tell me about Kelsey Ayers")
		assert response == "<b>Person Name: </b>Kelsey Ayers<br/><b>Contingent: </b>Alberta<br/><b>Sport Name: </b>Artistic Swimming<br/><b>Hometown: </b>Calgary<br/><b>Type: </b>Athlete<br/><b>Age: </b>17<br/><b>Height: </b>165 cm<br/><b>Weight: </b>56.5 kg<br/><b>Club: </b>Calgary Aquabelles<br/><b>Coach: </b>Jenn Tregale and Courtenay Grant<br/><b>Position: </b>team member<br/><b>Goals for Games: </b>My goals for the games are to have fun and swim the best as a team and as an individual swimmer<br/><b>Personal Best Result: </b>My personal best result in swimming would be from 2017 in Toronto when my team achived our goal of coming first at nationals.<br/><b>Award: </b>In 2017 I recieved most improved junior.<br/><b>Personal Role Model: </b>my personal role model is my mom, because she is always pushing herself to do more even if it's for her coaching or if it's for her family. She is always working and improving on things she loves and really pushes me to do the same.<br/><b>Other Info: </b>I got involved in artistic swimming when I was four years old. My mom had been coaching and I had joined after I saw how much fun the girls were having. after a few weeks of trying it out, I asked my mom if I could continue during the regular season. Then she put me in my first club Atlantis Synchro in Halifax Nova Scotia. Where I continued my career until 2013 when I moved to calgary where I continue to train.<br/>https://cg2019.gems.pro/Result/ShowPerson.aspx?Person_GUID=b18edb7a-a8e2-4e88-ba3e-591e1e8ed156&SetLanguage=en-CA<br/><br/>", "Valid input error. Function did not return expected output, response = " + response
	
	def testInvalidInput (self):
		response = chat ("Tell me about eminem")
		assert response != "<b>Person Name: </b>Kelsey Ayers<br/><b>Contingent: </b>Alberta<br/><b>Sport Name: </b>Artistic Swimming<br/><b>Hometown: </b>Calgary<br/><b>Type: </b>Athlete<br/><b>Age: </b>17<br/><b>Height: </b>165 cm<br/><b>Weight: </b>56.5 kg<br/><b>Club: </b>Calgary Aquabelles<br/><b>Coach: </b>Jenn Tregale and Courtenay Grant<br/><b>Position: </b>team member<br/><b>Goals for Games: </b>My goals for the games are to have fun and swim the best as a team and as an individual swimmer<br/><b>Personal Best Result: </b>My personal best result in swimming would be from 2017 in Toronto when my team achived our goal of coming first at nationals.<br/><b>Award: </b>In 2017 I recieved most improved junior.<br/><b>Personal Role Model: </b>my personal role model is my mom, because she is always pushing herself to do more even if it's for her coaching or if it's for her family. She is always working and improving on things she loves and really pushes me to do the same.<br/><b>Other Info: </b>I got involved in artistic swimming when I was four years old. My mom had been coaching and I had joined after I saw how much fun the girls were having. after a few weeks of trying it out, I asked my mom if I could continue during the regular season. Then she put me in my first club Atlantis Synchro in Halifax Nova Scotia. Where I continued my career until 2013 when I moved to calgary where I continue to train.<br/>https://cg2019.gems.pro/Result/ShowPerson.aspx?Person_GUID=b18edb7a-a8e2-4e88-ba3e-591e1e8ed156&SetLanguage=en-CA<br/><br/>", "Invalid input error. Function returned proper output, response = " + response
	
	def testRephrasing (self):
		response = chat ("is Kelsey Ayers participating")
		assert response == "<b>Person Name: </b>Kelsey Ayers<br/><b>Contingent: </b>Alberta<br/><b>Sport Name: </b>Artistic Swimming<br/><b>Hometown: </b>Calgary<br/><b>Type: </b>Athlete<br/><b>Age: </b>17<br/><b>Height: </b>165 cm<br/><b>Weight: </b>56.5 kg<br/><b>Club: </b>Calgary Aquabelles<br/><b>Coach: </b>Jenn Tregale and Courtenay Grant<br/><b>Position: </b>team member<br/><b>Goals for Games: </b>My goals for the games are to have fun and swim the best as a team and as an individual swimmer<br/><b>Personal Best Result: </b>My personal best result in swimming would be from 2017 in Toronto when my team achived our goal of coming first at nationals.<br/><b>Award: </b>In 2017 I recieved most improved junior.<br/><b>Personal Role Model: </b>my personal role model is my mom, because she is always pushing herself to do more even if it's for her coaching or if it's for her family. She is always working and improving on things she loves and really pushes me to do the same.<br/><b>Other Info: </b>I got involved in artistic swimming when I was four years old. My mom had been coaching and I had joined after I saw how much fun the girls were having. after a few weeks of trying it out, I asked my mom if I could continue during the regular season. Then she put me in my first club Atlantis Synchro in Halifax Nova Scotia. Where I continued my career until 2013 when I moved to calgary where I continue to train.<br/>https://cg2019.gems.pro/Result/ShowPerson.aspx?Person_GUID=b18edb7a-a8e2-4e88-ba3e-591e1e8ed156&SetLanguage=en-CA<br/><br/>", "Rephrase input error. Function did not return expected output, response = " + response
	
class TestSportInfo(unittest.TestCase):
		
	def testValidInput (self):
		response = chat ("what sport Kelsey Ayers play")
		assert response == "<i>Kelsey Ayers</i> participates in <b>Artistic Swimming</b>", "Rephrase input error. Function did not return expected output, response = " + response
	
	def testMultiple (self):
		response = chat ("what sport Aron Bargen play")
		assert response == "There are 2 player matching that name. <br/> Aron Bargen from Saskatchewan participates in Cross Country Skiing.<br/> Aron Bargen from Saskatchewan participates in Biathlon.<br/>", "Function did not return multple atheletes output, response = " + response
	
	def testDoesNotExist (self):
		response = chat ("what sport Kanye West play")
		assert response != "Kelsey Ayers participates in Artistic Swimming", "Doesn't exist error. Function returned a existing player response = " + response

class TestMedalCount(unittest.TestCase):
		
	def testOntario (self):
		response = chat ("How many medals does Ontario have?")
		assert response == "Ontario currently has <b>105</b> medals. <b>18</b> gold, <b>43</b> silver, <b>44</b> bronze", "Did not return expected output on ontario input, response = " + response
	
	def testInvalidProvince (self):
		response = chat ("How many medals does North Dakota have?")
		assert response == "Cannot find province or territory by that name", "Function returned a provinces medal count, response = " + response
	
	def testMisspelling (self):
		response = chat ("How many madels does Ontario have")
		assert response != "Ontario currently has <b>105</b> medals. <b>18</b> gold, <b>43</b> silver, <b>44</b> bronze", "function returned medal count. response = " + response
		
		
class TestEventTimes(unittest.TestCase):
	
	def testValidGameWithProvice (self):
		response = chat ("When is ontario's next basketball game")
		assert response == "<b>Game Name: </b>Preliminary | Pool B - Game 5 - ON vs PE</br><b>Dates: </b>2022-08-8</br> <b>Times: </b>17:30</br> <b>Location: </b>Niagara College - Welland Campus<br> <b>Game Name: </b>Preliminary | Pool A - Game 6 - NB vs ON</br><b>Dates: </b>2022-08-8</br> <b>Times: </b>19:45</br> <b>Location: </b>Meridian Centre<br> ", "Function 0 of the expected games. response = " + response
		
	def testValidGameWithoutProvince (self):
		response = chat ("When is the next basketball game")
		assert response == "<b>Game Name: </b>Preliminary | Pool B - Game 1 - MB vs NT</br> <b>Contingent: </b>Manitoba</br><b>Dates: </b>2022-08-8</br><b>Times: </b>08:30</br> <b>Location: </b>Niagara College - Welland Campus</br></br><b>Game Name: </b>Preliminary | Pool B - Game 1 - NS vs NT</br> <b>Contingent: </b>Northwest Territories</br><b>Dates: </b>2022-08-8</br><b>Times: </b>08:30</br> <b>Location: </b>Meridian Centre</br></br><b>Game Name: </b>Preliminary | Pool C - Game 2 - BC vs NL</br> <b>Contingent: </b>British Columbia</br><b>Dates: </b>2022-08-8</br><b>Times: </b>10:45</br> <b>Location: </b>Meridian Centre</br></br><b>Game Name: </b>Preliminary | Pool C - Game 2 - NL vs NS</br> <b>Contingent: </b>Newfoundland and Labrador</br><b>Dates: </b>2022-08-8</br><b>Times: </b>10:45</br> <b>Location: </b>Niagara College - Welland Campus</br></br><b>Game Name: </b>Preliminary | Pool C - Game 3 - AB vs YT</br> <b>Contingent: </b>Alberta</br><b>Dates: </b>2022-08-8</br><b>Times: </b>13:00</br> <b>Location: </b>Meridian Centre</br></br><b>Game Name: </b>Preliminary | Pool C - Game 3 - NB vs YT</br> <b>Contingent: </b>New Brunswick</br><b>Dates: </b>2022-08-8</br><b>Times: </b>13:00</br> <b>Location: </b>Niagara College - Welland Campus</br></br><b>Game Name: </b>Preliminary | Pool A - Game 4 - QC vs SK</br> <b>Contingent: </b>Quebec</br><b>Dates: </b>2022-08-8</br><b>Times: </b>15:15</br> <b>Location: </b>Niagara College - Welland Campus</br></br><b>Game Name: </b>Preliminary | Pool B - Game 5 - MB vs PE</br> <b>Contingent: </b>Manitoba</br><b>Dates: </b>2022-08-8</br><b>Times: </b>17:30</br> <b>Location: </b>Meridian Centre</br></br><b>Game Name: </b>Preliminary | Pool B - Game 5 - ON vs PE</br> <b>Contingent: </b>Ontario</br><b>Dates: </b>2022-08-8</br><b>Times: </b>17:30</br> <b>Location: </b>Niagara College - Welland Campus</br></br><b>Game Name: </b>Preliminary | Pool A - Game 6 - AB vs BC</br> <b>Contingent: </b>Alberta</br><b>Dates: </b>2022-08-8</br><b>Times: </b>19:45</br> <b>Location: </b>Niagara College - Welland Campus</br></br><b>Game Name: </b>Preliminary | Pool A - Game 6 - NB vs ON</br> <b>Contingent: </b>New Brunswick</br><b>Dates: </b>2022-08-8</br><b>Times: </b>19:45</br> <b>Location: </b>Meridian Centre</br></br>", "Function did not return the expected basketball games. response = " + response	
	
	def testValidProvince (self):
		
		response = chat ("when is ontario's next game?")
		assert response == "Here are the upcoming games for Ontario<br><b>Game Name: </b>Preliminary | Pool A - Game 27 - NS vs ON</br> <b>Sport Name: </b>Baseball</br><b>Dates: </b>2022-08-10</br><b>Times: </b>19:00</br> <b>Location: </b>Welland Baseball Stadium</br></br><b>Game Name: </b>Preliminary | Pool A - Duel 1089 - AB vs ON</br> <b>Sport Name: </b>Wrestling</br><b>Dates: </b>2022-08-10</br><b>Times: </b>08:30</br> <b>Location: </b>Canada Games Park</br></br><b>Game Name: </b>Preliminary | Pool B - Duel 6100 - ON vs YT</br> <b>Sport Name: </b>Wrestling</br><b>Dates: </b>2022-08-10</br><b>Times: </b>10:00</br> <b>Location: </b>Canada Games Park</br></br><b>Game Name: </b>Preliminary | Pool A - Duel 1111 - ON vs SK</br> <b>Sport Name: </b>Wrestling</br><b>Dates: </b>2022-08-10</br><b>Times: </b>12:30</br> <b>Location: </b>Canada Games Park</br></br><b>Game Name: </b>Preliminary | Pool B - Duel 3122 - AB vs ON</br> <b>Sport Name: </b>Wrestling</br><b>Dates: </b>2022-08-10</br><b>Times: </b>14:00</br> <b>Location: </b>Canada Games Park</br></br>", "Function did not return the expected games for ontario. response = " + response
		
class TestTicketInfo(unittest.TestCase):

	def testProperInput(self):
		response = chat ("where can i buy tickets?")
		assert response == "Tickets and ticket information can be obtained here https://niagara2022games.ca/tickets/", "No link to ticket info returned. response = " + response
		
	def testMisspelling(self):
		response = chat ("ware kan bye tickats?")
		assert response != "Tickets and ticket information can be obtained here https://niagara2022games.ca/tickets/", "A link was returned from misspelling. response = " + response
	

	
if __name__ == "__main__":
	unittest.main()