import pymysql
import db_config as dbconfig
from flask import jsonify
from flask import request
import translate as translate
import resulthelper as resulthelper
def getAll():
	try:
		lang = request.headers['lang']
		print(lang)
		conn = pymysql.connect(host=dbconfig.host,user=dbconfig.user,password=dbconfig.password,db=dbconfig.db)
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT id,medicine_name,imgurl FROM medicines")
		rows = cursor.fetchall()
		resp = jsonify(rows)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

def getOne(id):
	try:
		lang = request.headers['lang']
		conn = pymysql.connect(host=dbconfig.host,user=dbconfig.user,password=dbconfig.password,db=dbconfig.db)
		cursor = conn.cursor(pymysql.cursors.DictCursor)
		cursor.execute("SELECT * FROM medicines WHERE id=%s", id)

		row = cursor.fetchone()
		dataTrans=getDataTranslate(lang,row)
		labelTransDict=getLabelTranslate(lang)
		finaljson= combineDataAndlabel(row,labelTransDict,dataTrans)

		resp = jsonify(row)
		resp.status_code = 200
		return resp
	except Exception as e:
		print(e)
	finally:
		cursor.close()
		conn.close()

def getLabelTranslate(destlang):
	labeldict=resulthelper.medicineList
	labelValueList=[]
	for k in labeldict.values():
		labelValueList.append(k)
	i=0
	# temporary stop
	# labelValuetrans=translate.translate(labelValueList,'ja','destlang')
	# for key in labeldict:
	# 	labeldict[key]=labelValuetrans[i]
	# 	i=i+1
	return labeldict

def combineDataAndlabel(data, label, value):
	# looping the data
	for eachlabel in label:
		if eachlabel in data:
			data[eachlabel]={"text":label[eachlabel],"value":value[eachlabel]}
		else:
			data.update({eachlabel : label[eachlabel]})
	return data

def getDataTranslate(destlang,data):
	medicineDataDict=data
	medicineDataDict.pop('id')
	medicineDataDict.pop('medicine_name')

	medicineDataList=[]
	for k in medicineDataDict.values():
		medicineDataList.append(k)
	i=0
	# temporary stop
	# dataValuetrans=translate.translate(medicineDataList,'ja','destlang')
	# for key in medicineDataDict:
	# 	medicineDataDict[key]=dataValuetrans[i]
	# 	i=i+1
	return medicineDataDict
