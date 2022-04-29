using System;
using System.Collections.Generic;
using System.Text;
using OpenQA.Selenium.Chrome;
using OpenQA.Selenium;
using SeleniumExtras.PageObjects;

namespace TestCases.Pages
{
    class ChatbotPage
    {
        private ChromeDriver driver;
        public ChatbotPage(ChromeDriver driver)
        {
            this.driver = driver;
        }
        #region Elements
        public IWebElement SendButton => driver.FindElement(By.CssSelector(".send"));
        public IWebElement ClearButton => driver.FindElement(By.CssSelector(".clear"));
        public IWebElement Input => driver.FindElement(By.Id("msg"));
        public IWebElement Header => driver.FindElement(By.CssSelector("h4"));
        public IWebElement ChatLogButton => driver.FindElement(By.CssSelector(".bi-chat-left-text"));
        public IWebElement BackButton => driver.FindElement(By.CssSelector(".bi-arrow-return-left"));
        public IWebElement InfoButton => driver.FindElement(By.CssSelector(".bi-info-lg"));
        public IWebElement DonateButton => driver.FindElement(By.CssSelector(".home-link06"));
        public IWebElement TicketsButton => driver.FindElement(By.CssSelector(".home-text03"));
        public IWebElement SupportLink => driver.FindElement(By.CssSelector(".home-text01 > span"));
        public IWebElement Spinner => driver.FindElement(By.CssSelector(".spinner-border"));
        #endregion

        #region Messages 

        public IWebElement LastBotMessage => driver.FindElement(By.CssSelector(".messages.visitor")); //This will be the last gray message.

        public System.Collections.ObjectModel.ReadOnlyCollection<IWebElement> QuickSuggestMessages => driver.FindElements(By.CssSelector(".messages.quick-suggest"));

        
        #endregion
        
        /// <summary>
        /// This inputs text in the textbox and clicks send, so the chatbot can process the message.
        /// </summary>
        /// <param name="input">The string to be sent to the chatbot.</param>
        public void SendMessage(string input)
        {
            
            Input.SendKeys(input);
            SendButton.Click();
        }
       

    }
}
