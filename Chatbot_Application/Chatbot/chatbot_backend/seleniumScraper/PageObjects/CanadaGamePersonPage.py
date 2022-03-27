from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class CanadaGamesPersonPage:
    ExampleURL = 'https://cg2019.gems.pro/Result/ShowPerson.aspx?Person_GUID=15c71e8e-8fa1-4e29-b6b0-c0712b5655e3&SetLanguage=en-CA'

    def person_name():
        """
        person name ID locator.

        :return: tuple with By.ID as teh first item and ID as the second.
        :rtype: tuple
        """

        return (By.ID, "txtPersonNameFML")

    def person_contingent():
        """
        person contingent ID locator.

        :return: tuple with By.ID as the first item and ID as the second.
        :rtype: tuple
        """

        return (By.ID, "txtContingent")

    def person_hometown():
        """
        person hometown ID locator.

        :return: tuple with By.ID as the first item and ID as the second.
        :rtype: tuple
        """

        return (By.ID, "txtHomeTown")

    def person_type():
        """
        person type locator.

        :return: tuple with By.ID as the first item and ID as the second.
        :rtype: tuple
        """

        return(By.ID, "txtParticipantTypeName")

    def person_sport():
        """
        person sport locator.

        :return: tuple with By.ID as the first item and ID as the second.
        :rtype: tuple

        """
        return (By.ID, "txtSportName")

    def person_age():
        """
        person age locator.

        :return: tuple with By.ID as the first item and ID as the second.
        :rtype: tuple
        """

        return(By.ID, "txtAge")

    def person_height():
        """
        person height locator.

        :return: tuple with By.ID as the first item and ID as the second.
        :rtype: tuple
        """

        return(By.ID, "txtHeight")

    def person_weight():
        """
        person weight locator.

        :return: tuple with By.ID as the first item and ID as the second.
        :rtype: tuple
        """

        return(By.ID, "txtWeight")

    def club_or_team_affiliation():
        """
        person weight locator.

        :return: tuple with By.ID as the first item and ID as the second.
        :rtype: tuple
        """

        return (By.ID, "txtSchool")

    def name_of_coach():
        """
        person Name of Coach locator.

        :return: tuple with By.ID as the first item and ID as the second.
        :rtype: tuple
        """
        return(By.ID, "txtCoach")

    def person_position():
        """
        position of person.

        :return: tuple with By.ID as the first item and ID as the second.
        :rtype: tuple
        """
        return(By.ID, "txtTeamPosition")


    def my_goals_for_the_games():
        """
        person 'my goals for the games' locator.

        :return: tuple with By.ID as the first item and ID as the second.
        :rtype: tuple
        """
        return(By.ID, "txtGamesGoal")

    def my_personal_best_result_in_my_event():
        """
        person 'my personal best result in my event' locator.

        :return: tuple with By.ID as the first item and ID as the second.
        :rtype: tuple
        """

        return(By.ID, "txtBestResult")

    def awards_or_major_accomplishments_that_I_have_received():
        """
        person 'awards or major accomplishments that I have received' locator.

        :return: tuple with By.ID as the first item and ID as the second.
        :rtype: tuple
        """

        return(By.ID, "txtAwards")
    
    def my_personal_role_model():
        """
        person 'My personal role model' locator.

        :return: tuple with By.ID as the first item and ID as the second.
        :rtype: tuple
        """

        return(By.ID, "txtRoleModel")

    def other_information_that_could_be_of_interest_to_the_media():
        """
        person 'Other information that could be of interest to the media' locator.

        :return: tuple with By.ID as the first item and ID as the second.
        :rtype: tuple
        """

        return(By.ID, "txtMediaInfo")




        
