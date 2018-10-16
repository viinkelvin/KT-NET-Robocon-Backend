from googletrans import LANGUAGES
from flask import jsonify
def getLanguage():
	return jsonify(LANGUAGES)