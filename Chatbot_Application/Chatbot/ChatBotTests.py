import unittest
import json
from bot import chat

class TestAskingForTickets(unittest.TestCase):
	
	def testTicketsNormal(self):
		response = chat ("Where can I buy tickets");
		assert response == "Tickets and ticket information can be obtained here https://niagara2022games.ca/tickets/", "Does not return the link"
		
	def testTicketsPhraseMisspelled(self):
		response = chat ("Whe ca I bye tickets");
		assert response == "Tickets and ticket information can be obtained here https://niagara2022games.ca/tickets/", "Does not return the link due to misspelling everything in the phrase"
		
	def testTicketsMisspelled(self):
		response = chat ("Whe ca I bye tick");
		assert response == "Tickets and ticket information can be obtained here https://niagara2022games.ca/tickets/", "Does not return the link due to misspelling of tickets"
		
		
if __name__ == "__main__":
	unittest.main()