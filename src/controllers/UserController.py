from flask import jsonify
from flask import request

def userinformation():
	content = request.get_json()
	userID = content['user_id']
	print (content['user_id'])
	return userID

def usera():
	return 'tesst hendi API'

