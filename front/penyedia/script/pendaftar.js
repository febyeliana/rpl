let tableCode = `<table class="tRiwayat">
      <thead>
        <tr>
          <th>No.</th>
          <th>Nama Pendaftar</th>
          <th>Terima</th>
        </tr>
      </thead>
      <tbody id="{}">
        <tr></tr>
      </tbody>
    </table>
    <a class="button" href="#" onclick="acceptPendaftar('{X}')">Publikasikan</a>`;
    
const createRow = (tableId, bea, i, name, status) => {
  let namaBea = document.createElement('td');
  namaBea.style.display = 'None';
  namaBea.innerText = bea;
  namaBea.className = "bea";
  let nameCell = document.createElement('td');
  nameCell.innerText = name;
  nameCell.className = "name";
  let numCell = document.createElement('td');
  numCell.innerText = i;
  let statusCell = document.createElement('td');
  statusCell.className = "status";
  let statusInput = document.createElement('input');
  statusInput.type = "checkbox";
  statusInput.name = "terima";
  console.log(status);
  statusInput.checked = status === "Diterima";
  statusCell.appendChild(statusInput);
  let row = document.createElement('tr');
  row.appendChild(namaBea);
  row.appendChild(numCell);
  row.appendChild(nameCell);
  row.appendChild(statusCell);
  //console.log(row);
  nameCell.addEventListener('click', () => detail(name));

  let table = document.getElementById(tableId);
  table.appendChild(row);
};

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

const acceptPendaftar = async (tableId) => {
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
      body: JSON.stringify({"status_seleksi": statusInput.checked ? "Diterima" : "Ditolak", "nama_beasiswa": beaCell.innerText})
    })
  }

  await loadData();
};

const detail = async (nim) => {
  let urlPart = window.location.href.split('/');
  window.location = urlPart.splice(0, urlPart.length-1).join('/') + '/detailPendaftar.html';

  window.localStorage.setItem('pendaftar', nim);
}

 //way0l0OOOOOlet $ = (id) => document.getElementById(id);

let $ = (id) => document.getElementById(id);

const getProfileById = async () => {
  let nim = window.localStorage.getItem('pendaftar');
  let result = await fetch('http://3.227.193.57:9000/mahasiswa/nim/' + nim);
  let json = await result.json();
  let item = json[0];

  let namaElem = $('nama');
  let nimElem = $('nim');
  let emailElem = $('email');
  let teleponElem = $('telepon');
  let usiaElem = $('usia');
  let jurusanElem = $('jurusan');
  let ipkElem = $('ipk');
  let semElem = $('sem');
  let uangElem = $('uang');
  let berkasElem = $('berkas');

  namaElem.innerText = item.nama;
  nimElem.innerText = item.nim;
  emailElem.innerText = item.email;
  teleponElem.innerText = item.no_telepon;
  usiaElem.innerText = item.usia;
  jurusanElem.innerText = item.jurusan;
  ipkElem.innerText = item.gpa;
  semElem.innerText = item.semester;
  uangElem.innerText = item.pendapatan;
  berkasElem.innerText = item.berkas;

};