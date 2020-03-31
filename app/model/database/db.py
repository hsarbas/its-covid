import sqlite3
import os
import json


class Database(object):
    """ SQLite3 database"""
    def __init__(self):
        self.connection = None
        self.cursor = None

        self.connect()

    def connect(self):
        """
        Connect to 'covid-19' database
        :return:
        """

        _dir = os.path.dirname(__file__)
        fname = 'covid-19.db'
        db_fname = os.path.join(_dir, fname)

        self.connection = sqlite3.connect(db_fname, check_same_thread=False)
        self.cursor = self.connection.cursor()

        self._init_db()  # uncomment to initialize database tables

    def _init_db(self):
        if self.check_table_exists('records') is None:
            self.create_records_table()
            self.read_data()

    def create_records_table(self):
        """
        Create records table
        :return:
        """

        self.cursor.execute("""
                            CREATE TABLE records (
                            FID INTEGER PRIMARY KEY,
                            sequ INTEGER,
                            PH_masterl TEXT,
                            edad INTEGER,
                            kasarian TEXT,
                            nationalit TEXT,
                            residence TEXT,
                            travel_hx TEXT,
                            symptoms TEXT,
                            confirmed TEXT,
                            facility TEXT,
                            latitude REAL,
                            longitude REAL,
                            status TEXT,
                            epi_link TEXT,
                            petsa TEXT)
                            """)

    def check_table_exists(self, table_name):
        """
        Returns True if table with name table_name exists
        """
        _table_name = (table_name, )

        self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", _table_name)
        return self.cursor.fetchone()

    def insert_record_to_table(self, values, table):
        """
        Inserts a record to the database.

        :param values: An array of values to be included
        :param table: table name
        """

        if table == 'records':
            fid = values[0]
            if not self.check_record_in_table(fid, 'records'):
                self.cursor.execute("""
                                    INSERT INTO records VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                                    """, values)

        self.connection.commit()

    def check_record_in_table(self, value, table):
        """
        Check if record exists in the database.

        :param values: An array of values to be checked
        :param table: table name
        """

        if table == 'records':
            _value = (value,)
            self.cursor.execute("SELECT * FROM records WHERE FID=?", _value)

    def get_all_records(self):
        """
        Return a list of all items from records table.
        :return:
        """

        self.cursor.execute("SELECT * FROM records")
        return self.cursor.fetchall()

    def read_data(self):
        """
        Parse data from 'data.json' and insert them into records table
        :return:
        """

        filename = os.path.join(os.path.dirname(__file__), 'data.json')

        with open(filename, 'r') as f:
            data_dict = json.load(f)
            for feature in data_dict['features']:
                values = tuple(feature['attributes'].values())
                self.insert_record_to_table(values, 'records')

        self.connection.commit()
        print('done!')
