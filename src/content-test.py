import logging
import logging.config
import requests
import configparser
import src.constants

login_token = ""

def log_response(response_data):
	'''Log the response from any http request in one place, and in one format
	'''
	pass

def login():
	''' Log in and get login token'''
	pass

def uploadFile(fileName, filePath):
	''' Upload a file using EXP API.  Return UUID '''
	log_response(response_data)

def getFileData(fileUUID):
	'''Use the UUID returned from file upload to retrieve file version information'''
	pass

def deleteFile(fileUUID):
	'''use the UUID returned from file upload to delete the file in preparation for next test'''
	pass

if __name__ == '__main__':
	'''
	Init code for test - includes logging and configuration file setup
	'''
	config = configparser.ConfigParser()
	config.read(src.constants.CONFIG_FILE_PATH)
	baseurl = config['login']['baseurl']
	username = config['login']['username']
	password = config['login']['password']
	logging.config.fileConfig(src.constants.LOG_CONFIG_FILE_PATH)
	logging.info('Test is now beginning.  Configuration section complete')
	session = requests.Session();
