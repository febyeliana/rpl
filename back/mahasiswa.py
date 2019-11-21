from dbInterface import DBManager


class Mahasiswa:
    # read functions
    # login
    def login():
        return DBManager.readfromLoginMahasiswa()

    def lihatNIM(username):
        return DBManager.readfromLoginMappingMahasiswa(username)

    def lihatSemua():
        return DBManager.readfromMahasiswa()

    def filterNIM(nim):
        return DBManager.readfromMahasiswaByNIM(nim)

    # create function
    def insertDetail(info):
        return DBManager.inserttoMahasiswa(info)

    #update function
    def updateDetail(info,nim):
        return DBManager.updateDetailMahasiswa(info,nim)


