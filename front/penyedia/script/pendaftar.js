const createRow = (i, name, status) => {
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
  statusInput.checked = status === "Diterima";
  statusCell.appendChild(statusInput);
  let row = document.createElement('tr');
  row.appendChild(numCell);
  row.appendChild(nameCell);
  row.appendChild(statusCell);

  let table = document.getElementById('table-body');
  table.appendChild(row);
};

const loadData = async () => {
  let result = await fetch('http://3.227.193.57:9000/pilihanbeasiswa/id/' + window.localStorage.getItem('id'));
  let json = await result.json();
  let table = document.getElementById('table-body');
  table.innerHTML = '';
  let i = 1;
  for (let data of json) {
    createRow(i, data.nim, data.status_seleksi);
    i++;
  }
};

const acceptPendaftar = async () => {
  let table = document.getElementById('table-body');
  let rows = table.getElementsByTagName('tr');
  let id = window.localStorage.getItem('id');

  for (let r of rows) {
    let nameCell = r.getElementsByClassName('name')[0];
    let statusCell = r.getElementsByClassName('status')[0];
    let statusInput = statusCell.getElementsByTagName('input')[0];
    let nim = nameCell.innerText;

    await fetch(`http://3.227.193.57:9000/pilihanbeasiswa/id/${id}/nim/${nim}`, {
      method: 'PUT',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({"status_seleksi": statusInput.checked ? "Diterima" : "Ditolak"})
    })
  }

  await loadData();
};


