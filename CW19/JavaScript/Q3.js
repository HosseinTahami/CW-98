function storeUsername() {
    let username = prompt("Enter your username:");
    if (!greetUser(document.cookie)) {
      document.cookie = `username=${username};`
    }
    else{
      if (username === greetUser(document.cookie)){
        alert('Welcome back')
      }
      else{
        alert(`Welcome ${username}`)
        document.cookie = `username=${username};`
      }
    }
    //greetUser(document.cookie);
  }

function greetUser(usernameCookie) {
    let splitCookie = usernameCookie.split(';');
    let finalUsername = splitCookie[0].substring('username='.length);
    return finalUsername
    //alert(`Welcome ${finalUsername}`);
}

storeUsername();
