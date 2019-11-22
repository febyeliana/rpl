# Tugas Besar Rekayasa Perangkat Lunak STI
## Pengeloaan Beasiswa Mahasiswa Program Sarjana
### Created By : Group 1
1. William Halim / 18217021 (Commit name: William)
2. Nicholaus Danispadmanaba Y / 18217028 (Commit name: osboxes.org or nicholausdy or Cloud User)
3. Feby Eliana Tengry / 18217030 (Commit name: Feby)
4. Dicky / 18217041 (Commit name: dicky)

### Stack (production server):
1. Virtual machine: Amazon Web Service EC2 t2.micro
2. Operating system: Red Hat Enterprise Linux (RHEL) 8
3. Web server: Nginx 1.14.1
4. Web Server Gateway Interface (WSGI): Gunicorn 20.0.0
5. Back End: Python 3.6.8 with Flask + PostgreSQL 10.10
6. Front End: HTML, CSS, and native JavaScript

### Requirements 
#### A. Without Installation
1. Browser with support for HTML rendering and JavaScript.
#### B. With Installation
1. Operating system: RHEL 8 or CentOS 8
2. Interpreter: Python 3.6.8
3. RDBMS: PostgreSQL 10.10
4. Versioning: Git

### Usage:
#### A. PBMPS-Mahasiswa
1. Access this URL: http://3.227.193.57:9001
2. Use this username: nekopara
3. Use this password: nekopara

#### B. PBMPS-Penyedia
1. Access this URL: http://3.227.193.57:9002
2. Use this username: hatsune
3. Use this password: hatsune

#### C. Endpoint testing
1. Access this URL: http://3.227.193.57:9000/<insert endpoint>
2. Documentation: https://orange-water-4285.postman.co/collections/9500366-0e70c673-8a24-43d9-af95-76ddd61edcbc?version=latest&workspace=823da7b9-c6b6-44f6-8a22-0b192f261509

### Installation:
#### Simple installation (softcore):
1. Clone git repository to your local path:
```console
git clone https://github.com/febyeliana/rpl.git 
```
2. Navigate to back-end path:
```console
cd rpl/back  
```
3. Run server.py with Python:
```console
python3 server.py  
```
4. Navigate to front-end path for mahasiswa:
```console
cd ../front/mahasiswa
```
5. Open login.html on your browser.
6. Navigate to front-end path for mahasiswa:
```console
cd ../penyedia
```
7. Open index.html on your browser.

#### Full installation (hardcore):
1. Install the back-end components on Gunicorn and Nginx by following instruction at this link: https://github.com/febyeliana/rpl/blob/master/AWS_Deployment_Nginx_Gunicorn_Deployment.txt

2. Install front-end components on Nginx by following instruction at this link: https://github.com/febyeliana/rpl/blob/master/AWS_Deployment_Nginx_PBMPS_FrontEnd.txt








