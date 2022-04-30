using System;
using System.Collections.Generic;
using System.Text;
using System.Linq;
using System.Threading.Tasks;
using NUnit.Framework;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium.Support;
using TestCases.Pages;
using WebDriverManager.DriverConfigs.Impl;
using OpenQA.Selenium.Support.UI;
using SeleniumExtras.WaitHelpers;

namespace TestCases
{
    class Test
    {

        
        ChromeDriver driver;
        string input = "";

        [SetUp]
        public void startBrowser()
        {
            new WebDriverManager.DriverManager().SetUpDriver(new ChromeConfig());
            ChromeOptions options = new ChromeOptions();
            options.AddArgument("headless");
            driver = new ChromeDriver(options);
        }

        [Test, Description("Tests that the front end has all the elements with the appropriate texts")]
        public void FrontEndDisplayed()
        {
            
            driver.Url = "http://127.0.0.1:5500/Chatbot_Application/Chatbot/templates/html/textbox.html";
            ChatbotPage chatbotPage = new ChatbotPage(driver);

            Assert.IsTrue(chatbotPage.SendButton.Text == "Send");
            Assert.IsTrue(chatbotPage.ClearButton.Displayed);
            Assert.IsTrue(chatbotPage.Input.Displayed);
            Assert.IsTrue(chatbotPage.Header.Text == "Chat Bot");
            Assert.IsTrue(chatbotPage.ChatLogButton.Displayed);
            Assert.IsTrue(chatbotPage.BackButton.Displayed);
            Assert.IsTrue(chatbotPage.InfoButton.Displayed);

            Assert.IsTrue(chatbotPage.DonateButton.Text == "Donate");
            Assert.IsTrue(chatbotPage.TicketsButton.Text == "Tickets");

            Assert.IsTrue(chatbotPage.SupportLink.Displayed);
        }


        [Test, Description("Checks that the suggestion questions are matching")]
        public void CheckIntroMessages()
        {
            driver.Url = "http://127.0.0.1:5500/Chatbot_Application/Chatbot/templates/html/textbox.html";
            ChatbotPage chatbotPage = new ChatbotPage(driver);
            string intromessage = "Welcome to the Chatbot, ask me questions and I'll try to answer them, here are some suggestion questions:";
            string firstSuggestion = "Information about Canada Summer Games...";
            string secondSuggestion = "Information about Niagara...";
            string thirdSuggestion = "Information about Sports...";
            string fourthSuggestion = "Information about Players...";

            
            Assert.IsTrue(chatbotPage.LastBotMessage.Text == intromessage);
            var quickMessages = chatbotPage.QuickSuggestMessages;
            Assert.AreEqual(4, quickMessages.Count());

            
            Assert.AreEqual(firstSuggestion, quickMessages[3].Text);
            Assert.AreEqual(secondSuggestion, quickMessages[2].Text);
            Assert.AreEqual(thirdSuggestion, quickMessages[1].Text);
            Assert.AreEqual(fourthSuggestion, quickMessages[0].Text);


        }

        [Test, Description("Tests questions for asking about Canada Games website")]
        ///
        public void Question01CanadaGamesWebsite()
        {

            driver.Url = "http://127.0.0.1:5500/Chatbot_Application/Chatbot/templates/html/textbox.html";
            ChatbotPage chatbotPage = new ChatbotPage(driver);

            string[] questions = { "What is the Canada Game website?", "What is the Canada Summer Games website?", "Is there a Canada Game webiste?", "Is there a Canada Summer Games webiste?", 
                "How can I get to the Canada Game website?", "What is the link to the Canada Game website", "give me the link to canada summer games", "canada game website", "website",
                "what is the website to canada games", "what website", "what canada game website", "link", "I want the website", "want website", "want link",
                "Where can I find Canadian games online", "Where can I find games from Canada online?", "where can I find the website to get more information on canada summer games", 
                "I need more information on canada summer games", "I need more info on canada summer games", "i need more info about canada summer games", "i need more info" };
            Dictionary<string, int> responses = new Dictionary<string, int>();
            
            string[] response = { "You can get to the Canada Game website by using this link: https://niagara2022games.ca",
                "The link to the Canada Game website is https://niagara2022games.ca" };
            responses.Add(response[0], 1);
            responses.Add(response[1], 1);

            
            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(4));
            for(int i=0; i<questions.Length; i++)
            {
                chatbotPage.SendMessage(questions[i]);
                wait.Until(ExpectedConditions.InvisibilityOfElementLocated(By.CssSelector(".spinner-border")));
                input = questions[i];
                Assert.IsTrue(responses.ContainsKey(chatbotPage.LastBotMessage.Text));
            }
            input = "";
        }

