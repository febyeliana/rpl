const inputForm = async () => {
  let username = window.localStorage.getItem('username');
  console.log(username);

  let nimElem = $('nim');
  let emailElem = $('email');
  let passwordElem = $('password');
  let namaElem = $('nama');
  let no_teleponElem = $('no_telepon');
  let usiaElem = $('usia');
  let jurusanElem = $('jurusan');
  let semesterElem = $('semester');  
  let gpaElem = $('gpa');
  let pendapatanElem = $('pendapatan');
  let berkasElem = $('berkas');
  let usernameElem = username;



  await fetch(`http://3.227.193.57:9000/mahasiswa`, {
    method: 'POST',
    mode:'cors',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      "username": username,
      "nim": nimElem.value, 
      "email": emailElem.value,
      "password": passwordElem.value, 
      "nama": namaElem.value, 
      "no_telepon": no_teleponElem.value, 
      "usia": parseInt(usiaElem.value),
      "jurusan": jurusanElem.value, 
      "semester": semesterElem.value,
      "gpa": parseFloat(gpaElem.value), 
      "pendapatan": parseInt(pendapatanElem.value),
      "berkas": berkasElem.value,
    })
  })
  let urlPart = window.location.href.split('/');
    window.location = urlPart.splice(0, urlPart.length-1).join('/') + '/infomahasiswa.html';
    return;       
};