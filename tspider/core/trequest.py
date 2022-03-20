'''
@Time    : 2021/1/25 21:14
@Author  : 19045845
'''
import cfscrape
import requests
from lxml import etree
from tspider.downloadermiddlewares import proxies


class TRequest:
    def __init__(self, url, headers, downloadjson=None, proxies=False):
        self.url = url
        self.headers = headers
        self.proxies = proxies
        self.json = downloadjson

    def proxies_get(self):
        response = requests.get(url=self.url, headers=self.headers, proxies=proxies)
        return response

    def get(self):
        response = requests.get(url=self.url, headers=self.headers)
        return response

    def request_get(self):
        if self.proxies:
            response = self.proxies_get()
        else:
            response = self.get()
        return response

    def request_get_text_sp(self):
        response = self.request_get()
        if response.status_code == 200:
            sp = etree.HTML(response.text)
        else:
            print(response.status_code)
        return sp

    def cfscrape_proxies_get_(self, scraper):
        response = scraper.get(url=self.url, proxies=proxies)
        return response

    def cfscrape_get_(self, scraper):
        response = scraper.get(url=self.url)
        return response

    def cfscrape_get(self):
        scraper = cfscrape.create_scraper(delay=10)
        if self.proxies:
            response = self.cfscrape_proxies_get_(scraper)
        else:
            response = self.cfscrape_get_(scraper)
        return response

    def cfscrape_get_text_sp(self):
        response = self.cfscrape_get()
        if response.status_code == 200:
            sp = etree.HTML(response.text)
        else:
            print(response.status_code)
        return sp

    def proxies_post(self):
        response = requests.post(url=self.url, json=self.json, heads=self.headers, proxies=proxies)
        return response

    def post(self):
        response = requests.post(url=self.url, json=self.json, heads=self.headers)
        return response

    def request_post(self):
        if self.proxies:
            response = self.proxies_post()
        else:
            response = self.post()
        return response
