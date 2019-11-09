from dbInterface import DBManager

class Mahasiswa:
	#read functions
	def lihatSemua():
		return DBManager.readfromMahasiswa()
	def filterNIM(nim):
		return DBManager.readfromMahasiswaByNIM(nim)

	#create function
	def insertDetail(info):
		return DBManager.inserttoMahasiswa(info)


