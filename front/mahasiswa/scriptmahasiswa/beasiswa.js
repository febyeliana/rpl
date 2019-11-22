function createRow(i, name, description) {
			let nameCell = document.createElement('td');
			nameCell.innerText = name;
			let numCell = document.createElement('td');
			numCell.innerText = i;
			let descriptionCell = document.createElement('td');
			descriptionCell.innerText = description;
			let row = document.createElement('tr');
			row.appendChild(numCell);
			row.appendChild(nameCell);
			row.appendChild(descriptionCell);
			
			let table = document.getElementById('bea');
			table.appendChild(row);
			nameCell.addEventListener('click', () => detail(name));
}

async function loadData() {
	let jurusan = window.localStorage.getItem('jurusan');
	let semester = window.localStorage.getItem('semester');
	let gpa = window.localStorage.getItem('gpa');
	let result = await fetch(`http://3.227.193.57:9000/beasiswa/jurusan/${jurusan}/semester/${semester}/gpa/${gpa}`);
	let json = await result.json();
	let table = document.getElementById('bea');
	table.innerHTML = '';
	let i = 1;
	for (let data of json) {
		createRow(i, data.nama, data.deskripsi);
		i++;
	}
}

const applyBeasiswa = async () => {
	let idpenyediabeasiswa = window.localStorage.getItem('idpenyediabeasiswa');
	let namabeasiswa = window.localStorage.getItem('namabeasiswa');
	let nim = window.localStorage.getItem('nim');
	console.log(idpenyediabeasiswa);
	console.log(namabeasiswa);
	console.log(nim);

	let id_penyediaElem = idpenyediabeasiswa;
	let nama_beasiswaElem = namabeasiswa;
	let nimElem = nim;

	console.log(id_penyediaElem);



  await fetch(`http://3.227.193.57:9000/pilihanbeasiswa`, {
    method: 'POST',
    mode:'cors',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      "id_penyedia": parseInt(id_penyediaElem),
      "nama_beasiswa":nama_beasiswaElem,
      "nim":nimElem
    })
  })

  console.log(
	JSON.stringify({
      "id_penyedia": parseInt(id_penyediaElem),
      "nama_beasiswa":nama_beasiswaElem,
      "nim":nimElem
    })
   )
  let urlPart = window.location.href.split('/');
    window.location = urlPart.splice(0, urlPart.length-1).join('/') + '/beasiswa.html';
    return;   
};

const detail = async (name) => {
  let urlPart = window.location.href.split('/');
  window.location = urlPart.splice(0, urlPart.length-1).join('/') + '/detailbeasiswa.html';

  window.localStorage.setItem('namabeasiswa', name);


}

let $ = (namabea) => document.getElementById(namabea);

const getProfileByName = async (namabea) => {
  let namaebeasiswa = window.localStorage.getItem('namabeasiswa');
  console.log(namaebeasiswa);
  
  let result = await fetch('http://3.227.193.57:9000/beasiswa');
  let data = await result.json();
  for(let item of data){
  	if(namaebeasiswa===item.nama){
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

		let idpenyediabeasiswa = window.localStorage.setItem('idpenyediabeasiswa',item.id_penyedia);
	}
  }
};