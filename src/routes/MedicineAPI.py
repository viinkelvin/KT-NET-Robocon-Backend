from flask import Blueprint
import controllers.MedicineController as MedicineController
medicine = Blueprint('medicine', __name__)
url='/medicine'

@medicine.route(url,methods=['GET'])
def getAll():
	return MedicineController.getAll()

@medicine.route(url+'/<id>',methods=['GET'])
def getOne(id):
	return MedicineController.getOne(id)


