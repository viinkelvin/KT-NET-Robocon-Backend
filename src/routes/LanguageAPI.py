from flask import Blueprint
import controllers.LangController as LangController

language = Blueprint('language', __name__)
url='/language'

@language.route(url, methods=['GET'])
def getLanguage():
	return LangController.getLanguage();