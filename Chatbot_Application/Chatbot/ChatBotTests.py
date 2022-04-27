import unittest
from bot import chat

class TestAskingForCanadaGamesWebsite (unittest.TestCase):
	def testCorrectSpelling (self):
		response = chat ("What is the Canada games website")
		assert any([response == "You can get to the Canada Game website by using this link: https://niagara2022games.ca/?gclid=Cj0KCQiA-qGNBhD3ARIsAO_o7ym4JMO1oHPSmRfiX047qNfEf9FtK22b_Y8FrkJQxEMnOcZFlv3MbCEaAtQiEALw_wcB", response == "The link to the Canada Game website is https://niagara2022games.ca/?gclid=Cj0KCQiA-qGNBhD3ARIsAO_o7ym4JMO1oHPSmRfiX047qNfEf9FtK22b_Y8FrkJQxEMnOcZFlv3MbCEaAtQiEALw_wcB"]),"Correct spelling failure. The output recieved was not the expected response, response = " + response
    
	def testAbbriviation (self):
		response = chat ("Th Canada Games web")
		assert any([response == "You can get to the Canada Game website by using this link: https://niagara2022games.ca/?gclid=Cj0KCQiA-qGNBhD3ARIsAO_o7ym4JMO1oHPSmRfiX047qNfEf9FtK22b_Y8FrkJQxEMnOcZFlv3MbCEaAtQiEALw_wcB", response == "The link to the Canada Game website is https://niagara2022games.ca/?gclid=Cj0KCQiA-qGNBhD3ARIsAO_o7ym4JMO1oHPSmRfiX047qNfEf9FtK22b_Y8FrkJQxEMnOcZFlv3MbCEaAtQiEALw_wcB"]),"Abbriviation spelling failure. The output recieved was not the expected response, response = " + response
	
	def testRandomInput (self):
		response = chat ("The sky is blue")
		assert any([response != "You can get to the Canada Game website by using this link: https://niagara2022games.ca/?gclid=Cj0KCQiA-qGNBhD3ARIsAO_o7ym4JMO1oHPSmRfiX047qNfEf9FtK22b_Y8FrkJQxEMnOcZFlv3MbCEaAtQiEALw_wcB", response != "The link to the Canada Game website is https://niagara2022games.ca/?gclid=Cj0KCQiA-qGNBhD3ARIsAO_o7ym4JMO1oHPSmRfiX047qNfEf9FtK22b_Y8FrkJQxEMnOcZFlv3MbCEaAtQiEALw_wcB"]),"Random input failure. The input called the ask for website function, response = " + response
		
	
	def testIncorrectSpelling (self):
		response = chat ("Th Kanade Geams web")
		assert any([response != "You can get to the Canada Game website by using this link: https://niagara2022games.ca/?gclid=Cj0KCQiA-qGNBhD3ARIsAO_o7ym4JMO1oHPSmRfiX047qNfEf9FtK22b_Y8FrkJQxEMnOcZFlv3MbCEaAtQiEALw_wcB", response != "The link to the Canada Game website is https://niagara2022games.ca/?gclid=Cj0KCQiA-qGNBhD3ARIsAO_o7ym4JMO1oHPSmRfiX047qNfEf9FtK22b_Y8FrkJQxEMnOcZFlv3MbCEaAtQiEALw_wcB"]),"Incorrect spelling failure. The output recieved was a string containing link to canada games url, response = " + response
	
class TestAksingAboutTransit (unittest.TestCase):
	
	def testCorrectSpelling (self):
		response = chat ("What transport options are available.")
		assert response == "Niagara Region Transit information is available here: https://www.niagararegion.ca/transit/", "Correct input error, Incorrect response returned. Response = " + response
	
	def testAbbriviationSpelling (self):
		response = chat ("How can I get there.")
		assert response == "Niagara Region Transit information is available here: https://www.niagararegion.ca/transit/", "Abbriviation input error, Incorrect response returned. Response = " + response
	
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
		response = chat ("what colour is the bus?")
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
		assert response == "The Niagara Falls Tourism website provided here https://www.niagarafallstourism.com/niagara-region/ has information about what you can see and do in the region", "Correct input error. Function did not return expected output, response = " + response
	
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
		assert response == "The Niagara region COVID-19 information can be found here https://www.niagararegion.ca/health/covid-19/default.aspx?topic=1", "Correct input error. Function did not return expected output, response = " + response
	
	def testAbbriviation (self):
		response = chat ("Covid-19")
		assert response == "The Niagara region COVID-19 information can be found here https://www.niagararegion.ca/health/covid-19/default.aspx?topic=1", "Abbriviation input error. Function did not return expected output, response = " + response
	
	def testRandomInput (self):
		response = chat ("i'm sick")
		assert response != "The Niagara region COVID-19 information can be found here https://www.niagararegion.ca/health/covid-19/default.aspx?topic=1", "Random input error. Function returned function output, response = " + response
		
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
		assert response != "The Canada Games events will be taking place in various locations across the Niagara region, locations for specific sports can be found here https://niagara2022games.ca/sports/", "Abbriviation input error. Function did not return expected output, response = " + response
	
	def testIncorrectSpelling (self):
		response = chat ("ware Kanade gaems?")
		assert response != "The Canada Games news is available here https://niagara2022games.ca/news/", "Inorrect input error. Function did not return expected output, response = " + response
	
