from googletrans import Translator

trans = Translator()

def translate (mytext,mysrc,mydest):
	transResult = trans.translate(text=mytext, src=mysrc, dest=mydest)
	translateList=[]
	for eachlist in transResult:
		translateList.append(eachlist.text)
	return translateList


