import sqlite3
import os
import json
import csv
import json
import requests

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
        self.url = "https://services5.arcgis.com/mnYJ21GiFTR97WFg/arcgis/rest/services/PH_masterlist/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=true&spatialRel=esriSpatialRelIntersects&outFields=%2A&outSR=102100&cacheHint=true&fbclid=IwAR3WIYausDM0uo0Hk8AIjuwk60hJe0ay60Z7utrGHRNyXtQGvBKx8BeoZXI"
        self.response = requests.request("GET", self.url)
        self.data = self.response.content
        self.output = json.loads(self.data)
        # print(self.output)

    def get_all_records(self):
        """
        Return a list of all items from records table.
        :return:
        """
        data = self.output['features']
        return data