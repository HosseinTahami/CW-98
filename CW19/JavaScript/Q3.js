function storeUsername() {
    let username = prompt("Enter your username:");
    document.cookie = `username=${username}; expires=Thu, 18 Dec 2024 12:00:00 UTC; path=/"`;
    let usernameCookie = document.cookie;
    greetUser(usernameCookie);
  }

function greetUser(usernameCookie) {
    let splitCookie = usernameCookie.split(';');
    alert(`Welcome ${splitCookie[0]}`);
}

storeUsername();
