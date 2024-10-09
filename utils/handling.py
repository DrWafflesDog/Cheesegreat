import pandas as pd
import utils.handling as handling

class Handler():
    
    def __init__(self):
        pass
    
    def preload_df(self, titles, contents):
        if len(titles) != len(contents):
            return ''
        data = []
        for title in titles:
            for content in contents:
                data[title] = content
        return data
                
    def create_df(self, data):
        df = pd.DataFrame(data)
        return df
    
    def create_df_html(self, html):
        df = pd.read_html(str(html))
        if len(df) > 0:
            return df
        else:
            return None
    
    def to_xslx(self, data, filename='cg_output.xlsx'):
        df = pd.DataFrame(data=data)
        df.to_excel(filename)