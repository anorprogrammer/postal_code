import json
import requests as r
from data.config import API_KEY


class PostalCode:
    def __init__(self, base_url=None, api_type=None, method=None, m_format=None):
        # Example urls:
            # API: US Zip Code Distance
                # https://www.zipcodeapi.com/rest/DemoOnly00IKNl5il4zSPjW7rrwKtRgsD7DWA1JzTAzNmx5Z8lZRHyezCLDNoO4b/distance.json/12345/45678/km
            # API: Multiple US Zip Code Distances
                #
            # API: US Zip Codes by Radius
                #
            # API: Multiple US Zip Codes by Radius
                #
            # API: Find Close US Zip Codes
                #
            # API: US Zip Code to Location Information
                #
            # API: Multiple US Zip Codes to Location Information
                #
            # API: US Location to Zip Codes
                #
            # API: US State to Zip Codes
        self.base_url = base_url
        self.api_type = api_type
        self.method = method
        self.m_format = m_format

    def distance(self, m_format, zip_code_1, zip_code_2, units):
        pass
