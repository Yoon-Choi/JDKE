import json


class Utils:
    def get_config(self):
        with open('config.json', 'r') as f:
            return json.load(f)

    config = get_config()
