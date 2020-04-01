import requests


class RecordsAPI(object):
    """ API for pulling COVID-19 records"""

    def __init__(self):
        self.ph_masterlist = None
        self.connect()

    def connect(self):
        limit = 500
        offset = 0
        url = "https://services5.arcgis.com/mnYJ21GiFTR97WFg/arcgis/rest/services/PH_masterlist/FeatureServer/0/query?f=json&where=1%3D1&returnGeometry=true&spatialRel=esriSpatialRelIntersects&outFields=%2A&outSR=102100&cacheHint=true&fbclid=IwAR3WIYausDM0uo0Hk8AIjuwk60hJe0ay60Z7utrGHRNyXtQGvBKx8BeoZXI"
        headers = {'cache-control': "no-cache"}

        all_records = []
        ctr = 0
        while True:
            params = dict(resultOffset=offset, resultRecordCount=limit)
            response = requests.request("GET", url, headers=headers, params=params).json()

            for item in response['features']:
                all_records.append(item['attributes'])

            if 'exceededTransferLimit' in response:
                offset += limit
                ctr += 1
            else:
                break

        self.ph_masterlist = all_records

    def get_all_records(self):
        """
        Query API for updated records
        :return:
        """
        self.connect()

        return self.ph_masterlist
