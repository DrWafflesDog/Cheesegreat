from requests import get
from bs4 import BeautifulSoup as bs
import json

class WebScraper:
    
    def __init__(self, name=''):
        self.name = name
        pass
    
    def parse_html(self, endpoint):
        response = get(endpoint).content
        resoup = bs(response, 'html.parser')
        return resoup
    
    def page_to_images(self, page):
        images = page.findAll('img')
        srcs = []
        for img in images:
            srcs.append(img.attrs['src'])
        return srcs
    
    def get_meta(self, page):
        meta = page.findAll('meta')
        return meta
    
    