class TestAthlete(unittest.TestCase):
	
	def testValidInput (self):
		response = chat ("Tell me about Kelsey Ayers")
		assert response == "Alberta Artistic Swimming Kelsey Ayers https://cg2019.gems.pro/Result/ShowPerson.aspx?Person_GUID=b18edb7a-a8e2-4e88-ba3e-591e1e8ed156&SetLanguage=en-CA Calgary Athlete 17 165 cm 56.5 kg Calgary Aquabelles Jenn Tregale and Courtenay Grant team member My goals for the games are to have fun and swim the best as a team and as an individual swimmer My personal best result in swimming would be from 2017 in Toronto when my team achived our goal of coming first at nationals. In 2017 I recieved most improved junior. my personal role model is my mom, because she is always pushing herself to do more even if it's for her coaching or if it's for her family. She is always working and improving on things she loves and really pushes me to do the same. I got involved in artistic swimming when I was four years old. My mom had been coaching and I had joined after I saw how much fun the girls were having. after a few weeks of trying it out, I asked my mom if I could continue during the regular season. Then she put me in my first club Atlantis Synchro in Halifax Nova Scotia. Where I continued my career until 2013 when I moved to calgary where I continue to train. <br/>", "Valid input error. Function did not return expected output, response = " + response
	
	def testInvalidInput (self):
		response = chat ("Tell me about eminem")
		assert response != "Alberta Artistic Swimming Kelsey Ayers https://cg2019.gems.pro/Result/ShowPerson.aspx?Person_GUID=b18edb7a-a8e2-4e88-ba3e-591e1e8ed156&SetLanguage=en-CA Calgary Athlete 17 165 cm 56.5 kg Calgary Aquabelles Jenn Tregale and Courtenay Grant team member My goals for the games are to have fun and swim the best as a team and as an individual swimmer My personal best result in swimming would be from 2017 in Toronto when my team achived our goal of coming first at nationals. In 2017 I recieved most improved junior. my personal role model is my mom, because she is always pushing herself to do more even if it's for her coaching or if it's for her family. She is always working and improving on things she loves and really pushes me to do the same. I got involved in artistic swimming when I was four years old. My mom had been coaching and I had joined after I saw how much fun the girls were having. after a few weeks of trying it out, I asked my mom if I could continue during the regular season. Then she put me in my first club Atlantis Synchro in Halifax Nova Scotia. Where I continued my career until 2013 when I moved to calgary where I continue to train. <br/>", "Invalid input error. Function returned proper output, response = " + response
	
	def testRephrasing (self):
		response = chat ("is Kelsey Ayers participating")
		assert response == "Alberta Artistic Swimming Kelsey Ayers https://cg2019.gems.pro/Result/ShowPerson.aspx?Person_GUID=b18edb7a-a8e2-4e88-ba3e-591e1e8ed156&SetLanguage=en-CA Calgary Athlete 17 165 cm 56.5 kg Calgary Aquabelles Jenn Tregale and Courtenay Grant team member My goals for the games are to have fun and swim the best as a team and as an individual swimmer My personal best result in swimming would be from 2017 in Toronto when my team achived our goal of coming first at nationals. In 2017 I recieved most improved junior. my personal role model is my mom, because she is always pushing herself to do more even if it's for her coaching or if it's for her family. She is always working and improving on things she loves and really pushes me to do the same. I got involved in artistic swimming when I was four years old. My mom had been coaching and I had joined after I saw how much fun the girls were having. after a few weeks of trying it out, I asked my mom if I could continue during the regular season. Then she put me in my first club Atlantis Synchro in Halifax Nova Scotia. Where I continued my career until 2013 when I moved to calgary where I continue to train. <br/>", "Rephrase input error. Function did not return expected output, response = " + response
	
