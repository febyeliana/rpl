const login = async () => {
  let username = document.getElementById('username').value;
  let password = document.getElementById('password').value;

  let response = await fetch('http://3.227.193.57:9000/mahasiswa/login');
  let data = await response.json();

  for (let item of data) {
    if (item.username === username && item.password === password) {
      console.log(item.username);
      let cekform = await fetch('http://3.227.193.57:9000/mahasiswa/map/username/' + item.username);
      let checking = await cekform.json();

      for(let item of checking){ 
        if(item.Message ==="Form empty" || item.nim === null){
          let urlPart1 = window.location.href.split('/');
          window.location = urlPart1.splice(0, urlPart1.length-1).join('/') + '/form.html';
          window.localStorage.setItem('username', username);
          window.localStorage.setItem('password', password);
          return;
        }
        else{
          let urlPart2 = window.location.href.split('/');
          window.location = urlPart2.splice(0, urlPart2.length-1).join('/') + '/infomahasiswa.html';
          window.localStorage.setItem('username', username);
          window.localStorage.setItem('password', password);
          return;
        }
      }
    }
  }
  alert("Invalid login!")
};