        [Test,Description("Tests Question 2 which asks about transportation")]
        public void Question02CanadaGamesTransit()
        {

            driver.Url = "http://127.0.0.1:5500/Chatbot_Application/Chatbot/templates/html/textbox.html";
            ChatbotPage chatbotPage = new ChatbotPage(driver);


            string[] questions = { "What transportation options are available?", "Are there transportation options avaliable?", "Give me some transportation options", 
                "What modes of transportation could I use", "What are some transporation options?", "Give me transportation options", "What transportation options are there for Canada Summer Games",
                "I would like transporation options", "transporation options", "transportation", "cars", "vehicles", "trains", "How can I get around?", "How can you get around?", "Is there a range of transportation options?", 
                "Does canada summer games provide transport" };
            string response = "Niagara Region Transit information is available here: https://www.niagararegion.ca/transit/";

            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(4));
            for (int i = 0; i < questions.Length; i++)
            {
                chatbotPage.SendMessage(questions[i]);
                wait.Until(ExpectedConditions.InvisibilityOfElementLocated(By.CssSelector(".spinner-border")));
                input = questions[i];
                Assert.AreEqual(response, chatbotPage.LastBotMessage.Text);
            }
            input = "";
        }


        [Test, Description("Tests Question 3 which asks about Transit")]
        public void Question03CanadaGamesBusSystem()
        {

            driver.Url = "http://127.0.0.1:5500/Chatbot_Application/Chatbot/templates/html/textbox.html";
            ChatbotPage chatbotPage = new ChatbotPage(driver);


            string[] questions = { "Is there an app for the buses?", "Where can I find the app for buses?", "Give me the app for buses", "Is there an iOS app for buses?", 
                "Is there an android app for buses?", "Are there buses to Canada Games?", "app for buses", "buesses", "bus", "Buses have apps, do they not?", 
                "Are there any apps for the buses?", "Has an app been developed for the buses?", "The buses have an app, right?", "How is the transit system in niagara" };

            string response = "The Niagara Reigon Transit app for Android is avaiable here https://play.google.com/store/apps/details?id=com.thetransitapp.droid and a version for iOS is available here https://apps.apple.com/ca/app/transit-bus-train-times/id498151501";

            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(4));
            for (int i = 0; i < questions.Length; i++)
            {
                chatbotPage.SendMessage(questions[i]);
                wait.Until(ExpectedConditions.InvisibilityOfElementLocated(By.CssSelector(".spinner-border")));
                input = questions[i];
                Assert.AreEqual(response, chatbotPage.LastBotMessage.Text);
            }
            input = "";
        }

        [Test, Description("Tests Question 4 What can you do in the Niagara region?")]
        public void Question04NiagaraActivities()
        {

            driver.Url = "http://127.0.0.1:5500/Chatbot_Application/Chatbot/templates/html/textbox.html";
            ChatbotPage chatbotPage = new ChatbotPage(driver);


            string[] questions = { "What can you do in the Niagara region?", "Is there anything to do in the Niagara region?", "What are some attractions of the Niagra Region?", 
                "Is there anything to do in the Niagara Region?", "niagara", "Niagara offers a variety of things to do.", "Can you find fun things to do in Niagara?", 
                "In Niagara, what are your options?", "The Niagara region has a number of things to offer.", "In Niagara, what is there to do?", "How can you enjoy Niagara?", 
                "what's there to do here", "anything fun to do here", "local activites in the area", "Events outside of canada summer games" };

            string response = "The Niagara Falls Tourism website provided here https://www.niagarafallstourism.com/niagara-region/ has information about what you can see and do in the region";

            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(4));
            for (int i = 0; i < questions.Length; i++)
            {
                chatbotPage.SendMessage(questions[i]);
                wait.Until(ExpectedConditions.InvisibilityOfElementLocated(By.CssSelector(".spinner-border")));
                input = questions[i];
                Assert.AreEqual(response, chatbotPage.LastBotMessage.Text);
            }
            input = "";
        }

        [Test, Description("Tests Question 5 Where can you stay in the Niagara Region?")]
        public void Question05NiagaraAccomodations()
        {

            driver.Url = "http://127.0.0.1:5500/Chatbot_Application/Chatbot/templates/html/textbox.html";
            ChatbotPage chatbotPage = new ChatbotPage(driver);


            string[] questions = { "Where can you stay in the Niagara region?", "I need a place to stay", "What are some hotels I can stay in?", "hotels", "motels", "inns", "inn",
                "bnbs", "Give me some lodging options?", "I need some accommodations I can stay in", "Give me some accommodations", "What are some accomodations I can stay in?", 
                "lodging", "In the Niagara region, where can you stay?", "What hotels are available in the Niagara region?", "How do you find a place to stay in Niagara?", 
                "Is Niagara region a good place to stay?", "Niagara region accommodations", "accommodations", "is there an AirBnB here", "bnb", "places to sleep", 
                "hotels close to me", "hotels close to the games", "hotels near canada summer games", "available accomodations", "available accommodations", 
                "hotels to sleep at night", "places to sleep at night", "I need a place to stay", "inns to place at night", "BnBs to place at night", "I don't have a place to stay", 
                "recommend me some good hotels", "recommendations on hotels" };

            string response = "The Niagara Falls Tourism website provided here https://www.niagarafallstourism.com/niagara-region/ has information about accommodations in the Niagara Region";

            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(4));
            for (int i = 0; i < questions.Length; i++)
            {
                chatbotPage.SendMessage(questions[i]);
                wait.Until(ExpectedConditions.InvisibilityOfElementLocated(By.CssSelector(".spinner-border")));
                input = questions[i];
                Assert.AreEqual(response, chatbotPage.LastBotMessage.Text);
            }
            input = "";
        }

        [Test, Description("Tests Question 6 Covid restrictions in Niagara?")]
        public void Question06Covidrestrictions()
        {

            driver.Url = "http://127.0.0.1:5500/Chatbot_Application/Chatbot/templates/html/textbox.html";
            ChatbotPage chatbotPage = new ChatbotPage(driver);


            string[] questions = { "What are the COVID-19 restrictions like in Niagara?", "Are there COVID-19 restrictions in Niagara", "How strict are the COVID-19 restrictions in the Niagara Region?", 
                "covid-19", "restrictions", "guidelines", "masks", "do i need to wear a mask", "wear mask", "vaccine", "booster shot", "vaccine passport", "do i need a vaccine passport", 
                "do i need to be vaccinated", "vaccinated", "sick", "flu", "cold", "In Niagara, what restrictions apply to COVID-19?", "Is COVID-19 restricted in Niagara?", "In Niagara, what is the COVID-19 restriction?", 
                "The COVID-19 regulations in Niagara are what?", "Covid", "Coivd 19", "Do I need a mask", "mask", "Do I need to wear a mask", "Do I have to be 6 feet away", "social distancing", "Do I need to social distance" };
            string response = "The Niagara region COVID-19 information can be found here https://www.niagararegion.ca/health/covid-19/";

            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(4));
            for (int i = 0; i < questions.Length; i++)
            {
                chatbotPage.SendMessage(questions[i]);
                wait.Until(ExpectedConditions.InvisibilityOfElementLocated(By.CssSelector(".spinner-border")));
                input = questions[i];
                Assert.AreEqual(response, chatbotPage.LastBotMessage.Text);
            }
            input = "";
        }

        [Test, Description("Tests Question 7 How long until Canada Games Starts?")]
        public void Question07StartDate()
        {

            driver.Url = "http://127.0.0.1:5500/Chatbot_Application/Chatbot/templates/html/textbox.html";
            ChatbotPage chatbotPage = new ChatbotPage(driver);


            string[] questions = { "How long until Canada Games starts", "When does Canada Games begin", "When does Canada Summer Games begin", "Has Canada Games already started?", 
                "What's the starting time for Canada Games", "When does Canada Games start", "When is Canada Games starting", "start", "begin", "commence", "when", 
                "When are the Canada Games?", "The start of Canada Games is how long away", "How long until the Canada Games begin?", "In how long will the Canada Games begin?", 
                "How long before the Canada Games start?", "when do the games start", "start", "what time is the event going to be", "what time is the even going to be" };

            string response = "Saturday, August 6, 2022";

            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(4));
            for (int i = 0; i < questions.Length; i++)
            {
                chatbotPage.SendMessage(questions[i]);
                wait.Until(ExpectedConditions.InvisibilityOfElementLocated(By.CssSelector(".spinner-border")));
                input = questions[i];
                Assert.AreEqual(response, chatbotPage.LastBotMessage.Text);
            }
            input = "";
        }

        [Test, Description("Tests Question 8 Canada Games News")]
        public void Question08GamesNews()
        {

            driver.Url = "http://127.0.0.1:5500/Chatbot_Application/Chatbot/templates/html/textbox.html";
            ChatbotPage chatbotPage = new ChatbotPage(driver);


            string[] questions = { "What's new with the Canada Games?", "Has anything new happened in Canada Games?", "Anything new happen with Canada Games?", "Is there any breaking news with Canada Games?", 
                "news", "breaking news", "new", "Updates on the Canada Games", "Updates on the Canada Summer Games", "New developments in the Canada Games", "New developments", "The Canada Games have undergone several changes since last year", 
                "Introducing the Canada Games", "anything new happening", "the lastest from canada games" };

            string response = "The Canada Games news is available here https://niagara2022games.ca/news/";

            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(4));
            for (int i = 0; i < questions.Length; i++)
            {
                chatbotPage.SendMessage(questions[i]);
                wait.Until(ExpectedConditions.InvisibilityOfElementLocated(By.CssSelector(".spinner-border")));
                input = questions[i];
                Assert.AreEqual(response, chatbotPage.LastBotMessage.Text);
            }
            input = "";
        }

        [Test, Description("Tests Question 9 Where is Canada Games being hosted this year?")]
        public void Question09CanadaGamesHosting()
        {

            driver.Url = "http://127.0.0.1:5500/Chatbot_Application/Chatbot/templates/html/textbox.html";
            ChatbotPage chatbotPage = new ChatbotPage(driver);


            string[] questions = { "Where is the Canada Games", "Where is the Canada Games", "where is the next game", "Where is Canada Games being hosted", 
                "What are the directions to Canada Games?", "Give me directions to Canada games", "How do I get to Canada games?", "get to canada summer games", "where", "directions", "directions to", 
                "The Canada Games are held in Canada", "The Canada Games will take place in Vancouver", "How can I find the Canada Games", "What is the venue for the Canada Games?", "where can I watch ontario play", "where can I watch", 
                "where can I watch  British Columbia", "where can I watch prince edward island play", "where will it be" };
            
            string response = "The Canada Games events will be taking place in various locations across the Niagara region, locations for specific sports can be found here https://niagara2022games.ca/sports/";

            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(4));
            for (int i = 0; i < questions.Length; i++)
            {
                chatbotPage.SendMessage(questions[i]);
                wait.Until(ExpectedConditions.InvisibilityOfElementLocated(By.CssSelector(".spinner-border")));
                input = questions[i];
                Assert.AreEqual(response, chatbotPage.LastBotMessage.Text);
            }
            input = "";
        }

        [Test,Description("Tests Question 10 Tell me about a Player, full name ")]
        public void Question10PlayerInfoFullName()
        {

            driver.Url = "http://127.0.0.1:5500/Chatbot_Application/Chatbot/templates/html/textbox.html";
            ChatbotPage chatbotPage = new ChatbotPage(driver);
            string player = "Evelyn Beaton";

            string[] questions = { "Tell me about", "I want to know more about", "Give me information on", "know more about", "more about", "about", "information on", "what do you know about", "do you know", "you know", "know", "info on", "Please tell me about", "Let me know about", "Can you tell me about", "who is", "" };
            string response = "Contingent: AlbertaSport Name: JudoPerson Name: Evelyn BeatonHometown: " +
                "Lethbridge, ABType: AthleteAge: 14Height: 158cmWeight: 44kgClub: Lethbridge Judo ClubCoach: " +
                "Russel Gallant, Trevor McAlpine, Ewan BeatonPosition: 44kgGoals for Games: Podium in 44kg and podium in team " +
                "eventPersonal Best Result: National Championships because it is the National Championships. I just won the U18 Quebec " +
                "Open and beat a tough girl from the USA during the competition. In November I won the U16 Ontario Open and beat a tough " +
                "girl from Brazil in the final that I had lost to the week before, so beating her was really excitingAward: 2018 " +
                "Female Proficiency Award Lethbridge Judo ClubOther Info: My dad went to the olympics for Judo and my mom did Judo " +
                "to so it came from both of my parents. I was always around judo when I was younger and by the age of 6 or 7 I started " +
                "Judo.Get More Info Here";

            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(4));
            for (int i = 0; i < questions.Length; i++)
            {
                chatbotPage.SendMessage(questions[i] + " " +player);
                wait.Until(ExpectedConditions.InvisibilityOfElementLocated(By.CssSelector(".spinner-border")));
                input = questions[i];
                Assert.AreEqual(response, chatbotPage.LastBotMessage.GetAttribute("textContent"));
            }
            input = "";
        }

        [Test, Description("Tests Question 10 Tell me about a Player, first name ")]
        public void Question10PlayerInfoFirstName()
        {

            driver.Url = "http://127.0.0.1:5500/Chatbot_Application/Chatbot/templates/html/textbox.html";
            ChatbotPage chatbotPage = new ChatbotPage(driver);
            string player = "Evelyn";
            input = player;
            string[] questions = { "Tell me about", "I want to know more about", "Give me information on", "know more about", "more about", "about", "information on", "what do you know about", 
                "do you know", "you know", "know", "info on", "Please tell me about", "Let me know about", "Can you tell me about", "who is", "" };

            string response = "Contingent: AlbertaSport Name: JudoPerson Name: Evelyn BeatonHometown: " +
                "Lethbridge, ABType: AthleteAge: 14Height: 158cmWeight: 44kgClub: Lethbridge Judo ClubCoach: " +
                "Russel Gallant, Trevor McAlpine, Ewan BeatonPosition: 44kgGoals for Games: Podium in 44kg and podium in team " +
                "eventPersonal Best Result: National Championships because it is the National Championships. I just won the U18 Quebec " +
                "Open and beat a tough girl from the USA during the competition. In November I won the U16 Ontario Open and beat a tough " +
                "girl from Brazil in the final that I had lost to the week before, so beating her was really excitingAward: 2018 " +
                "Female Proficiency Award Lethbridge Judo ClubOther Info: My dad went to the olympics for Judo and my mom did Judo " +
                "to so it came from both of my parents. I was always around judo when I was younger and by the age of 6 or 7 I started " +
                "Judo.Get More Info HereContingent: Nova ScotiaSport Name: RingettePerson Name: " +
                "Elizabeth Evelyn C WelshHometown: BedfordType: AthleteAge: 20Height: 168Coach: Tracy " +
                "TullochPosition: GoalieOther Info: I went to a neurologist at six years old for chronic headaches " +
                "and while treating me he told me about ringette and how it was the right sport for \"smart girls\"Get " +
                "More Info Here";


            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(4));
            
            for (int i = 0; i < questions.Length; i++)
            {
                chatbotPage.SendMessage(questions[i] + " " + player);

                wait.Until(ExpectedConditions.InvisibilityOfElementLocated(By.CssSelector(".spinner-border")));
                input = questions[i];
                Assert.AreEqual(response, chatbotPage.LastBotMessage.GetAttribute("textContent"));
            }
            input = "";
        }

        [Test, Description("Tests Question 10 Tell me about a Player, Last name.")]
        public void Question10PlayerInfoLastName()
        {

            driver.Url = "http://127.0.0.1:5500/Chatbot_Application/Chatbot/templates/html/textbox.html";
            ChatbotPage chatbotPage = new ChatbotPage(driver);
            string player = "Beaton";

            string[] questions = { "Tell me about", "I want to know more about", "Give me information on", "know more about", "more about", "about", "information on", "what do you know about", "do you know", "you know", "know", "info on", "Please tell me about", "Let me know about", "Can you tell me about", "who is", "" };
            string response = "Contingent: AlbertaSport Name: JudoPerson Name: Evelyn BeatonHometown: " +
                "Lethbridge, ABType: AthleteAge: 14Height: 158cmWeight: 44kgClub: Lethbridge Judo ClubCoach: " +
                "Russel Gallant, Trevor McAlpine, Ewan BeatonPosition: 44kgGoals for Games: Podium in 44kg and podium in team " +
                "eventPersonal Best Result: National Championships because it is the National Championships. I just won the U18 Quebec " +
                "Open and beat a tough girl from the USA during the competition. In November I won the U16 Ontario Open and beat a tough " +
                "girl from Brazil in the final that I had lost to the week before, so beating her was really excitingAward: 2018 " +
                "Female Proficiency Award Lethbridge Judo ClubOther Info: My dad went to the olympics for Judo and my mom did Judo " +
                "to so it came from both of my parents. I was always around judo when I was younger and by the age of 6 or 7 I started " +
                "Judo.Get More Info Here";

            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(4));
            for (int i = 0; i < questions.Length; i++)
            {
                chatbotPage.SendMessage(questions[i] + " " + player);
                wait.Until(ExpectedConditions.InvisibilityOfElementLocated(By.CssSelector(".spinner-border")));
                input = questions[i];
                Assert.AreEqual(response, chatbotPage.LastBotMessage.GetAttribute("textContent"));
            }
            input = "";
        }

        [Test, Description("Tests Question 11 What sport did person play? Full Name.")]
        public void Question11SportInfoFullName()
        {

            driver.Url = "http://127.0.0.1:5500/Chatbot_Application/Chatbot/templates/html/textbox.html";
            ChatbotPage chatbotPage = new ChatbotPage(driver);
            string player = "Evelyn Beaton";
            

            string[] questions = { "What sport did", "what sport", "sport did", "what sport did play", "what sport does play" };
            string response = "Evelyn Beaton participates in Judo";

            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(4));
            for (int i = 0; i < questions.Length; i++)
            {
                chatbotPage.SendMessage(questions[i] + " " + player);
                wait.Until(ExpectedConditions.InvisibilityOfElementLocated(By.CssSelector(".spinner-border")));
                input = questions[i];
                Assert.AreEqual(response, chatbotPage.LastBotMessage.Text);

            }

            input = "";
        }

        [Test, Description("Tests Question 11 What sport did person play? First Name.")]
        public void Question11SportInfoFirstName()
        {

            driver.Url = "http://127.0.0.1:5500/Chatbot_Application/Chatbot/templates/html/textbox.html";
            ChatbotPage chatbotPage = new ChatbotPage(driver);
            string player = "Evelyn";

            string[] questions = { "What sport did", "What sport does", "what sport", "sport did", "sport does", "sport", "what sport did play", "what sport does play" };
            string response = "There are 2 player matching that name.\r\nEvelyn Beaton from Alberta participates in Judo.\r\nElizabeth Evelyn C Welsh from Nova Scotia participates in Ringette.";

            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(4));
            for (int i = 0; i < questions.Length; i++)
            {
                chatbotPage.SendMessage(questions[i] + " " + player);
                wait.Until(ExpectedConditions.InvisibilityOfElementLocated(By.CssSelector(".spinner-border")));
                input = questions[i];
                Assert.AreEqual(response, chatbotPage.LastBotMessage.Text);
            }
            input = "";
        }

        [Test, Description("Tests Question 11 What sport did person play? Last Name.")]
        public void Question11SportInfoLastName()
        {

            driver.Url = "http://127.0.0.1:5500/Chatbot_Application/Chatbot/templates/html/textbox.html";
            ChatbotPage chatbotPage = new ChatbotPage(driver);
            string player = "Beaton";

            string[] questions = { "What sport did", "What sport does", "what sport", "sport did", "sport does", "what sport did play", "what sport does play" };
            string response = "Evelyn Beaton participates in Judo";

            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(4));
            for (int i = 0; i < questions.Length; i++)
            {
                chatbotPage.SendMessage(questions[i] + " " + player);
                wait.Until(ExpectedConditions.InvisibilityOfElementLocated(By.CssSelector(".spinner-border")));
                input = questions[i];
                Assert.AreEqual(response, chatbotPage.LastBotMessage.Text);
            }
            input = "";
        }

        [Test, Description("Tests Question 14 Where can I buy tickets?")]
        public void Question12MedalsInformation()
        {

            driver.Url = "http://127.0.0.1:5500/Chatbot_Application/Chatbot/templates/html/textbox.html";
            ChatbotPage chatbotPage = new ChatbotPage(driver);
            // Subbing in Ontario into the questions

            string[] questions = { "How many medals does Ontario", "What's the scoring for Ontario", "What are the stats for Ontario", "How many silver medals does Ontario have?", "How many bronze medals does Ontario have", "How many gold medals does Ontario have", "Ontario medals", "Ontario silver", "Ontario bronze", "Ontario gold", "Ontario silver medals", "Ontario gold medals", "Ontario bronze medals", "How many silver medals does ontario have?", "How many bronze medals does ontario have", "How many gold medals does ontario have", "How many silver medals does Ontario have?", "How many bronze medals does Ontario have", "How many gold medals does Ontario have", "How many medals does Ontario have", "How many medals does Ontario have", "How many medals does Ontario have", "What is the number of medals of Ontario", "How many medals has Ontario won", "How many medals has ontario earned", "What number of medals does Ontario have", "does Ontario have any medals", "does Ontario have any medals" };
            Dictionary<string, int> responses = new Dictionary<string, int>();

            responses.Add("Ontario currently has 18 gold medals", 1);
            responses.Add("Ontario currently has 43 silver medals", 1);
            responses.Add("Ontario currently has 44 bronze medals", 1);
            responses.Add("Ontario currently has 105 medals. 18 gold, 43 silver, 44 bronze",1);


            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(4));
            for (int i = 0; i < questions.Length; i++)
            {
                chatbotPage.SendMessage(questions[i]);
                wait.Until(ExpectedConditions.InvisibilityOfElementLocated(By.CssSelector(".spinner-border")));
                input = questions[i];
                Assert.IsTrue(responses.ContainsKey( chatbotPage.LastBotMessage.Text));

            }
            input = "";
        }


        [Test, Description("Tests Question 14 Where can I buy tickets?")]
        public void Question14TicketsInfo()
        {

            driver.Url = "http://127.0.0.1:5500/Chatbot_Application/Chatbot/templates/html/textbox.html";
            ChatbotPage chatbotPage = new ChatbotPage(driver);
            // Subbing in Ontario into the questions

            string[] questions = { "Where can I buy tickets?", "I want to buy a ticket?", "How can I purchase a ticket?", "How much is a ticket?", "How much are tickets?", "buy", "tickets", "bye tickets", "i want to bye tickets", "want buy tickets", "want bye tickets", "tickets bye", "where can i get tickets", "get tickets", "Ticket purchasing information" };
            string response = "Tickets and ticket information can be obtained here https://niagara2022games.ca/tickets/" ;

            WebDriverWait wait = new WebDriverWait(driver, TimeSpan.FromSeconds(4));
            for (int i = 0; i < questions.Length; i++)
            {
                chatbotPage.SendMessage(questions[i]);
                wait.Until(ExpectedConditions.InvisibilityOfElementLocated(By.CssSelector(".spinner-border")));
                input = questions[i];
                Assert.AreEqual(response, chatbotPage.LastBotMessage.Text);
            }
            input = "";
;        }

        [TearDown]
            public void closeBrowser()
        {
            if (input != "")
            {
                Console.WriteLine(input);
            }
            
            driver.Close();
        }

    }
}