class TestSportInfo(unittest.TestCase):
		
	def testValidInput (self):
		response = chat ("what sport Kelsey Ayers play")
		assert response == "Kelsey Ayers participates in Artistic Swimming", "Rephrase input error. Function did not return expected output, response = " + response
	
	def testMultiple (self):
		response = chat ("what sport Aron Bargen play")
		assert response == "There are 2 player matching that name. <br/> Aron Bargen from Saskatchewan participates in Cross Country Skiing.<br/> Aron Bargen from Saskatchewan participates in Biathlon.<br/>", "Function did not return multple atheletes output, response = " + response
	
	def testDoesNotExist (self):
		response = chat ("what sport Kanye West play")
		assert response != "Kelsey Ayers participates in Artistic Swimming", "Doesn't exist error. Function returned a existing player response = " + response

class TestMedalCount(unittest.TestCase):
		
	def testOntario (self):
		response = chat ("How many medals does Ontario have?")
		assert response == "Ontario currently has 105 medals. 18 gold, 43 silver, 44 bronze", "Did not return expected output on ontario input, response = " + response
	
	def testInvalidProvince (self):
		response = chat ("How many medals does North Dakota have?")
		assert response == "Cannot find province or territory by that name", "Function returned a provinces medal count, response = " + response
	
	def testMisspelling (self):
		response = chat ("How many madels does Ontario have")
		assert response != "Ontario currently has 105 medals. 18 gold, 43 silver, 44 bronze", "function returned medal count. response = " + response
		
		
class TestEventTimes(unittest.TestCase):
	
	def testValidGameWithProvice (self):
		response = chat ("When is ontario's next basketball game")
		assert response == "Preliminary | Pool B - Game 5 - ON vs PE at 2022-08-8 on 05:30 PM in Niagara College - Welland Campus.<br> Preliminary | Pool A - Game 6 - NB vs ON at 2022-08-8 on 07:45 PM in Meridian Centre.<br> ", "Function 0 of the expected games. response = " + response
		
	def testValidGameWithoutProvince (self):
		response = chat ("When is the next basketball game")
		assert response == "Preliminary | Pool B - Game 1 - MB vs NT Manitoba on 2022-08-8 at 08:30 AM in Niagara College - Welland Campus.<br> Preliminary | Pool B - Game 1 - NS vs NT Northwest Territories on 2022-08-8 at 08:30 AM in Meridian Centre.<br> Preliminary | Pool C - Game 2 - BC vs NL British Columbia on 2022-08-8 at 10:45 AM in Meridian Centre.<br> Preliminary | Pool C - Game 2 - NL vs NS Newfoundland and Labrador on 2022-08-8 at 10:45 AM in Niagara College - Welland Campus.<br> Preliminary | Pool C - Game 3 - AB vs YT Alberta on 2022-08-8 at 01:00 PM in Meridian Centre.<br> Preliminary | Pool C - Game 3 - NB vs YT New Brunswick on 2022-08-8 at 01:00 PM in Niagara College - Welland Campus.<br> Preliminary | Pool A - Game 4 - QC vs SK Quebec on 2022-08-8 at 03:15 PM in Niagara College - Welland Campus.<br> Preliminary | Pool B - Game 5 - MB vs PE Manitoba on 2022-08-8 at 05:30 PM in Meridian Centre.<br> Preliminary | Pool B - Game 5 - ON vs PE Ontario on 2022-08-8 at 05:30 PM in Niagara College - Welland Campus.<br> Preliminary | Pool A - Game 6 - AB vs BC Alberta on 2022-08-8 at 07:45 PM in Niagara College - Welland Campus.<br> Preliminary | Pool A - Game 6 - NB vs ON New Brunswick on 2022-08-8 at 07:45 PM in Meridian Centre.<br> ", "Function did not return the expected basketball games. response = " + response	
	def testValidProvince (self):
		
		response = chat ("when is ontario's next game?")
		assert response == "Here are the upcoming games for Ontario<br>Preliminary | Pool A - Game 27 - NS vs ON Baseball on 2022-08-10 at 07:00 PM in Welland Baseball Stadium.<br> Preliminary | Pool A - Duel 1089 - AB vs ON Wrestling on 2022-08-10 at 08:30 AM in Canada Games Park.<br> Preliminary | Pool B - Duel 6100 - ON vs YT Wrestling on 2022-08-10 at 10:00 AM in Canada Games Park.<br> Preliminary | Pool A - Duel 1111 - ON vs SK Wrestling on 2022-08-10 at 12:30 PM in Canada Games Park.<br> Preliminary | Pool B - Duel 3122 - AB vs ON Wrestling on 2022-08-10 at 02:00 PM in Canada Games Park.<br> ", "Function did not return the expected games for ontario. response = " + response
		
	
	

	
if __name__ == "__main__":
	unittest.main()