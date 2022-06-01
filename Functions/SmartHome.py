import sys
import os
from . import token_extractor
from Settings import username, password, language
import subprocess

class Vacuum:
    def __init__(self):
        self.data = token_extractor.extract(username, password, language)
        self.ip = self.data[1]
        self.token = self.data[3]

    def start(self):
        command = f"miiocli dreamevacuum --ip {self.ip} --token {self.token} start"
        os.system(command)
    
    def stop(self):
        command = f"miiocli dreamevacuum --ip {self.ip} --token {self.token} stop"
        os.system(command)


