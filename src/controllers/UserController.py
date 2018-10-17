import pymysql
import db_config as dbconfig
from flask import jsonify
from flask import request
def UserInformation():
	try:
		content = request.get_json()
		userID = content['user_id']
		conn=pymysql.connect(host=dbconfig.host,user=dbconfig.user,password=dbconfig.password,db=dbconfig.db)
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM user WHERE user_id=%s", userID)

		row = cursor.fetchone()
		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()


