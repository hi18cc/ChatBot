import sqlite3
from sqlite3 import Error

class SQLMethods:
    def create_connection(db_file):
        """ create a database connection to the SQLite database
            specified by db_file
        :param db_file: database file
        :return: Connection object or None
        """

        conn = None

        try:
            conn = sqlite3.connect(db_file)
        except Error as e:
            print(e)

        print("connection created")

        return conn

 
    def insert_games(conn, game):
        """
        insert game into the games table
        :param Connect conn: Connected database file.
        :param games:
        :return: game id
        """

        sql = ''' INSERT OR IGNORE INTO Games(GameName, SportName, Location, Event, GameDate, GameTime) VALUES(?,?,?,?,?,?)'''

        cur = conn.cursor()
        cur.execute(sql, game)
        conn.commit()
        #print("commited Games")
        return cur.lastrowid

    def insert_sports(conn, sport):
        """
        insert sport into the sports table
        :param Connect conn: Connected database file.
        :param sport:
        :return: sport id
        """

        sql = ''' INSERT OR IGNORE INTO sports(SportName) VALUES(?)'''

        cur = conn.cursor()
        cur.execute(sql, sport)
        conn.commit()


        return cur.lastrowid

    def insert_locations(conn, location):
        """
        insert location into the locations table
        :param Connect conn: Connected database file.
        :param Tuple location: Tuple with the location name. (location name,)
        :return: location id
        """

        sql = ''' INSERT OR IGNORE INTO locations(location) VALUES (?)'''

        cur = conn.cursor()
        cur.execute(sql, location)
        conn.commit()

        #print("commited locations")
        return cur.lastrowid

    def insert_sportLocations(conn, sportLocation):
        """
        insert location into the locations table
        :param Connect conn: Connected database file.
        :param Tuple sportLocation: The tuple containing (sportName, Location Name).
        :return: location id
        """

        sql = ''' INSERT OR IGNORE INTO sportLocations(SportName, Location) VALUES (?, ?)'''

        cur = conn.cursor()
        cur.execute(sql, sportLocation)
        conn.commit()

        #print("commited sportLocations")
        return cur.lastrowid

    def insert_contingents(conn, contingent):
        """
        insert contingent into the contingents table
        :param Connect conn: Connected database file.
        :param Tuple contingent: Contingent abberviation, Contingent Name, medals
        :return: location id
        """

        sql = ''' INSERT OR IGNORE INTO contingents(contingentAbbreviation, ContingentName, Medals) VALUES (?,?,?)'''

        cur = conn.cursor()
        cur.execute(sql, contingent)
        conn.commit()

        #print("commited contingents")
        return cur.lastrowid

    def insert_ContingentGames(conn, gameName, contingent, sport):
        """
        insert ContingentGames into the ContingentGames table

        :param Connect conn: Connected database file.
        :param string gameName: The name of the specific game to be played.
        :param string contingent: The name of the province.

        :return: game contingent 
        """

        query = ''' INSERT OR IGNORE INTO ContingentGames(gameName, contingent, sport) VALUES (?,?,?)'''

        cur = conn.cursor()
        queryTuple = (gameName, contingent, sport) 
        cur.execute(query, queryTuple)
        conn.commit()
        #print("commited ContingentGames")
        return cur.lastrowid

    def insert_person_with_contingent_sportName_personName(conn, Contingent, sportName, personName, personURL ):
        """
        Insert person into the persons table
        :param Connect conn: connected database file.
        :param string personName: person name (string).
        :return: person id
        """
        query = ''' INSERT OR IGNORE INTO Persons(Contingent, sportName, personName, URL) VALUES (?,?,?,?)'''

        cur = conn.cursor()
        queryTuple = (Contingent[0], sportName, personName, personURL)
        #print(queryTuple)
        cur.execute(query, queryTuple)
        conn.commit()
        #print("commited Persons")
        return cur.lastrowid

    def sql_select_person_by_personID_all_columns(conn, personID):
        """
        Gets all columns from person, refer to the database to see what order the columns are presented in.

        :param Connected conn: Connected database file.
        :param string personName: Person ID string. (string)
        :return: records
        """

        query = """select * from Persons where personID = ?"""

        cur = conn.cursor()

        queryTuple = (personID,)
        cur.execute(query, queryTuple)
        records = cur.fetchall()
        cur.close()

        return records

    def sql_select_persons_by_sport_all_columns(conn, sportName):
        """
        select personName, Contingent, and sportName
        :param Connect conn: Connected database file.
        :param personName: Person name string. (string)
        :param personSport: Name of sport. (string)

        :return: records
        """
        query = """ select * from Persons where SportName = '?'"""

        cur = conn.cursor()

        queryTuple = (sportName,)
        cur.execute(query, queryTuple)
        records = cur.fetchall()
        cur.close()

        return records

    def sql_select_person_by_contingent_all_columns(conn, contingent): 
        """
        select person, Contingent and sportname

        :param Connect conn: Connected database file.
        :param String personName: Person name string.
        :param String personSport: Name of sport.

        :return: records
        """
        query = """select * from Persons where Contingent = '?' """

        cur = conn.cursor()

        queryTuple = (contingent,)
        cur.execute(query, queryTuple)
        records = cur.fetchall()
        cur.close()

        return records

    def sql_select_person_by_person_name_all_columns(conn, name):
        """
        Select all columns for person who's name matches the value given, keep in mind that there could be two people with the same names.
        
        :param Connect conn: Connected database file.
        :param String name: Name of the person you're looking for. First and Last

        :Return: Returns the records matching the names.
        :rtype: tuple
        """

        query = """ select  * from Persons where personname = ?"""

        cur = conn.cursor()

        queryTuple = (name,)
        cur.execute(query, queryTuple)
        records = cur.fetchall()
        cur.close()

        return records

    def sql_select_person_by_person_name_sport_column_personName_column_contingent_column(conn, name):
        """
        Select person Name column, sport column, contingent column for person who's name matches the value given, keep in mind that there could be two people with the same names.
        :param Connect conn: Connected database file.
        :param String name: Name of the person you're looking for. First and Last

        :Return: Returns the records matching the names.
        :rtype: tuple
        """

        query = """ select personName, sportName, contingent from Persons where personName = ?"""

        cur = conn.cursor()

        queryTuple = (name,)
        cur.execute(query, queryTuple)
        records = cur.fetchall()
        cur.close()

        return records 

    def sql_select_person_by_any_column(conn, column, value):
        """
        Select all columns for Person that matches the column selected for the value provided

        :param Connect conn: Connected database file.
        :param String column: Column to be searched within.
        :param String Value: The value you want to check the column for, there is no exception if the value does not exist.
        :return: Matching records
        :rtype: tuple
        """

        query = """ select  * from Persons where ? = '?'"""

        cur = conn.cursor()

        queryTuple = (column, value)
        cur.execute = (query, queryTuple)
        records = cur.fetchall()
        cur.close()

        return records

    
    def sql_select_all_columns_for_contingents(conn, ContingentAbbreviation): 
        """
        Select all columns for contingent that matches the abbreviation

        :param Connect conn: Connected database file.
        :param ContingentAbbreviation: 

        :return: records
        """

        query = """ select * from Contingents where ContingentAbbreviation = '?'"""

        cur = conn.cursor()

        queryTuple = (ContingentAbbreviation,)
        cur.execute(query, queryTuple)
        records = cur.fetchall()
        cur.close()

        return records

    def sql_select_contingentName_from_contingents_table(conn):
        """
        Select contingent Name column from the Contingents table
        :param Connect conn: Connected database file.

        :return: records
        """

        query = """select contingentName from Contingents"""

        cur = conn.cursor()
        cur.execute(query)
        records = cur.fetchall()
        cur.close()

        return records
    def sql_select_medals_from_Contingents(conn):
        """
        Gets the medal count (gold,silver,bronze) for all contingents and the contingent name.

        :param Connect conn: Connected Database File.

        :return: Contingent and it's medal count
        :rtype: tuple

        """

        query = """select ContingentName, goldMedals, Silvermedals, bronzemedals From Contingents"""

        cur = conn.cursor()
        cur.execute(query)
        records = cur.fetchall()
        cur.close()

        return records

    def sql_select_medals_from_contingents_by_contingentName(conn, contingentName):
        """
        Gets the medals (gold,silver,brone) from contingents by the contingent name

        :param Connect conn: Connected Database File.
        :param String contingentName: name of contingent.
        
        :return: contingent name and the medal counts
        :rtype: tuple
        """

        query = """select ContingentName, goldMedals, Silvermedals, bronzemedals From Contingents Where contingentName = ?"""

        cur = conn.cursor()
        queryTuple = (contingentName,)
        cur.execute(query, queryTuple)
        records = cur.fetchall()
        cur.close()

        return records 

    def sql_select_medals_from_Contingents(conn):
        """
        Gets the medal count for all contingents

        :param Connect conn: Connected Database File.

        :return: Contingent and it's medal count
        :rtype: tuple

        """

        query = """select ContingentName, Medals From Contingents"""

        cur = conn.cursor()
        cur.execute(query)
        records = cur.fetchall()
        cur.close()

        return records

    

    def sql_select_contingent_by_contingent_name(conn, contingent):
        """
        Gets the contingent abbreviation and medal count by name

        :param Connect conn: Connected database file.
        :param String contingent: contingent name searching for.

        :return: Contingent
        :rtype: 
        """

    def sql_select_all_colums_from_contingent_games_by_contingent(conn, contingent):
        """
        Select all columns from the contingent games table by contingent name

        :param Connect conn: Connected database file.
        :param String Contingent: The name of the contingent you want to see the games for.

        :return: all games that are played by the Contingent
        :rtype: tuple
        """

        query = """select * from ContingentGames where contingent = '?'"""

        cur = conn.cursor()

        queryTuple = (contingent,)
        cur.execute(query, queryTuple)
        records = cur.fetchall()
        cur.close()

        return records

    def sql_select_all_columns_from_contingentgames_by_sport(conn, sport):
        """
        select all columns from the contingent games table by sport name

        :param Connect conn: Connected database file
        :param String sport: Name of Sport.

        :return
        """

        query = """ select * from ContingentGames where sport = '?' """
        cur = conn.cursor()
        queryTuple = (sport,)
        cur.execute(query, queryTuple)
        records = cur.fetchall()
        cur.close()

        return records

    def sql_select_all_columns_from_contingentgames_by_gamename(conn, gameName):
        """
        select all columns from the contingent games table by gameName():

        :param Connect conn: Connected database file.
        :param String gameName: Name of game being played.

        :return: Games with that name, the sport being played and the contingents name.
        :rtype: tuple.
        """

        query = "select * from contingentgames where gameName = '?'"

        cur = conn.cursor()
        queryTuple = (gameName,)

        cur.execute(query,queryTuple)
        records = cur.fetchall()
        cur.close()

        return records

    def sql_select_all_columns_from_contingentgames_by_gamename_and_sport():
        """
        
        """

    def sql_select_all_columns_from_games_by_sport(conn, sportName):
        """
        Select all columns from Games Table matching sport
        
        :param Connect conn: Connected database file.
        :param string sportName: Name of the sport.

        :return: rows
        """

    def sql_select_all_columns_from_games_by_sportName(conn, sportName):

        query = """ select * from Games Where sportName = '?'"""

        cur = conn.cursor()

        queryTuple = (sportName,)
        cur.execute(query, queryTuple)
        records = cur.fetchall()
        cur.close()

        return records

    def sql_select_all_columns_from_games_by_gameName(conn, gameName):
        """
        Select all columns from Games Table matching game name.
        
        :param Connect conn: Connected database file.
        :param string gameName: Name of the sport. (string)

        :return: rows
        """

        query = """ select * from Games Where sportName = '?'"""

        cur = conn.cursor()

        queryTuple = (gameName)
        cur.execute(query, queryTuple)
        records = cur.fetchall()
        cur.close()

        return records

    def sql_select_all_columns_from_sports(conn):
        """
        Select all columns from Sports

        :param Connect conn: Connected database file.

        :return: rows
        """
        
        query = """select * from Sports"""

        cur = conn.cursor()
        cur.execute(query)
        records = cur.fetchall()
        cur.close()

        return records


    def sql_exists_for_sports_by_name(conn, value):
        """
        This will check the database to see if an item exists.

        :param Connect conn: connected database file.
        :param string table: Name of the table you're checking in.
        :param string column: Name of the column you're checking

        :return: if item exists.
        :rtype: bool
        """

        query = """SELECT EXISTS (SELECT 1 FROM Sports WHERE SportName = ?) """
        
        cur = conn.cursor()
        queryTuple = (value, )
        cur.execute(query, queryTuple)
        records = cur.fetchall()
        cur.close()
        return bool(records)
    
    def sql_select_url_and_id_from_persons(conn):
        """
        This will select the columns url and ID from the persons table.

        :param Connect conn: Connected Database file.
        :return: records found.
        :rtype: bool
        """

        query = "SELECT personID, url FROM persons"

        cur=conn.cursor()
        cur.execute(query)
        records = cur.fetchall()
        cur.close()
        return records

    def sql_select_next_date(conn):
        """
        Finds the next game by earliest date and give sgamename and sport name to go with it, no other criteria.

        :param Connect conn: Connected Game

        :return: The earliest games
        :rtype: tuple
        """
        query = """ Select gameName, sportName, min(dates) as NextGame from games Where dates >= date() group by sportName"""

        cur = conn.cursor()
        cur.execute(query)
        records = cur.fetchall()
        cur.close()
        return records 

    def sql_update_hometown_type_age_hieght_weight_club_coach_position_goals_for_games_personal_best_result_award_personal_role_model_other_info_for_person(
        conn, hometown, type, age, height, weight, club, coach, position, goals_for_games, 
        personal_best_result, award, personal_role_model, other_info, personID):
        """
        Update the fields for hometown, type, age, height, weight, club, coach, position, goals_for_games, 
        personal_best_result, award, personal_role_model, other_info in the Persons table.

        :param Connect conn: Connected database file.
        :param String hometown: Hometown of the person.
        :param String type: Type of person e.g. Athlete/coach/trainer.
        :param String age: Age of person.
        :param String height: Height in cm of person.
        :param String weight: Weight in kg of person.
        :param String club: Local team or team outside of Canada summer games for person.
        :param String coach: Person coach if exists.
        :param String Position: Position in sport if applicable.
        :param String goals_for_games: Persons goals for games.
        :param String personal_best_result: Persons previous best result before the summer games.
        :param String award: Previous rewards achieved by person if applicable.
        :param String personal_role_model: Persons role model.
        :param String other_info: Additional info offered by the person.

        :param string personID: ID used to find person to update

        :return: if update successful
        :rtype: Bool
        """

        query = """ Update Persons SET hometown = ? , type = ? , age = ? , height = ? , weight = ? , club = ? , coach = ? , position = ? , goals_for_games = ? , personal_best_result = ? , award = ? , personal_role_model = ? , other_info = ? WHERE personID = ? """
        cur = conn.cursor()
        queryTuple = (hometown, type, age, height, weight, club, coach, position, 
        goals_for_games, personal_best_result, award, personal_role_model, other_info, personID)
        cur.execute(query, queryTuple)
        conn.commit()
        cur.close() 
        return True

    def sql_select_next_date_by_sportName(conn, sportName):
        """
        Finds the next games for the sport by the earliest date.

        :param Connect conn: Connected Game

        :return: The earliest games
        :rtype: tuple (gameName, sportName, contingent, date, times)
        """
        query = """ Select ContingentGames.gameName, sportName, contingent, dates, times from games, ContingentGames where sportName = ? AND contingentGames.gamename = games.gamename AND dates = (Select min(dates) from Games where sportName = ? AND contingentGames.gamename = games.gamename AND Dates >= Date())"""

        cur = conn.cursor()
        queryTuple = (sportName, sportName)
        cur.execute(query, queryTuple)
        records = cur.fetchall()
        cur.close()
        return records

    def sql_select_next_date_by_contingent(conn, contingent):
        """
        Is able to find the next game being played by the contingent

        :param Connect conn: Connected game
        :param String contingent: name of contingent

        :return: next dates game
        :rtype: tuple(gameName, sportName, contingent, date, times)
        """

        query = """ Select ContingentGames.gameName, sportName, contingent, dates, times from games, ContingentGames where Contingent = ? AND contingentGames.gamename = games.gamename AND dates = (Select min(dates) from Games, contingentgames where Contingent = ? AND contingentGames.gamename = games.gamename AND Dates >= Date())  """
        
        cur = conn.cursor()
        queryTuple = (contingent, contingent)

        cur.execute(query, queryTuple)
        records =cur.fetchall()
        cur.close()

        return records

    def select_next_time_by_date_and_sportName(conn, date, sportName):
        """
        Selects the next game by earliest time, with the selected date and sport.

        :param Connect conn: Connected database file.
        :param String sportName: Name of the sport.
        :param String date: YYYY-MM-DD

        :return: next game with 
        :rtype: tuple
        """
        query = """ select sportName, gameName, dates, Times from games where sportName = ? AND dates = ? AND Times = (Select min(Times) from Games where sportName = ? AND dates = ?)"""

        cur = conn.cursor()
        queryTuple = (sportName, date, sportName, date)

        cur.execute(query, queryTuple)
        records =cur.fetchall()
        cur.close()

        return records 
    
    def select_next_time_by_date_and_contingent(conn, date, contingent):
        """
        Selects the next game by earliest time using the date and contingent 

        :param Connect conn: Connected database file.
        :param String date: YYYY-MM-DD
        :param string contingent: 
        """

        query = """ select sportName, games.gameName, dates, contingent, Times from games, ContingentGames where contingent = ? AND contingentGames.GameName = Games.GameName AND dates = ? AND Times = (Select min(Times) from Games contingent = ? AND contingentGames.GameName = Games.GameName AND dates = ?)"""

        cur = conn.cursor()
        queryTuple = (contingent, date, contingent, date)
        cur.execute(query, queryTuple)
        records =cur.fetchall()
        cur.close()

        return records

    def select_next_time_by_date_and_Contingent_and_sport(conn, date, contingent, sport):
        """
        Selects the next game by earliest tume using the date, contingent and sport

        :param Connect conn: Connected database file.
        :param String date: YYYY-MM-DD
        :param String contingent: name of province/territory.
        :param  String sport: name of sport.

        :return: all records with the earliest time that has the given date, contingent and sport.
        :rtype: tuple
        """

        query = """ select sportName, Games.gameName, dates, contingent, Times from games, ContingentGames where contingent = ? AND contingentGames.GameName = Games.GameName AND dates = ? AND sportName = ? AND Times = (Select min(Times) from Games WHERE contingent = ? AND contingentGames.GameName = Games.GameName AND dates = ? AND sportName = ?) """

        cur = conn.cursor(contingent, date, sport)
        queryTuple = (query, queryTuple)
        cur.execute(query,queryTuple)
        records =cur.fetchall()
        cur.close()

        return records

    def sql_select_next_date_by_contingent_and_sport(conn, contingent, sport):
        """
        Is able to find the next date for the game being played by contingent and sport.

        :param Connect conn: Connected game
        :param String contingent: Name of contingent.
        :param String sport: Name of Sport.

        :return: next dates game
        :rtype: tuple(gameName, sportName, contingent, date, times)
        """

        query = """ Select ContingentGames.gameName, sportName, contingent, dates, times from games, ContingentGames where Contingent = ? AND sportName = ? AND contingentGames.gamename = games.gamename AND dates = (Select min(dates) from Games, contingentgames where Contingent = ? AND contingentGames.gamename = games.gamename AND sportName = ? AND Dates >= Date())"""
                     
        
        cur = conn.cursor()
        queryTuple = (contingent, sport, contingent, sport)

        cur.execute(query, queryTuple)
        records =cur.fetchall()
        cur.close()

        return records 


    


















