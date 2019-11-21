let $ = (id) => document.getElementById(id);

const publikasi = async () => {
  let namaProgramElem = $('nama');
  let bukaElem = $('waktu_buka');
  let tutupElem = $('waktu_tutup');
  let fakultasElem = $('fakultas');
  let jurusanElem = $('jurusan');
  let minElem = $('min_gpa');
  let deskripsiElem = $('deskripsi');
  let maxSemElem = $('max_sem');  
  let minSemElem = $('min_sem');
  let tipeElem = $('tipe');


let id = window.localStorage.getItem('id');
  await fetch(`http://3.227.193.57:9000/beasiswa`, {
    method: 'POST',
    mode:'cors',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({"id_penyedia": parseInt(id), 
		"nama": document.getElementById('nama').value,
	  	"waktu_buka": parseInt(bukaElem.value), 
	  	"waktu_tutup": parseInt(tutupElem.value), 
	  	"deskripsi": deskripsiElem.value, 
	  	"min_gpa": parseFloat(minElem.value),
	  	"semester": parseInt(minSemElem.value), 
	  	"batas_semester": parseInt(document.getElementById('max_sem').value),
	  	"fakultas": fakultasElem.value, 
	  	"jurusan": jurusanElem.value,
	  	"tipe": tipeElem.value
	  })

  })

let urlPart = window.location.href.split('/');
window.location = urlPart.splice(0, urlPart.length-1).join('/') + '/publikasi.html';
}