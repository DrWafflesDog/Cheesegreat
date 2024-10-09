#!/usr/bin/env python3 
from sys import exit

import utils.remote_view as rviewer
import utils.scraping as scraper
import utils.handling as handling

def main():
    print("Go")
    ws = scraper.WebScraper('Main')
    handle = handling.Handler()
    res = ws.parse_html('https://books.toscrape.com/')
    meta = ws.get_meta(res)
    result = handle.create_df_html('https://en.wikipedia.org/wiki/Geoffrey_Hinton')
    print(result)
    
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("Process killed by user.")
    except Exception as e:
        print("Error at : {}".format(e))
    finally:
        exit()