import pymysql
import db_config as dbconfig
from flask import jsonify
from flask import request
import translate as translate
import resulthelper as resulthelper
def getUserLatestResult(user_code):
	try:
		lang = request.headers['lang']
		print(lang)
		conn=pymysql.connect(host=dbconfig.host,user=dbconfig.user,password=dbconfig.password,db=dbconfig.db)
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("""SELECT users.*,results.* FROM users 
			LEFT JOIN results on users.id=results.user_id
			WHERE users.user_code=%s""", user_code)
		row = cursor.fetchone()
		labelTransDict=getLabelTranslate(lang)
		finaljson= combineDataAndlabel(row,labelTransDict)

		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

def getLabelTranslate(destlang):
	labeldict=resulthelper.labelList
	labelValueList=[]
	for k in labeldict.values():
		labelValueList.append(k)
	i=0
	labelValuetrans=translate.translate(labelValueList,'ja',destlang)
	for key in labeldict:
		labeldict[key]=labelValuetrans[i]
		i=i+1
	return labeldict

def combineDataAndlabel(data, label):
	for eachlabel in label:
		if eachlabel in data:
			data[eachlabel]={"text":label[eachlabel],"value":data[eachlabel]}
		else:
			data.update({eachlabel : label[eachlabel]})
	return data
