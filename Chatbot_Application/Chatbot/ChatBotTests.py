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
  
		
class TestAksingHotels(unittest.TestCase):
	
	def testCorrectSpelling (self):
		response = chat ("What are the COVID-19 restrictions like in Niagara?")
		assert response == "The Niagara region COVID-19 information can be found here https://www.niagararegion.ca/health/covid-19/default.aspx?topic=1", "Correct input error. Function did not return expected output, response = " + response
	
	def testAbbriviation (self):
		response = chat ("Covid-19")
		assert response == "The Niagara region COVID-19 information can be found here https://www.niagararegion.ca/health/covid-19/default.aspx?topic=1", "Abbriviation input error. Function did not return expected output, response = " + response
	
	def testRandomInput (self):
		response = chat ("i'm sick")
		assert response != "The Niagara region COVID-19 information can be found here https://www.niagararegion.ca/health/covid-19/default.aspx?topic=1", "Random input error. Function returned function output, response = " + response
	
	
if __name__ == "__main__":
	unittest.main()