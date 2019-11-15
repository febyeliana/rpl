from flask import Flask, request, make_response
from flask_cors import CORS   #enable cross domain API request
from detail_beasiswa import DetailBeasiswa
from mahasiswa import Mahasiswa
from penyedia_beasiswa import PenyediaBeasiswa
from pilihan_beasiswa import PilihanBeasiswa

app = Flask(__name__)
CORS(app)

# mahasiswa routes
# login
@app.route('/mahasiswa/login', methods=['GET'])
def mahasiswa_login():
    # method GET
    resp = make_response(Mahasiswa.login(), 200)
    resp.mimetype = "application/json"
    return resp

# lihat semua mahasiswa
@app.route('/mahasiswa', methods=['GET', 'POST'])
def mahasiswa():
    # method GET
    if request.method == 'GET':
        resp = make_response(Mahasiswa.lihatSemua(), 200)
    # method POST
    elif request.method == 'POST':
        resp = make_response(Mahasiswa.insertDetail(request.data), 200)
    resp.mimetype = "application/json"
    return resp

# filter by NIM
@app.route('/mahasiswa/nim/<nim>', methods=['GET'])
def mahasiswa_nim(nim):
    resp = make_response(Mahasiswa.filterNIM(nim), 200)
    resp.mimetype = "application/json"
    return resp

# lihat NIM by username
@app.route('/mahasiswa/map/username/<username>', methods=['GET'])
def mahasiswa_map(username):
    resp = make_response(Mahasiswa.lihatNIM(username),200)
    resp.mimetype = "application/json"
    return resp


# penyedia beasiswa routes
# login
@app.route('/penyedia/login', methods=['GET'])
def penyedia_login():
    # method GET
    resp = make_response(PenyediaBeasiswa.login(), 200)
    resp.mimetype = "application/json"
    return resp

# lihat semua penyedia beasiswa
@app.route('/penyedia', methods=['GET', 'POST'])
def penyediabeasiswa():
    # method GET
    if request.method == 'GET':
        resp = make_response(PenyediaBeasiswa.lihatSemua(), 200)
    # method POST
    elif request.method == 'POST':
        resp = make_response(PenyediaBeasiswa.insertDetail(request.data), 200)
    resp.mimetype = "application/json"
    return resp

#lihat ID penyedia by username
@app.route('/penyedia/map/username/<username>', methods=['GET'])
def penyedia_map(username):
    resp = make_response(PenyediaBeasiswa.lihatID(username),200)
    resp.mimetype = "application/json"
    return resp

# filter by ID
@app.route('/penyedia/id/<id_penyedia>', methods=['GET'])
def penyediabeasiswa_id(id_penyedia):
    resp = make_response(PenyediaBeasiswa.filterID(id_penyedia), 200)
    resp.mimetype = "application/json"
    return resp

# detail beasiswa routes
# lihat semua detail beasiswa
@app.route('/beasiswa', methods=['GET', 'POST'])
def detailbeasiswa():
    # method GET
    if request.method == 'GET':
        resp = make_response(DetailBeasiswa.lihatSemua(), 200)
    # method POST
    elif request.method == 'POST':
        resp = make_response(DetailBeasiswa.insertDetail(request.data), 200)
    resp.mimetype = "application/json"
    return resp

#filter by ID penyedia (sejarah beasiswa)
@app.route('/beasiswa/id/<id_penyedia>', methods=['GET'])
def detailbeasiswa_id(id_penyedia):
    resp = make_response(DetailBeasiswa.filterID(id_penyedia),200)
    resp.mimetype = "application/json"
    return resp
    
# filter by fakultas
@app.route('/beasiswa/fakultas/<fakultas>', methods=['GET'])
def detailbeasiswa_fakultas(fakultas):
    resp = make_response(DetailBeasiswa.filterFakultas(fakultas), 200)
    resp.mimetype = "application/json"
    return resp

# filter by fakultas jurusan
@app.route('/beasiswa/fakultas/<fakultas>/jurusan/<jurusan>', methods=['GET'])
def detailbeasiswa_fakultas_jurusan(fakultas, jurusan):
    resp = make_response(
        DetailBeasiswa.filterFakultasJurusan(fakultas, jurusan), 200)
    resp.mimetype = "application/json"
    return resp

# filter by fakultas jurusan semester
@app.route('/beasiswa/fakultas/<fakultas>/jurusan/<jurusan>/semester/<semester>', methods=['GET'])
def detailbeasiswa_fakultas_jurusan_semester(fakultas, jurusan, semester):
    resp = make_response(DetailBeasiswa.filterFakultasJurusanSemester(
        fakultas, jurusan, semester), 200)
    resp.mimetype = "application/json"
    return resp

# filter by fakultas jurusan gpa
@app.route('/beasiswa/fakultas/<fakultas>/jurusan/<jurusan>/gpa/<gpa>', methods=['GET'])
def detailbeasiswa_fakultas_jurusan_gpa(fakultas, jurusan, gpa):
    resp = make_response(DetailBeasiswa.filterFakultasJurusanMinGPA(
        fakultas, jurusan, gpa), 200)
    resp.mimetype = "application/json"
    return resp

