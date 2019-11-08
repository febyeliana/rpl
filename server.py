from flask import Flask, request, make_response
from detail_beasiswa import DetailBeasiswa

app = Flask(__name__)

# lihat semua detail beasiswa
@app.route('/detailbeasiswa',methods=['GET'])
def detailbeasiswa():
	#method GET
	if request.method == 'GET':
		resp = make_response(DetailBeasiswa.lihatSemua(),200)
	resp.mimetype = "application/json" 
	#method POST


	return resp

#filter by fakultas
@app.route('/detailbeasiswa/fakultas/<fakultas>',methods=['GET'])
def detailbeasiswa_fakultas(fakultas):
	resp = make_response(DetailBeasiswa.filterFakultas(fakultas),200)
	resp.mimetype = "application/json"
	return resp

#filter by fakultas jurusan
@app.route('/detailbeasiswa/fakultas/<fakultas>/jurusan/<jurusan>',methods=['GET'])
def detailbeasiswa_fakultas_jurusan(fakultas,jurusan):
	resp = make_response(DetailBeasiswa.filterFakultasJurusan(fakultas,jurusan),200)
	resp.mimetype = "application/json"
	return resp

#filter by fakultas jurusan semester
@app.route('/detailbeasiswa/fakultas/<fakultas>/jurusan/<jurusan>/semester/<semester>', methods=['GET'])
def detailbeasiswa_fakultas_jurusan_semester(fakultas,jurusan,semester):
	resp = make_response(DetailBeasiswa.filterFakultasJurusanSemester(fakultas,jurusan,semester),200)
	resp.mimetype = "application/json"
	return resp

#filter by fakultas jurusan gpa
@app.route('/detailbeasiswa/fakultas/<fakultas>/jurusan/<jurusan>/gpa/<gpa>', methods = ['GET'])
def detailbeasiswa_fakultas_jurusan_gpa(fakultas,jurusan,gpa):
	resp = make_response(DetailBeasiswa.filterFakultasJurusanMinGPA(fakultas,jurusan,gpa),200)
	resp.mimetype = "application/json"
	return resp

#filter by fakultas semester
@app.route('/detailbeasiswa/fakultas/<fakultas>/semester/<semester>',methods=['GET'])
def detailbeasiswa_fakultas_semester(fakultas,semester):
	resp = make_response(DetailBeasiswa.filterFakultasSemester(fakultas,semester),200)
	resp.mimetype = "application/json"
	return resp

#filter by fakultas semester gpa
@app.route('/detailbeasiswa/fakultas/<fakultas>/semester/<semester>/gpa/<gpa>', methods = ['GET'])
def detailbeasiswa_fakultas_semester_gpa(fakultas,semester,gpa):
	resp = make_response(DetailBeasiswa.filterFakultasSemesterMinGPA(fakultas,semester,gpa),200)
	resp.mimetype = "application/json"
	return resp

#filter by fakultas gpa
@app.route('/detailbeasiswa/fakultas/<fakultas>/gpa/<gpa>', methods = ['GET'])
def detailbeasiswa_fakultas_gpa(fakultas,gpa):
	resp = make_response(DetailBeasiswa.filterFakultasMinGPA(fakultas,gpa),200)
	resp.mimetype = "application/json"
	return resp

#filter all (fakultas,jurusan,semester,gpa)
@app.route('/detailbeasiswa/fakultas/<fakultas>/jurusan/<jurusan>/semester/<semester>/gpa/<gpa>', methods = ['GET'])
def detailbeasiswa_fakultas_jurusan_semester_gpa(fakultas,jurusan,semester,gpa):
	resp = make_response(DetailBeasiswa.filterAll(fakultas,jurusan,semester,gpa),200)
	resp.mimetype = "application/json"
	return resp
	
if __name__ == '__main__':
	print('Maid cafe running at port 9000')
	#jalankan server
	app.run(threaded = True, host='192.168.43.206', port=9000)