from dbInterface import DBManager
from datetime import datetime
import json

class PilihanBeasiswa:
    def integertoDateString(num_tgl):
    #convert integer to date format in string (ex: 12 November 2019)
        string_tgl = str(num_tgl)
        date_object = datetime(year=int(string_tgl[0:4]),month=int(string_tgl[4:6]),day=int(string_tgl[6:8]))
        return (date_object.strftime("%d" + " %B " + "%Y"))
    def convertDate(info):
    #convert integer in json from integer to date format in string
        formatted_info = json.loads(info)
        for i in range(len(formatted_info)):
            formatted_info[i]['waktu_submit'] = PilihanBeasiswa.integertoDateString(formatted_info[i]['waktu_submit'])
        return (json.dumps(formatted_info))

    def checkDictResult(info):
    #check whether json is an error message or not
        for key in json.loads(info)[0]:
            if key == 'Message':
                break
            elif key == 'id_penyedia':
                info = PilihanBeasiswa.convertDate(info)
                break 
        return info
    # read
    # read all
    def lihatSemua():
        info = DBManager.readfromPilihanBeasiswa()
        return PilihanBeasiswa.checkDictResult(info)
    # read by ID

    def filterID(id_penyedia):
        info = DBManager.readfromPilihanBeasiswaByIDPenyedia(id_penyedia)
        return PilihanBeasiswa.checkDictResult(info)
    # read by NIM

    def filterNIM(nim):
        info = DBManager.readfromPilihanBeasiswaByNIM(nim)
        return PilihanBeasiswa.checkDictResult(info)

    #read by status seleksi
    def filterIDStatusSeleksi(id_penyedia,status_seleksi):
        info = DBManager.readfromPilihanBeasiswaByIDStatus(id_penyedia,status_seleksi)
        return PilihanBeasiswa.checkDictResult(info)
    # create
    def insertDetail(info):
        return DBManager.inserttoPilihanBeasiswa(info)

    # update
    def updateStatusSeleksi(info, id_penyedia, nim):
        return DBManager.updatetoPilihanBeasiswa(info, id_penyedia, nim)
