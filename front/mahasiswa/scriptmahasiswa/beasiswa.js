function createRow(i, name, description, apply) {
	let nameCell = document.createElement('td');
	nameCell.innerText = name;
	let numCell = document.createElement('td');
	numCell.innerText = i;
	let descriptionCell = document.createElement('td');
	descriptionCell.innerText = description;
	let applyCell = document.createElement('td');
	applyCell.innerText = document.createElement('button')
	let row = document.createElement('tr');
	row.appendChild(numCell);
	row.appendChild(nameCell);
	row.appendChild(descriptionCell);
	row.appendChild(applyCell);

	let table = document.getElementById('bea');
	table.appendChild(row);
}

async function loadData() {
	let result = await fetch('http://3.227.193.57:9000/beasiswa');
	let json = await result.json();
	let table = document.getElementById('bea');
	table.innerHTML = '';
	let i = 1;
	for (let data of json) {
		createRow(i, data.nama, data.deskripsi, data.ketersediaan, );
		i++;
	}
}