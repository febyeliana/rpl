from dbInterface import DBManager

class DetailBeasiswa:
	#read
	def lihatSemua():
		return DBManager.readfromDetailBeasiswa()
	def filterFakultas(fakultas):
		return DBManager.readfromDetailBeasiswaByFakultas(fakultas)
	def filterFakultasJurusan(fakultas,jurusan):
		return DBManager.readfromDetailBeasiswaByFakultasAndJurusan(fakultas,jurusan)
	def filterFakultasJurusanSemester(fakultas,jurusan,semester):
		return DBManager.readfromDetailBeasiswaByFakultasAndJurusanAndSemester(fakultas,jurusan,semester)
	def filterFakultasJurusanMinGPA(fakultas,jurusan,gpa):
		return DBManager.readfromDetailBeasiswaByFakultasAndJurusanAndMinGPA(fakultas,jurusan,gpa)
	def filterFakultasSemester(fakultas,semester):
		return DBManager.readfromDetailBeasiswaByFakultasAndSemester(fakultas,semester)
	def filterFakultasSemesterMinGPA(fakultas,semester,gpa):
		return DBManager.readfromDetailBeasiswaByFakultasAndSemesterAndMinGPA(fakultas,semester,gpa)
	def filterFakultasMinGPA(fakultas,gpa):
		return DBManager.readfromDetailBeasiswaByFakultasAndMinGPA(fakultas,gpa)
	def filterAll(fakultas,jurusan,semester,gpa):
		return DBManager.readfromDetailBeasiswaByAllParameters(fakultas,jurusan,semester,gpa)



