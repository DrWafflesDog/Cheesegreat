from selenium import *

class RemoteViewer():
    
    def __init__(self, t=''):
        self.set_target(t)
    
    def get_target():
        return self.target_url
    
    def set_target(t_url):
        self.target_url = t_url