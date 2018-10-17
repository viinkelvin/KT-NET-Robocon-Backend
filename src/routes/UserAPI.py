from flask import Blueprint
import controllers.UserController as UserController
user = Blueprint('user', __name__)
url='/user'

@user.route(url,methods=['POST'])
def UserInformation():
	return UserController.UserInformation()




