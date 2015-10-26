import logging
import logging.config
import requests
import configparser
from res.constants import *

login_token = ""

def setup():
	config = configparser.ConfigParser()
	config.read(CONFIG_FILE_PATH)

def login