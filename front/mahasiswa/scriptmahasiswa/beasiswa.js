let tabel = `<table class="tablelistbeasiswa">
	<thead>
		<tr>
			<th>No</th>
			<th>Nama beasiswa</th>
			<th>Deskripsi</th>
			<th>Apply</th>
		</tr>
	</thead>
	<tbody id="{}">
		<tr></tr>
	</tbody>
	</table>
	<a class="buttonformmhs" onclick="applyBeasiswa('{X}')">Apply</a>`;

const createRow(tableId, penyedia, i, nama, apply) => {
	let penyediabea = document.createElement('td');
	penyediabea.style.display = 'None';
	penyediabea.innerText = penyedia;
	penyediabea.className = "penyedia";
	let nameCell = document.createElement('td');
	nameCell.innerText = nama;
	nameCell.className = "nama";
	let numCell = document.createElement('td');
	numCell.innerText = i;
	let applyCell = document.createElement('td');
	applyCell.className = "apply";
	let applyInput = document.createElement('input');
	applyInput.type ="checkbox";
	applyInput.name ="apply";
	console.log(apply);
	applyInput.checked = status === "Applied";
	applyCell.appendChild(applyInput);
	let row = document.createElement('tr');
	row.appendChild(penyediabea);
	row.appendChild(numCell);
	row.appendChild(nameCell);
	row.appendChild(applyCell);
	nameCell.addEventListener('click', () => detail(name));

	let table = document.getElementById('tableId');
	table.appendChild(row);
}

const loadData = async () => {
  let id = window.localStorage.getItem('id');
  let result = await fetch('http://3.227.193.57:9000/pilihanbeasiswa/id/' + id);
  let json = await result.json();
  let resultProgram = await fetch(`http://3.227.193.57:9000/beasiswa/id/${id}/aktif/Yes`);
  let jsonProgram = await resultProgram.json();

  let programs = {};
  for (let p of jsonProgram) {
    programs[p.nama] = [];
  }

  json = json.filter(x => (x.nama in programs));
  for (let p of json) {
    programs[p.nama].push(p);
  }

  let content = document.getElementById('table-content');
  content.innerHTML = '';

  programValues = Object.values(programs);

  for (let p of programValues) {
    if (p.length === 0) {
      continue;
    }
    content.innerHTML += `<br><h2>${p[0].nama}</h2>`;
    content.innerHTML += tableCode.replace("{}", `${p[0].nama}-table`).replace("{X}", `${p[0].nama}`);
  }

  for (let p of programValues) {
    if (p.length === 0) {
      continue;
    }
    let tableId = `${p[0].nama}-table`;

    let i = 1;
    for (let data of p) {
      createRow(tableId, data.nama, i, data.nim, data.status_seleksi);
      i++;
    }
  }
};

const acceptBeasiswa = async (tableId) => {
  let table = document.getElementById(tableId + '-table');
  let rows = table.getElementsByTagName('tr');
  let id = window.localStorage.getItem('id');

  for (let r of rows) {
    let nameCell = r.getElementsByClassName('name')[0];
    let statusCell = r.getElementsByClassName('status')[0];
    let statusInput = statusCell.getElementsByTagName('input')[0];
    let beaCell = r.getElementsByClassName('bea')[0];
    let nim = nameCell.innerText;

    await fetch(`http://3.227.193.57:9000/pilihanbeasiswa/id/${id}/nim/${nim}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({"status_seleksi": statusInput.checked ? "Applied" : "Not Applied", "nama_beasiswa": beaCell.innerText})
    })
  }

  await loadData();
};


const detail = async (id) => {
  let urlPart = window.location.href.split('/');
  window.location = urlPart.splice(0, urlPart.length-1).join('/') + '/detailbeasiswa.html';

  window.localStorage.setItem('beasiswa', id);
}

let $ = (id) => document.getElementById(id);

const getProfileById = async () => {
  let idpenyediabea = window.localStorage.getItem('idpenyedia');
  let namabea = window.localStorage.getItem('nama');
  let result = await fetch('http://3.227.193.57:9000/beasiswa/id/' + idpenyediabea);
  let data = await result.json();
  for(let item of data){
  	if(namabea===item.nama){
		let namaElem = $('nama');
		let waktu_bukaElem = $('waktu_buka');
		let waktu_tutupElem = $('waktu_tutup');
		let fakultasElem = $('fakultas');
		let jurusanElem = $('jurusan');
		let semesterElem = $('semester');
		let min_gpaElem = $('min_gpa');
		let deskripsiElem = $('deskripsi');
		let batas_semesterElem = $('batas_semester');
		let tipeElem = $('tipe');
		let aktifElem = $('aktif');
		let ketersediaanElem = $('ketersediaan');

		namaElem.innerText = item.nama;
		waktu_bukaElem.innerText = item.waktu_buka;
		waktu_tutupElem.innerText = item.waktu_tutup;
		fakultasElem.innerText = item.fakultas;
		jurusanElem.innerText = item.jurusan;
		semesterElem.innerText = item.semester;
		min_gpaElem.innerText = item.min_gpa;
		deskripsiElem.innerText = item.deskripsi;
		batas_semesterElem.innerText = item.batas_semester;
		tipeElem.innerText = item.tipe;
		aktifElem.innerText = item.aktif;
		ketersediaanElem.innerText = item.ketersediaan;
	}
  }
};