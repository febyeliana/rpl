function createRow(i, name, description, apply) {
			let nameCell = document.createElement('td');
			nameCell.innerText = name;
			let numCell = document.createElement('td');
			numCell.innerText = i;
			let descriptionCell = document.createElement('td');
			descriptionCell.innerText = description;
			let applyCell = document.createElement('td');
  			applyCell.className = "apply";
  			let applyInput = document.createElement('input');
			applyInput.type = "checkbox";
			applyInput.name = "apply";
			console.log(apply);
			applyInput.checked = status === "Applied";
			applyCell.appendChild(applyInput);
			let row = document.createElement('tr');
			row.appendChild(numCell);
			row.appendChild(nameCell);
			row.appendChild(descriptionCell);
			row.appendChild(applyCell);

			let table = document.getElementById('bea');
			table.appendChild(row);
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
		createRow(i, data.nama, data.deskripsi, data.ketersediaan );
		i++;
	}
}