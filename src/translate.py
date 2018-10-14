from googletrans import Translator

trans = Translator()

def readFile():
	srcFile = open('translate-result.txt','r')
	v = srcFile.readlines()
	print(v)

def translate (mytext,mysrc,mydest):
	transResult = trans.translate(text=mytext, src=mysrc, dest=mydest)
	writeToFile(transResult)




def writeToFile(txtList):
	file = open('translate-result.txt','w')

	for eachlist in txtList:
		file.writelines(eachlist.text + '\n')

	

translate(['私','学校','学生'],"ja","en")
# translate("尿酸 = 10021","ja","en")

readFile()