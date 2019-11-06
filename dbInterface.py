import psycopg2
from psycopg2.extras import RealDictCursor
import json
import datetime

class DBManager:
	def dateConverter(o):
		if isinstance(o, datetime,datetime):
			return o.__str__()

	def connect():
		#connect to postgresql
		conn = None
		try:
			#connect using md5 method
			conn = psycopg2.connect(host="192.168.43.206",database="pbmps",user="postgres",password="swordbeach")
			print("Connected to database")
			return conn
		except(Exception, psycopg2.DatabaseError) as error:
			print(error)

	def close(conn):
		#close connection to postgresql
		if conn is not None:
			conn.close()
			print("Database connection closed")

	def readfromPenyedia():
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			cur.execute(""" SELECT * FROM penyedia_beasiswa """)
			json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = {'Message': 'Failed to read record from mobile table'}
			json_result = json.dumps(dump)
		finally:
			print(json_result)
			return json_result
			DBManager.close(conn)

	def readfromPenyediaByID(id_penyedia):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM penyedia_beasiswa WHERE id_penyedia = %(id)s """
			values = {'id':id_penyedia}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = {'Message':'Invalid id_penyedia','id_penyedia':id_penyedia}
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = {'Message': 'Failed to read record from mobile table'}
			json_result = json.dumps(dump)
		finally:
			print(json_result)
			return json_result
			DBManager.close(conn)

	def readfromDetailBeasiswa():
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			cur.execute(""" SELECT * FROM detail_beasiswa """)
			json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = {'Message': 'Failed to read record from mobile table'}
			json_result = json.dumps(dump)
		finally:
			print(json_result)
			return json_result
			DBManager.close(conn)

	def readfromDetailBeasiswaByFakultas(fakultas):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE fakultas = %(id)s """
			values = {'id':fakultas}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = {'Message':'Invalid fakultas','Fakultas':fakultas}
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = {'Message': 'Failed to read record from mobile table'}
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			return json_result
			DBManager.close(conn)

	def readfromDetailBeasiswaByFakultasAndJurusan(fakultas,jurusan):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE fakultas = %(f)s AND jurusan = %(j)s """
			values = {'f':fakultas, 'j':jurusan}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = {'Message':'Invalid fakultas or jurusan','Fakultas':fakultas,'Jurusan':jurusan}
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = {'Message': 'Failed to read record from mobile table'}
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			return json_result
			DBManager.close(conn)

	def readfromDetailBeasiswaByFakultasAndJurusanAndSemester(fakultas,jurusan,semester):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE fakultas = %(f)s AND jurusan = %(j)s AND semester <= %(s)s AND batas_semester >= %(s)s """
			values = {'f':fakultas, 'j':jurusan, 's':semester}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = {'Message':'Invalid fakultas, jurusan, or semester','Fakultas':fakultas,'Jurusan':jurusan,'Semester':semester}
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = {'Message': 'Failed to read record from mobile table'}
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			return json_result
			DBManager.close(conn)

	def readfromDetailBeasiswaByFakultasAndJurusanAndMinGPA(fakultas,jurusan,gpa):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE fakultas = %(f)s AND jurusan = %(j)s AND min_gpa <= %(s)s """
			values = {'f':fakultas, 'j':jurusan, 's':gpa}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = {'Message':'Invalid fakultas, jurusan, or gpa','Fakultas':fakultas,'Jurusan':jurusan,'GPA':gpa}
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = {'Message': 'Failed to read record from mobile table'}
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			return json_result
			DBManager.close(conn)

	def readfromDetailBeasiswaByFakultasAndSemester(fakultas,semester):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE fakultas = %(f)s AND semester <= %(s)s AND batas_semester >= %(s)s """
			values = {'f':fakultas, 's':semester}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = {'Message':'Invalid fakultas or semester','Fakultas':fakultas, 'Semester':semester}
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = {'Message': 'Failed to read record from mobile table'}
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			return json_result
			DBManager.close(conn)
	
	def readfromDetailBeasiswaByFakultasAndSemesterAndMinGPA(fakultas,semester,gpa):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE fakultas = %(f)s AND semester <= %(s)s AND batas_semester >= %(s)s AND min_gpa <= %(g)s """
			values = {'f':fakultas, 's':semester, 'g':gpa}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = {'Message':'Invalid fakultas, semester, or gpa','Fakultas':fakultas, 'Semester':semester,'GPA':gpa}
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = {'Message': 'Failed to read record from mobile table'}
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			return json_result
			DBManager.close(conn)

	def readfromDetailBeasiswaByFakultasAndMinGPA(fakultas,gpa):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE fakultas = %(f)s AND min_gpa <= %(g)s """
			values = {'f':fakultas, 'g':gpa}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = {'Message':'Invalid fakultas or gpa','Fakultas':fakultas, 'GPA':gpa}
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = {'Message': 'Failed to read record from mobile table'}
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			return json_result
			DBManager.close(conn)

	def readfromDetailBeasiswaByAllParameters(fakultas,jurusan,semester,gpa):
		conn = DBManager.connect()
		try:
			cur = conn.cursor(cursor_factory=RealDictCursor)
			query = """ SELECT * FROM detail_beasiswa WHERE fakultas = %(f)s AND jurusan = %(j)s AND semester <= %(s)s AND batas_semester >= %(s)s AND min_gpa <= %(g)s """
			values = {'f':fakultas, 'j':jurusan,'s':semester, 'g':gpa}
			cur.execute(query,values)
			if (cur.rowcount == 0):
				dump = {'Message':'Invalid fakultas, jurusan, semester, or gpa','Fakultas':fakultas, 'Jurusan':jurusan,'Semester':semester,'GPA':gpa}
				json_result = json.dumps(dump)
			else:
				json_result = json.dumps(cur.fetchall())
		except(Exception, psycopg2.Error) as error:
			dump = {'Message': 'Failed to read record from mobile table'}
			json_result = json.dumps(dump)
			print(error)
		finally:
			print(json_result)
			return json_result
			DBManager.close(conn)

	








