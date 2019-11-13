from dbInterface import DBManager
from datetime import datetime
import json


class DetailBeasiswa:
    def getCurrentDate():
        currentYear = str(datetime.now().year)
        currentMonth = str(datetime.now().month)
        currentDay = str(datetime.now().day)
        date = int(currentYear+currentMonth+currentDay)
        return date

    def checkDate(info):
        formatted_info = json.loads(info)
        for i in range(len(formatted_info)):
            if((formatted_info[i]['waktu_tutup']) < DetailBeasiswa.getCurrentDate()):
                formatted_info[i]['ketersediaan'] = 'invalid'
            else:
                formatted_info[i]['ketersediaan'] = 'valid'
        return(json.dumps(formatted_info))

    # read
    # read all

    def lihatSemua():
        info = DBManager.readfromDetailBeasiswa()
        return DetailBeasiswa.checkDate(info)

    # filter by fakultas and its combinations
    def filterFakultas(fakultas):
        info = DBManager.readfromDetailBeasiswaByFakultas(fakultas)
        return DetailBeasiswa.checkDate(info)

    def filterFakultasJurusan(fakultas, jurusan):
        info = DBManager.readfromDetailBeasiswaByFakultasAndJurusan(
            fakultas, jurusan)
        return DetailBeasiswa.checkDate(info)

    def filterFakultasJurusanSemester(fakultas, jurusan, semester):
        info = DBManager.readfromDetailBeasiswaByFakultasAndJurusanAndSemester(
            fakultas, jurusan, semester)
        return DetailBeasiswa.checkDate(info)

    def filterFakultasJurusanMinGPA(fakultas, jurusan, gpa):
        info = DBManager.readfromDetailBeasiswaByFakultasAndJurusanAndMinGPA(
            fakultas, jurusan, gpa)
        return DetailBeasiswa.checkDate(info)

    def filterFakultasSemester(fakultas, semester):
        info = DBManager.readfromDetailBeasiswaByFakultasAndSemester(
            fakultas, semester)
        return DetailBeasiswa.checkDate(info)

    def filterFakultasSemesterMinGPA(fakultas, semester, gpa):
        info = DBManager.readfromDetailBeasiswaByFakultasAndSemesterAndMinGPA(
            fakultas, semester, gpa)
        return DetailBeasiswa.checkDate(info)

    def filterFakultasMinGPA(fakultas, gpa):
        info = DBManager.readfromDetailBeasiswaByFakultasAndMinGPA(
            fakultas, gpa)
        return DetailBeasiswa.checkDate(info)

    def filterAll(fakultas, jurusan, semester, gpa):
        info = DBManager.readfromDetailBeasiswaByAllParameters(
            fakultas, jurusan, semester, gpa)
        return DetailBeasiswa.checkDate(info)

# filter by jurusan and its combinations
    def filterJurusan(jurusan):
        info = DBManager.readfromDetailBeasiswaByJurusan(jurusan)
        return DetailBeasiswa.checkDate(info)

    def filterJurusanSemester(jurusan, semester):
        info = DBManager.readfromDetailBeasiswaByJurusanAndSemester(
            jurusan, semester)
        return DetailBeasiswa.checkDate(info)

    def filterJurusanMinGPA(jurusan, gpa):
        info = DBManager.readfromDetailBeasiswaByJurusanAndMinGPA(jurusan, gpa)
        return DetailBeasiswa.checkDate(info)

    def filterJurusanSemesterMinGPA(jurusan, semester, gpa):
        info = DBManager.readfromDetailBeasiswaByJurusanSemesterMinGPA(
            jurusan, semester, gpa)
        return DetailBeasiswa.checkDate(info)

# filter by semester and its combinations
    def filterSemester(semester):
        info = DBManager.readfromDetailBeasiswaBySemester(semester)
        return DetailBeasiswa.checkDate(info)

    def filterSemesterMinGPA(semester, gpa):
        info = DBManager.readfromDetailBeasiswaBySemesterMinGPA(semester, gpa)
        return DetailBeasiswa.checkDate(info)

# filter by gpa
    def filterMinGPA(gpa):
        info = DBManager.readfromDetailBeasiswaByMinGPA(gpa)
        return DetailBeasiswa.checkDate(info)

# create
    def insertDetail(info):
        return DBManager.inserttoDetailBeasiswa(info)
