from dbInterface import DBManager


class PenyediaBeasiswa:
    # read
    # login
    def login():
        return DBManager.readfromLoginPenyedia()
    # read all
    def lihatSemua():
        return DBManager.readfromPenyedia()
    #lihat ID penyedia
    def lihatID(username):
        return DBManager.readfromLoginMappingPenyedia(username)
    # filter by ID

    def filterID(id_penyedia):
        return DBManager.readfromPenyediaByID(id_penyedia)

    # create
    def insertDetail(info):
        return DBManager.inserttoPenyediaBeasiswa(info)

    # update
    def updateDetail(info,id_penyedia):
        return DBManager.updatePenyediaBeasiswa(info,id_penyedia)
