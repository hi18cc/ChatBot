from selenium.webdriver.common.by import By


class CanadaGamesMedalPage:
    URL = 'https://cg2019.gems.pro/Result/MedalList.aspx?'

    def gold_medal_count_by_contingent(contingentAbbrev):
        """
        Element for the table cell containing the number of gold medals for the provided contingent.

        :return: tuple with By.ID as the first element and ID as the second element.
        :rtype: tuple
        """

        return (By.ID, f"ctl00_ContentPlaceHolder1_tdPlacing_{contingentAbbrev}1")

    def silver_medal_count_by_contingent(contingentAbbrev):
        """
        Element for the table cell containing the number of silver medals for the provided contingent.

        :return: tuple with By.ID as the first element and ID as the second element.
        :rtype: tuple
        """

        return (By.ID, f"ctl00_ContentPlaceHolder1_tdPlacing_{contingentAbbrev}2")

    def bronze_medal_count_by_contingent(contingentAbbrev):
        """
        Element for the table cell containing the number of bronze medals for the provided contingent.

        :return: tuple with By.ID as the first element and ID as the second element.
        :rtype: tuple
        """

        return (By.ID, f"ctl00_ContentPlaceHolder1_tdPlacing_{contingentAbbrev}3")

    def total_medal_count_by_contingent(contingentAbbrev):
        """
        Element for the table cell containing the number of silver medals for the provided contingent.

        :return: tuple with By.ID as the first element and ID as the second element.
        :rtype: tuple
        """

        return (By.ID, f"ctl00_ContentPlaceHolder1_tdSum_{contingentAbbrev}")
    