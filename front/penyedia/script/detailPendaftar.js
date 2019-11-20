let $ = (id) => document.getElementById(id);

const getProfileById = async () => {
  let nim = window.localStorage.getItem('nim');
  console.log(nim);
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