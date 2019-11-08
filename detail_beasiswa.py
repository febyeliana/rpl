from dbInterface import DBManager

class DetailBeasiswa:
	#read 
	#read all
	def lihatSemua():
		return DBManager.readfromDetailBeasiswa()
		
	#filter by fakultas and its combinations
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

	#filter by jurusan and its combinations
	def filterJurusan(jurusan):
		return DBManager.readfromDetailBeasiswaByJurusan(jurusan)
	def filterJurusanSemester(jurusan,semester):
		return DBManager.readfromDetailBeasiswaByJurusanAndSemester(jurusan,semester)
	def filterJurusanMinGPA(jurusan,gpa):
		return DBManager.readfromDetailBeasiswaByJurusanAndMinGPA(jurusan,gpa)
	def filterJurusanSemesterMinGPA(jurusan,semester,gpa):
		return DBManager.readfromDetailBeasiswaByJurusanSemesterMinGPA(jurusan,semester,gpa)

	#filter by semester and its combinations
	def filterSemester(semester):
		return DBManager.readfromDetailBeasiswaBySemester(semester)
	def filterSemesterMinGPA(semester,gpa):
		return DBManager.readfromDetailBeasiswaBySemesterMinGPA(semester,gpa)

	#filter by gpa
	def filterMinGPA(gpa):
		return DBManager.readfromDetailBeasiswaByMinGPA(gpa)


