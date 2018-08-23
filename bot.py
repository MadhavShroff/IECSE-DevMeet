import os, sys
import random
import json
import requests
from time import sleep

# Assuming comic files are in a folder 'comics'
comics = [item for item in os.listdir(os.path.join(os.getcwd(), 'comics'))]

API_TOKEN = '519269089:AAFL9IDX7x46Z2Qb8MBO2XVRCb3t9X8ZuCA'

base_url = 'https://api.telegram.org/bot{token}/'.format(token=API_TOKEN)

current_offset = 0

def getMe():
	return requests.get(''.join([base_url, 'getMe'])).json()

def getUpdates():
	return requests.get(''.join([base_url, 'getUpdates']), params={'offset': current_offset}).json()

def sendMessage(chatId, text):
	requests.get(''.join([base_url, 'sendMessage']), params={
		'chat_id': chatId,
		'text': text,
	})

def sendPhoto(chatId):
	requests.post(
		''.join([base_url, 'sendPhoto']), 
		files={ 'photo': open('comics/{filename}'.format(filename=random.choice(comics)), 'rb')},
		data={ 'chat_id': chatId }
	)

while True:
	results = getUpdates()['result']
	for result in results:
		update_id = result['update_id']
		chat_id = result['message']['chat']['id']
		if current_offset <= update_id:
			current_offset = update_id + 1

			if result['message']['text'] == '/hitme':
				sendPhoto(chat_id)
			else:
				sendMessage(chat_id, 'Ask for a comic with /hitme')
	sleep(2)