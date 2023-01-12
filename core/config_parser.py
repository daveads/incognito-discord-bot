from pprint import pprint

try:
    import tomllib
except ModuleNotFoundError:
    import tomli as tomllib


import logging
from rich.logging import RichHandler

logging.basicConfig(format='%(levelname)s ::: %(message)s', handlers=[RichHandler()])


class BotConfigs:
    def __init__ (self):
        with open("bot_config.toml", "rb") as f:
            self.data = tomllib.load(f)
        
    def role(self, role):
        if role in self.data["roles"]:
            return self.data["roles"][role]


    def channel(self, chn):

        if chn in self.data['channels']:
            return self.data['channels'][chn]