import json
import requests


class RecordsAPI(object):
    """ API for pulling COVID-19 records"""

    def __init__(self):
        self.ph_masterlist = None
        self.connect()

    def connect(self):
        """
        Connect to 'covid-19' database
        :return:
        """

        url = "https://services5.arcgis.com/mnYJ21GiFTR97WFg/arcgis/rest/services/PH_masterlist/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=true&spatialRel=esriSpatialRelIntersects&outFields=%2A&outSR=102100&cacheHint=true&fbclid=IwAR3WIYausDM0uo0Hk8AIjuwk60hJe0ay60Z7utrGHRNyXtQGvBKx8BeoZXI"

        response = requests.request("GET", url)
        data = response.content
        self.ph_masterlist = json.loads(data)

    def get_all_records(self):
        """
        Return a list of all items from PH_masterlist records table.
        :return:
        """
        data = self.ph_masterlist['features']
        return data
