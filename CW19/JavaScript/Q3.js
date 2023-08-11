function storeUsername() {
    let username = prompt("Enter your username:");
    document.cookie = username;
    let usernameCookie = document.cookie;
    greetUser(usernameCookie);
  }

function greetUser(usernameCookie) {
    alert(`Welcome ${usernameCookie}`);
}

storeUsername();
