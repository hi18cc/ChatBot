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

    def insert_players(conn, player):
        """
        insert player into the players table
        :param conn:
        :param palyer:
        :return: player id
        """
        sql = ''' INSERT OR IGNORE INTO gameContingents(playerID, playerName) VALUES (?,?)'''

        cur = conn.cursor()
        cur.execute(sql, player)
        conn.commit()
        print("commited Players")
        return cur.lastrowid








