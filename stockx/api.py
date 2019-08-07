import requests
import pandas as pd
import json
from pandas.io.json import json_normalize


class StockXScraper:
    def __init__(self):
        self.BaseUrl = 'https://stockx.com/api/'
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
        self.category = 'sneakers'
        self.currency = 'EUR'
        self.page = None
        self.params = 'browse?productCategory=%s&currency=%s&page=%d'
        self.product_list = None
        self.df = pd.DataFrame()

    def buildUrl(self):
        self.parameters = self.params % (
            self.category,
            self.currency,
            self.page
        )
        return self.BaseUrl + self.parameters

    def get_listings(self, page=1):
        self.page = page
        self.request = requests.get(self.buildUrl(), headers=self.headers)
        self.response = self.request.json()
        return self.response

    def parse_products(self, response):
        if response['Products'] is not None:
            self.product_list = self.response['Products']
            if len(self.df) == 0:
                self.df = json_normalize(self.product_list)
            else:
                self.df = pd.concat(
                    [self.df, json_normalize(self.product_list)])
