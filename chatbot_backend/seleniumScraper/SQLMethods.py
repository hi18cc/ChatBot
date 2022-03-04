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
        cursor.fe

        return conn

 
    def insert_games(conn, game):
        """
        insert game into the games table
        :param conn:
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
        :param conn:
        :param sport:
        :return: sport id
        """

        sql = ''' INSERT OR IGNORE INTO sports(SportName) VALUES(?)'''

        cur = conn.cursor()
        cur.execute(sql, sport)
        conn.commit()

        print(sport[0])

        return cur.lastrowid

    def insert_sportgames(conn, sportGame):
        """
        insert sportGame into the sportGames table
        :param conn:
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
        insert locaiton into the locations table
        :param conn:
        :param sport:
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
        :param conn:
        :param sport:
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
        :param conn:
        :param sport:
        :return: location id
        """

        sql = ''' INSERT OR IGNORE INTO contingents(contingent) VALUES (?)'''

        cur = conn.cursor()
        cur.execute(sql, contingent)
        conn.commit()

        print("commited contingents")
        return cur.lastrowid

    def insert_gameContingents(conn, gameContingent):
        """
        insert gameContingent into the gameContingents table
        :param conn:
        :param sport:
        :return: gameContingent id
        """

        sql = ''' INSERT OR IGNORE INTO gameContingents(gameName, contingentName) VALUES (?,?)'''

        cur = conn.cursor()
        cur.execute(sql, gameContingent)
        conn.commit()
        print("commited gameContingents")
        return cur.lastrowid

    def insert_players(conn, playerName):
        """
        Insert player into the players table
        :param conn: connected database file.
        :param playerName: player name (string).
        :return: player id
        """
        sql = ''' INSERT OR IGNORE INTO gameContingents(playerID, playerName) VALUES (?,?)'''

        cur = conn.cursor()
        cur.execute(sql, playerName)
        conn.commit()
        print("commited Players")
        return cur.lastrowid

    
    def sql_select_all_columns_query(conn, table, queryColumn, value):
        """
        Basic query which takes strings
        :param table: The tables in the database. (string)
        :param column: The column you want to check for e.g. 'playerName' = x. (string)
        :param value: The value you want to check for  'value' 'playerName' = value. (string)
        :return: records
        """
        query = """ select * from ? where ? = ?"""

        cur = conn.cursor()

        queryTuple = (table, queryColumn, value)
        cur.execute(query, queryTuple)
        records = cur.fetchall()
        cur.close()
        return records
        

    def sql_select_player(conn, playerName):
        """
        Gets the playerName, Contingent, and SportName column for player with a specific name.

        :param playerName: Player name string. (string)
        :return: records
        """

        query = """ select playerName, Contingent, SportName from Players, Sport where players.player = ? AND playerSport.PlayerID = Players.PlayerID"""

        cur = conn.cursor()

        queryTuple = (playerName,)
        cur.execute(query, queryTuple)
        records = cur.fetchall()
        cur.close()

        return records

    def sql_select_player_by_sport(conn, playerName, sportName):
        """
        select playerName, Contingent, and sportName
        :param conn: connected database file.
        :param playerName: Player name string. (string)
        :param playerSport: Name of sport . (string)

        :return: records
        """
        query = """ select playerName, Contingent, SportName from Players, PlayerSport where players.playerName = ? AND playerSport = ?"""

        cur = conn.cursor()

        queryTuple = (playerName, sportName)
        cur.execute(query, queryTuple)
        records = cur.fetchall()
        cur.close()

        return records

    def sql_select_player_by_contingent(conn, player, ContingentAbbreviation): 
        """
        select player, Contingent and sportname

        :param conn: connected database file.
        :param playerName: Player name string. (string)
        :param playerSport: Name of sport . (string)

        :return: records
        """
        query = """ select playerName, Contingent, SportName from Players, PlayerSport where players.playerName = ? AND Contingent = ? AND playerSport.PlayerID = Players.PlayerID"""

        cur = conn.cursor()

        queryTuple = (player, ContingentAbbreviation)
        cur.execute(query, queryTuple)
        records = cur.fetchall()
        cur.close()

        return records
    
    def sql_select_all_columns_for_contingents(conn, ContingentAbbreviation): 
        """
        Select all columns for contingent that matches the abbreviation

        :param conn: connected database file.
        :param ContingentAbbreviation: 

        :return: records
        """

        query = """ select * from Contingent where ContingentAbbreviation = ?"""

        cur = conn.cursor()

        queryTuple = (ContingentAbbreviation)
        cur.execute(query, queryTuple)
        records = cur.fetchall()
        cur.close()

        return records

    













