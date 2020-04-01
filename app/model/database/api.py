import sqlite3
import os
import json
import csv
import json
import requests


class Database(object):
    """ Api database"""

    def __init__(self):
        self.connect()

    def connect(self):
        """
        Connect to 'covid-19' database
        :return:
        """

        limit = 2000
        offset = 0
        url = "https://services5.arcgis.com/mnYJ21GiFTR97WFg/arcgis/rest/services/PH_masterlist/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=true&spatialRel=esriSpatialRelIntersects&outFields=%2A&outSR=102100&cacheHint=true&fbclid=IwAR3WIYausDM0uo0Hk8AIjuwk60hJe0ay60Z7utrGHRNyXtQGvBKx8BeoZXI"
        data = dict(resultOffset=offset ,resultRecordCount=limit)
        response = requests.request("GET", url, params=data)
        data = response.content
        self.PH_masterlist = json.loads(data)



    def get_all_records(self):
        """
        Return a list of all items from PH_masterlist records table.
        :return:
        """
        data = self.PH_masterlist['features']
        return data
