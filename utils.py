import json

class Utils:
    def __init__(self):
        print ()
    def get_config(self) -> object:
        with open('config.json', 'r') as f:
            return json.load(f)


