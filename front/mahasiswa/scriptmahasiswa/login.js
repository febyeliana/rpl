const login = async () => {
  let username = document.getElementById('username').value;
  let password = document.getElementById('password').value;

  let response = await fetch('http://3.227.193.57:9000/mahasiswa/login');
  let data = await response.json();

  for (let item of data) {
    if (item.username === username && item.password === password) {
      let cekform = await fetch('http://3.227.193.57:9000/mahasiswa/map/username/' + username)
      let checking = await cekform.json();

      for(item in checking){
        let obj = item.message;
        var pesan = JSON.stringify(obj); 
        if(pesan ==="form empty"){
          let urlPart = window.location.href.split('/');
          window.location = urlPart.splice(0, urlPart.length-1).join('/') + '/form.html';
          window.localStorage.setItem('username', username);
          window.localStorage.setItem('password', password);
          return;
        }
        else{
          let urlPart = window.location.href.split('/');
          window.location = urlPart.splice(0, urlPart.length-1).join('/') + '/infomahasiswa.html';
          window.localStorage.setItem('username', username);
          window.localStorage.setItem('password', password);
          return;
        }
      }
    }
  }
  alert("Invalid login!")
};