# filter by fakultas semester
@app.route('/beasiswa/fakultas/<fakultas>/semester/<semester>', methods=['GET'])
def detailbeasiswa_fakultas_semester(fakultas, semester):
    resp = make_response(
        DetailBeasiswa.filterFakultasSemester(fakultas, semester), 200)
    resp.mimetype = "application/json"
    return resp

# filter by fakultas semester gpa
@app.route('/beasiswa/fakultas/<fakultas>/semester/<semester>/gpa/<gpa>', methods=['GET'])
def detailbeasiswa_fakultas_semester_gpa(fakultas, semester, gpa):
    resp = make_response(DetailBeasiswa.filterFakultasSemesterMinGPA(
        fakultas, semester, gpa), 200)
    resp.mimetype = "application/json"
    return resp

# filter by fakultas gpa
@app.route('/beasiswa/fakultas/<fakultas>/gpa/<gpa>', methods=['GET'])
def detailbeasiswa_fakultas_gpa(fakultas, gpa):
    resp = make_response(
        DetailBeasiswa.filterFakultasMinGPA(fakultas, gpa), 200)
    resp.mimetype = "application/json"
    return resp

# filter all (fakultas,jurusan,semester,gpa)
@app.route('/beasiswa/fakultas/<fakultas>/jurusan/<jurusan>/semester/<semester>/gpa/<gpa>', methods=['GET'])
def detailbeasiswa_fakultas_jurusan_semester_gpa(fakultas, jurusan, semester, gpa):
    resp = make_response(DetailBeasiswa.filterAll(
        fakultas, jurusan, semester, gpa), 200)
    resp.mimetype = "application/json"
    return resp

# filter by jurusan
@app.route('/beasiswa/jurusan/<jurusan>', methods=['GET'])
def detailbeasiswa_jurusan(jurusan):
    resp = make_response(DetailBeasiswa.filterJurusan(jurusan), 200)
    resp.mimetype = "application/json"
    return resp

# filter by jurusan semester
@app.route('/beasiswa/jurusan/<jurusan>/semester/<semester>', methods=['GET'])
def detailbeasiswa_jurusan_semester(jurusan, semester):
    resp = make_response(
        DetailBeasiswa.filterJurusanSemester(jurusan, semester), 200)
    resp.mimetype = "application/json"
    return resp

# filter by jurusan gpa
@app.route('/beasiswa/jurusan/<jurusan>/gpa/<gpa>', methods=['GET'])
def detailbeasiswa_jurusan_gpa(jurusan, gpa):
    resp = make_response(DetailBeasiswa.filterJurusanMinGPA(jurusan, gpa), 200)
    resp.mimetype = "application/json"
    return resp

# filter by jurusan semester gpa
@app.route('/beasiswa/jurusan/<jurusan>/semester/<semester>/gpa/<gpa>', methods=['GET'])
def detailbeasiswa_jurusan_semester_gpa(jurusan, semester, gpa):
    resp = make_response(DetailBeasiswa.filterJurusanSemesterMinGPA(
        jurusan, semester, gpa), 200)
    resp.mimetype = "application/json"
    return resp

# filter by semester
@app.route('/beasiswa/semester/<semester>', methods=['GET'])
def detailbeasiswa_semester(semester):
    resp = make_response(DetailBeasiswa.filterSemester(semester), 200)
    resp.mimetype = "application/json"
    return resp

# filter by semester gpa
@app.route('/beasiswa/semester/<semester>/gpa/<gpa>', methods=['GET'])
def detailbeasiswa_semester_gpa(semester, gpa):
    resp = make_response(
        DetailBeasiswa.filterSemesterMinGPA(semester, gpa), 200)
    resp.mimetype = "application/json"
    return resp

# filter by gpa
@app.route('/beasiswa/gpa/<gpa>', methods=['GET'])
def detailbeasiswa_gpa(gpa):
    resp = make_response(DetailBeasiswa.filterMinGPA(gpa), 200)
    resp.mimetype = "application/json"
    return resp

# pilihan beasiswa routes
@app.route('/pilihanbeasiswa', methods=['GET', 'POST'])
def pilihanbeasiswa():
    # method GET
    if request.method == 'GET':
        resp = make_response(PilihanBeasiswa.lihatSemua(), 200)
    # method POST
    elif request.method == 'POST':
        resp = make_response(PilihanBeasiswa.insertDetail(request.data), 200)
    resp.mimetype = "application/json"
    return resp


@app.route('/pilihanbeasiswa/id/<id_penyedia>', methods=['GET'])
def pilihanbeasiswa_id(id_penyedia):
    resp = make_response(PilihanBeasiswa.filterID(id_penyedia), 200)
    resp.mimetype = "application/json"
    return resp


@app.route('/pilihanbeasiswa/nim/<nim>', methods=['GET'])
def pilihanbeasiswa_nim(nim):
    resp = make_response(PilihanBeasiswa.filterNIM(nim), 200)
    resp.mimetype = "application/json"
    return resp


@app.route('/pilihanbeasiswa/id/<id_penyedia>/nim/<nim>', methods=['PUT'])
def pilihanbeasiswa_nim_id(id_penyedia, nim):
    resp = make_response(PilihanBeasiswa.updateStatusSeleksi(
        request.data, id_penyedia, nim), 200)
    resp.mimetype = "application/json"
    return resp


if __name__ == '__main__':
    print('Maid cafe running at port 9000')
    # jalankan server
    app.run(threaded=True, host='0.0.0.0', port=9000)
