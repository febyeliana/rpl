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
		"nama": document.getElementById('nama').innerText,
	  	"waktu_buka": parseInt(bukaElem.innerText), 
	  	"waktu_tutup": parseInt(tutupElem.innerText), 
	  	"deskripsi": deskripsiElem.innerText, 
	  	"min_gpa": parseFloat(minElem.innerText),
	  	"semester": parseInt(minSemElem.innerText), 
	  	"batas_semester": parseInt(document.getElementById('max_sem').innerText),
	  	"fakultas": fakultasElem.innerText, 
	  	"jurusan": jurusanElem.innerText,
	  	"tipe": tipeElem.innerText
	  })

  })
}