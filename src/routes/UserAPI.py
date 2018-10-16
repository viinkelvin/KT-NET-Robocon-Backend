from flask import Blueprint
import controllers.UserController as UserController
user = Blueprint('user', __name__)
url='/user'

@user.route(url,methods=['POST'])
def userinformation():
	return UserController.userinformation()

@user.route(url + '/a',methods=['POST'])
def usera():
	return UserController.usera();


