const createRow = (i, name, startDate, closeDate, total) => {
  let nameCell = document.createElement('td');
  nameCell.innerText = name;
  nameCell.className = "name";

  let numCell = document.createElement('td');
  numCell.innerText = i;

  let startDateCell = document.createElement('td');
  startDateCell.innerText = startDate;
  startDateCell.className = "startDate";

  let closeDateCell = document.createElement('td');
  closeDateCell.innerText = closeDate;
  closeDateCell.className = "closeDate";

  let totalCell = document.createElement('td');
  totalCell.innerText = total;
  totalCell.className = "total";

  let row = document.createElement('tr');
  row.appendChild(numCell);
  row.appendChild(nameCell);
  row.appendChild(startDateCell);
  row.appendChild(closeDateCell);
  row.appendChild(totalCell);

  let table = document.getElementById('table-body');
  table.appendChild(row);
};

const loadData = async () => {
  let result = await fetch('http://3.227.193.57:9000/beasiswa/riwayat/id/' + window.localStorage.getItem('id'));
  let json = await result.json();
  let table = document.getElementById('table-body');
  table.innerHTML = '';
  let i = 1;
  for (let data of json) {
    createRow(i, data.nama, data.waktu_buka, data.waktu_tutup, data.jumlah_pendaftar);
    i++;
  }
};

/*
const acceptPendaftar = async () => {
  let table = document.getElementById('table-body');
  let rows = table.getElementsByTagName('tr');
  let id = window.localStorage.getItem('id');

  for (let r of rows) {
    let nameCell = r.getElementsByClassName('name')[0];
    let dateCell = r.getElementsByClassName('date')[0];
    let dateInput = dateCell.getElementsByTagName('input')[0];
    let nim = nameCell.innerText;

    await fetch(`http://3.227.193.57:9000/pilihanbeasiswa/id/${id}/nim/${nim}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({"date_seleksi": dateInput.checked ? "Diterima" : "Ditolak"})
    })
  }

  await loadData();
};
*/

