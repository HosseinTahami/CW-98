function storeUsername() {
    let username = prompt("Enter your username:");
    document.cookie = `username=${username};`;
    let usernameCookie = document.cookie;
    greetUser(usernameCookie);
  }

function greetUser(usernameCookie) {
    let splitCookie = usernameCookie.split(';');
    alert(`Welcome ${splitCookie[0]}`);
}

storeUsername();
