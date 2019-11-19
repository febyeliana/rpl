let $ = (id) => document.getElementById(id);

const getProfile = async () => {
  let result = await fetch('http://3.227.193.57:9000/penyedia');
  let data = await result.json();
  let username = window.localStorage.getItem('username');

  for (let item of data) {
    console.log(item.nama);
    if (item.nama.toLowerCase() === username) {
      let namaElem = $('nama');
      let emailElem = $('email');
      let alamatElem = $('alamat');
      let teleponElem = $('telepon');
      let webElem = $('web');

      namaElem.innerText = item.nama;
      emailElem.innerText = item.email;
      teleponElem.innerText = item.no_telepon;
      alamatElem.innerText = item.alamat;
      webElem.innerText = item.website;
      window.localStorage.id = item.id_penyedia;
      
      return;
    }
  }
};

const getProfileById = async () => {
  let id = window.localStorage.getItem('id');
  let result = await fetch('http://3.227.193.57:9000/penyedia/id/' + id);
  let json = await result.json();
  let item = json[0];

  let namaElem = $('nama');
  let emailElem = $('email');
  let alamatElem = $('alamat');
  let teleponElem = $('telepon');
  let webElem = $('web');

  namaElem.value = item.nama;
  emailElem.value = item.email;
  teleponElem.value = item.no_telepon;
  alamatElem.value = item.alamat;
  webElem.value = item.website;
};

const updateProfile = async () => {
  let namaElem = $('nama');
  let emailElem = $('email');
  let alamatElem = $('alamat');
  let teleponElem = $('telepon');
  let webElem = $('web');
  let id = window.localStorage.getItem('id');
  await fetch(`http://3.227.193.57:9000/penyedia/id/${id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({"nama": namaElem.value,
      "email": emailElem.value, 
      "no_telepon": teleponElem.value, 
      "alamat":alamatElem.value, 
      "website": webElem.value})
  })
  let urlPart = window.location.href.split('/');
      window.location = urlPart.splice(0, urlPart.length-1).join('/') + '/profil.html';
};