from dbInterface import DBManager


class PilihanBeasiswa:
    # read
    # read all
    def lihatSemua():
        return DBManager.readfromPilihanBeasiswa()
    # read by ID

    def filterID(id_penyedia):
        return DBManager.readfromPilihanBeasiswaByIDPenyedia(id_penyedia)
    # read by NIM

    def filterNIM(nim):
        return DBManager.readfromPilihanBeasiswaByNIM(nim)

    # create
    def insertDetail(info):
        return DBManager.inserttoPilihanBeasiswa(info)

    # update
    def updateStatusSeleksi(info, id_penyedia, nim):
        return DBManager.updatetoPilihanBeasiswa(info, id_penyedia, nim)
