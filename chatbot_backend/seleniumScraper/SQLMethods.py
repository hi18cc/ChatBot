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
        cursor = conn.cursor

        return conn

 
    def insert_games(conn, game):
        """
        insert game into the games table
        :param Connect conn: conn connected database file.
        :param games:
        :return: game id
        """

        sql = ''' INSERT OR IGNORE INTO Games(GameName, SportName, Location, Event, GameDate, GameTime) VALUES(?,?,?,?,?,?)'''

        cur = conn.cursor()
        cur.execute(sql, game)
        conn.commit()
        print("commited Games")
        return cur.lastrowid

    def insert_sports(conn, sport):
        """
        insert sport into the sports table
        :param Connect conn: conn connected database file.
        :param sport:
        :return: sport id
        """

        sql = ''' INSERT OR IGNORE INTO sports(SportName) VALUES(?)'''

        cur = conn.cursor()
        cur.execute(sql, sport)
        conn.commit()


        return cur.lastrowid

    def insert_sportgames(conn, sportGame):
        """
        insert sportGame into the sportGames table
        :param Connect conn: conn connected database file.
        :param sport:
        :return: sportGames id
        """

        sql = ''' INSERT OR IGNORE INTO sportGames(SportName, GameName) VALUES (?,?)'''

        cur = conn.cursor()
        cur.execute(sql, sportGame)
        conn.commit()

        print("commited Sportgames")
        return cur.lastrowid

    def insert_locations(conn, location):
        """
        insert location into the locations table
        :param Connect conn: conn connected database file.
        :param Tuple location: Tuple with the location name. (location name,)
        :return: location id
        """

        sql = ''' INSERT OR IGNORE INTO locations(location) VALUES (?)'''

        cur = conn.cursor()
        cur.execute(sql, location)
        conn.commit()

        print("commited locations")
        return cur.lastrowid

    def insert_sportLocations(conn, sportLocation):
        """
        insert location into the locations table
        :param Connect conn: conn connected database file.
        :param Tuple sportLocation: The tuple containing (sportName, Location Name).
        :return: location id
        """

        sql = ''' INSERT OR IGNORE INTO sportLocations(SportName, Location) VALUES (?, ?)'''

        cur = conn.cursor()
        cur.execute(sql, sportLocation)
        conn.commit()

        print("commited sportLocations")
        return cur.lastrowid

    def insert_contingents(conn, contingent):
        """
        insert contingent into the contingents table
        :param Connect conn: conn connected database file.
        :param Tuple contingent: Contingent abberviation, Contingent Name, medals
        :return: location id
        """

        sql = ''' INSERT OR IGNORE INTO contingents(contingentAbbreviation, ContingentName, Medals) VALUES (?,?,?)'''

        cur = conn.cursor()
        cur.execute(sql, contingent)
        conn.commit()

        print("commited contingents")
        return cur.lastrowid

    def insert_gameContingents(conn, gameContingent):
        """
        insert gameContingent into the gameContingents table
        :param Connect conn: conn connected database file.
        :param tuple gameContingent:The tuple of (gameName, contingentName)
        :return: gameContingent id
        """

        sql = ''' INSERT OR IGNORE INTO gameContingents(gameName, contingentName) VALUES (?,?)'''

        cur = conn.cursor()
        cur.execute(sql, gameContingent)
        conn.commit()
        print("commited gameContingents")
        return cur.lastrowid

    def insert_person_with_contingent_sportName_playerName(conn, Contingent, sportName, personName, personURL ):
        """
        Insert person into the players table
        :param Connect conn: connected database file.
        :param string playerName: player name (string).
        :return: player id
        """
        query = ''' INSERT INTO Persons(Contingent, sportName, personName, URL) VALUES (?,?,?,?)'''

        cur = conn.cursor()
        queryTuple = (Contingent[0], sportName, personName, personURL)
        print(queryTuple)
        cur.execute(query, queryTuple)
        conn.commit()
        print("commited Players")
        return cur.lastrowid
    
    def sql_select_all_columns_query(conn, table, queryColumn, value):
        """
        Basic query which takes strings
        :param string table: The tables in the database.
        :param string column: The column you want to check for e.g. 'playerName' = x.
        :param string value: The value you want to check for  'value' 'playerName' = value.
        :return: records
        """
        query = """ select * from ? where ? = '?'"""

        cur = conn.cursor()

        queryTuple = (table, queryColumn, value)
        cur.execute(query, queryTuple)
        records = cur.fetchall()
        cur.close()
        return records
        
        

    def sql_select_player(conn, playerName):
        """
        Gets the playerName, Contingent, and SportName column for player with a specific name.

        :param string playerName: Player name string. (string)
        :return: records
        """

        query = """ select playerName, Contingent, SportName from Players, Sport where players.player = '?' AND playerSport.PlayerID = Players.PlayerID"""

        cur = conn.cursor()

        queryTuple = (playerName,)
        cur.execute(query, queryTuple)
        records = cur.fetchall()
        cur.close()

        return records

    def sql_select_player_by_sport(conn, playerName, sportName):
        """
        select playerName, Contingent, and sportName
        :param Connect conn: conn connected database file.
        :param playerName: Player name string. (string)
        :param playerSport: Name of sport . (string)

        :return: records
        """
        query = """ select playerName, Contingent, SportName from Players, PlayerSport where players.playerName = '?' AND playerSport = '?'"""

        cur = conn.cursor()

        queryTuple = (playerName, sportName)
        cur.execute(query, queryTuple)
        records = cur.fetchall()
        cur.close()

        return records

    def sql_select_player_by_contingent(conn, player, ContingentAbbreviation): 
        """
        select player, Contingent and sportname

        :param Connect conn: conn connected database file.
        :param playerName: Player name string. (string)
        :param playerSport: Name of sport . (string)

        :return: records
        """
        query = """ select playerName, Contingent, SportName from Players, PlayerSport where players.playerName = '?' AND Contingent = '?' AND playerSport.PlayerID = Players.PlayerID"""

        cur = conn.cursor()

        queryTuple = (player, ContingentAbbreviation)
        cur.execute(query, queryTuple)
        records = cur.fetchall()
        cur.close()

        return records
    
    def sql_select_all_columns_for_contingents(conn, ContingentAbbreviation): 
        """
        Select all columns for contingent that matches the abbreviation

        :param Connect conn: conn connected database file.
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
        :param Connect conn: conn connected database file.

        :return: records
        """

        query = """ select contingentName from Contingents"""

        cur = conn.cursor()
        cur.execute(query)
        records = cur.fetchall()
        cur.close()

        return records

    def sql_select_all_colums_from_contingent_games(conn, ContingentAbbreviation):
        """
        Select all columns from the contingent games table

        :param Connect conn: conn connected database file.
        :param String ContingentAbbreviation:

        :return: rows
        """

        query = """select * from ContingentGames where contingentAbbreviation = '?'"""

        cur = conn.cursor()

        queryTuple = (ContingentAbbreviation,)
        cur.execute(query, queryTuple)
        records = cur.fetchall()
        cur.close()

        return records

    def sql_select_all_columns_from_games_by_sport(conn, sportName):
        """
        Select all columns from Games Table matching sport
        
        :param Connect conn: conn connected database file.
        :param string sportName: Name of the sport. (string)

        :return: rows
        """

        query = """ select * from Games Where sportName = '?'"""

        cur = conn.cursor()

        queryTuple = (sportName)
        cur.execute(query, queryTuple)
        records = cur.fetchall()
        cur.close()

        return records

    def sql_select_all_columns_from_games_by_gameName(conn, gameName):
        """
        Select all columns from Games Table matching game name.
        
        :param Connect conn: conn connected database file.
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

        :param Connect conn: conn connected database file.

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

        :param Connect conn: conn connected database file.
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
















