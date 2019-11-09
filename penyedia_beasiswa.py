from dbInterface import DBManager

class PenyediaBeasiswa:
	#read
	#read all
	def lihatSemua():
		return DBManager.readfromPenyedia()
	#filter by ID
	def filterID(id_penyedia):
		return DBManager.readfromPenyediaByID(id_penyedia)

	#create
	def insertDetail(info):
		return DBManager.inserttoPenyediaBeasiswa(info)