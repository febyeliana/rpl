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
    #if waktu_tutup < current date of server, append invalid to json; else append valid
        formatted_info = json.loads(info)
        for i in range(len(formatted_info)):
            if((formatted_info[i]['waktu_tutup']) < DetailBeasiswa.getCurrentDate()):
                formatted_info[i]['ketersediaan'] = 'invalid'
            else:
                formatted_info[i]['ketersediaan'] = 'valid'
        return(json.dumps(formatted_info))

    def integertoDateString(num_tgl):
    #convert integer to date format in string (ex: 12 November 2019)
        string_tgl = str(num_tgl)
        date_object = datetime(year=int(string_tgl[0:4]),month=int(string_tgl[4:6]),day=int(string_tgl[6:8]))
        return (date_object.strftime("%d" + " %B " + "%Y"))

    def convertDate(info):
    #convert integer in json from integer to date format in string
        formatted_info = json.loads(info)
        for i in range(len(formatted_info)):
            formatted_info[i]['waktu_buka'] = DetailBeasiswa.integertoDateString(formatted_info[i]['waktu_buka'])
            formatted_info[i]['waktu_tutup'] = DetailBeasiswa.integertoDateString(formatted_info[i]['waktu_tutup'])
        return (json.dumps(formatted_info))

    def checkDictResult(info):
    #check whether json is an error message or not
        for key in json.loads(info)[0]:
            if key == 'Message':
                break
            elif key == 'id_penyedia':
                info = DetailBeasiswa.checkDate(info)
                info = DetailBeasiswa.convertDate(info)
                break 
        return info

    # read
    # read all

    def lihatSemua():
        info = DBManager.readfromDetailBeasiswa()
        info = DetailBeasiswa.checkDate(info)
        return (DetailBeasiswa.convertDate(info))

    def filterID(id_penyedia):
        info = DBManager.readfromDetailBeasiswaByID(id_penyedia)
        return (DetailBeasiswa.checkDictResult(info))

    # filter by fakultas and its combinations
    def filterFakultas(fakultas):
        info = DBManager.readfromDetailBeasiswaByFakultas(fakultas)
        return(DetailBeasiswa.checkDictResult(info)) 

    def filterFakultasJurusan(fakultas, jurusan):
        info = DBManager.readfromDetailBeasiswaByFakultasAndJurusan(
            fakultas, jurusan)
        return(DetailBeasiswa.checkDictResult(info)) 

    def filterFakultasJurusanSemester(fakultas, jurusan, semester):
        info = DBManager.readfromDetailBeasiswaByFakultasAndJurusanAndSemester(
            fakultas, jurusan, semester)
        return(DetailBeasiswa.checkDictResult(info))

    def filterFakultasJurusanMinGPA(fakultas, jurusan, gpa):
        info = DBManager.readfromDetailBeasiswaByFakultasAndJurusanAndMinGPA(
            fakultas, jurusan, gpa)
        return(DetailBeasiswa.checkDictResult(info))

    def filterFakultasSemester(fakultas, semester):
        info = DBManager.readfromDetailBeasiswaByFakultasAndSemester(
            fakultas, semester)
        return(DetailBeasiswa.checkDictResult(info))

    def filterFakultasSemesterMinGPA(fakultas, semester, gpa):
        info = DBManager.readfromDetailBeasiswaByFakultasAndSemesterAndMinGPA(
            fakultas, semester, gpa)
        return(DetailBeasiswa.checkDictResult(info))

    def filterFakultasMinGPA(fakultas, gpa):
        info = DBManager.readfromDetailBeasiswaByFakultasAndMinGPA(
            fakultas, gpa)
        return(DetailBeasiswa.checkDictResult(info))

    def filterAll(fakultas, jurusan, semester, gpa):
        info = DBManager.readfromDetailBeasiswaByAllParameters(
            fakultas, jurusan, semester, gpa)
        return(DetailBeasiswa.checkDictResult(info))


# filter by jurusan and its combinations
    def filterJurusan(jurusan):
        info = DBManager.readfromDetailBeasiswaByJurusan(jurusan)
        return(DetailBeasiswa.checkDictResult(info))

    def filterJurusanSemester(jurusan, semester):
        info = DBManager.readfromDetailBeasiswaByJurusanAndSemester(
            jurusan, semester)
        return(DetailBeasiswa.checkDictResult(info))

    def filterJurusanMinGPA(jurusan, gpa):
        info = DBManager.readfromDetailBeasiswaByJurusanAndMinGPA(jurusan, gpa)
        return(DetailBeasiswa.checkDictResult(info))
        
    def filterJurusanSemesterMinGPA(jurusan, semester, gpa):
        info = DBManager.readfromDetailBeasiswaByJurusanSemesterMinGPA(
            jurusan, semester, gpa)
        return(DetailBeasiswa.checkDictResult(info))

# filter by semester and its combinations
    def filterSemester(semester):
        info = DBManager.readfromDetailBeasiswaBySemester(semester)
        return(DetailBeasiswa.checkDictResult(info))

    def filterSemesterMinGPA(semester, gpa):
        info = DBManager.readfromDetailBeasiswaBySemesterMinGPA(semester, gpa)
        return(DetailBeasiswa.checkDictResult(info))

# filter by gpa
    def filterMinGPA(gpa):
        info = DBManager.readfromDetailBeasiswaByMinGPA(gpa)
        return(DetailBeasiswa.checkDictResult(info))

    def filterAktif(id_penyedia,aktif):
        info = DBManager.readfromDetailBeasiswaByAktif(id_penyedia,aktif)
        return(DetailBeasiswa.checkDictResult(info))

# create
    def insertDetail(info):
        return DBManager.inserttoDetailBeasiswa(info)

# update
    def updateAktif(info,id_penyedia):
        return DBManager.updateAktifDetailBeasiswa(info,id_penyedia)
