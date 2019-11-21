let $ = (nim) => document.getElementById(nim);

const getProfile = async () => {
  let username = window.localStorage.getItem('username')
  let result1 = await fetch('http://3.227.193.57:9000/mahasiswa/map/username/' +username);
  let nim = await result1.json();
  for(let item of nim){
    let nims = item.nim;
    console.log(nims);

    let result2 = await fetch('http://3.227.193.57:9000/mahasiswa/nim/' +nims);
    let data = await result2.json();

 
    for (let item of data) {
      console.log(item.nim);
      if (item.nim == nims) {
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

        nimElem.innerText = item.nim;
        emailElem.innerText = item.email;
        passwordElem.innerText = item.password;
        namaElem.innerText = item.nama;
        no_teleponElem.innerText = item.no_telepon;
        usiaElem.innerText = item.usia;
        jurusanElem.innerText = item.jurusan;
        semesterElem.innerText = item.semester;
        gpaElem.innerText = item.gpa;
        pendapatanElem.innerText = item.pendapatan;
        berkasElem.innerText = item.berkas;
        window.localStorage.nim = item.nim;
      
        return;
      }
    }
  }
};

const getProfileByNim = async () => {
  let nim = window.localStorage.getItem('nim');
  let result = await fetch('http://3.227.193.57:9000/mahasiswa/nim/' + nim);
  let json = await result.json();
  let item = json[0];

  let nimElem = $('nim');
  let namaElem = $('nama');
  let emailElem = $('email');
  let usiaElem = $('usia');

  nimElem.value = item.nim;
  namaElem.value = item.nama;
  emailElem.value = item.email;
  usiaElem.value = item.usia;
};

const updateProfile = async () => {
  let namaElem = $('nama');
  let nimElem = $('nim');
  let emailElem = $('email');
  let usiaElem = $('usia');
  let nim = window.localStorage.getItem('nim');
  await fetch(`http://3.227.193.57:9000/mahasiswa/nim/${nim}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      "nama": namaElem.value,
      "nama": namaElem.value, 
      "email": email.value, 
      "usia":usia.value
  })
  })
  let urlPart = window.location.href.split('/');
      window.location = urlPart.splice(0, urlPart.length-1).join('/') + '/infomahasiswa.html';
};