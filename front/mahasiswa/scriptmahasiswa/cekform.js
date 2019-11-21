const checkLogin =  (isLoggedIn) => {
  return async () => {
    let username = localStorage.getItem('username');
    let password = localStorage.getItem('password');

    let response = await fetch('http://3.227.193.57:9000/mahasiswa/login');
    let data = await response.json();

    for (let item of data) {
      if (item.username === username && item.password === password && isLoggedIn) {
        console.log('loggedIn');
        return;
      } else if (item.username === username && item.password === password && !isLoggedIn) {
        console.log('supposed not to be logged in')
        let urlPart = window.location.href.split('/');
        window.location = urlPart.splice(0, urlPart.length-1).join('/') + '/infomahasiswa.html';
        return;
      }
    }
    if (isLoggedIn) {
      let urlPart = window.location.href.split('/');
      window.location = urlPart.splice(0, urlPart.length-1).join('/') + '/login.html';
    }
  }
};