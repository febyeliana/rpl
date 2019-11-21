let $ = (nim) => document.getElementById(nim);

const createRow = (i, namabeasiswa, namapenyedia, date, status) => {
	let numCell = document.createElement('td');
	numCell.innerText = i;
	let nama_beasiswaCell = document.createElement('td');
	nama_beasiswaCell.innerText = namabeasiswa;
	let nama_penyediaCell = document.createElement('td');
	nama_penyediaCell.innerText = namapenyedia;
	let dateCell = document.createElement('td');
	dateCell.innerText = date;
	let statusCell = document.createElement('td');
	statusCell.innerText = status;
	let row = document.createElement('tr');
	row.appendChild(numCell);
	row.appendChild(nama_beasiswaCell);
	row.appendChild(nama_penyediaCell);
	row.appendChild(dateCell);
	row.appendChild(statusCell);

	let table = document.getElementById('statuses');
	table.appendChild(row);
};

const loadData = async () => {
	let username = window.localStorage.getItem('username')
	let result1 = await fetch('http://3.227.193.57:9000/mahasiswa/map/username/' +username);
	let nim = await result1.json();
	for(let item of nim){
		let nims = item.nim;
		console.log(nims);

		let result2 = await fetch('http://3.227.193.57:9000/pilihanbeasiswa/nim/' +nims);
		let hasil = await result2.json();

		for (let item of hasil) {
		    console.log(item.nim);
		    if (item.nim == nims) {
				let table = document.getElementById('statuses');
				table.innerHTML = '';
				let i = 1;
				for (let data of hasil) {
					createRow(i, data.nama_beasiswa, data.nama_penyedia, data.waktu_submit, data.status_seleksi);
					i++;
				}
			}
		}
	}
};