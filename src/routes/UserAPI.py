from flask import Blueprint
import controllers.UserController as UserController
user = Blueprint('user', __name__)
url='/user'

@user.route(url+'/<user_code>',methods=['GET'])
def getUserLatestResult(user_code):
	return UserController.getUserLatestResult(user_code)




