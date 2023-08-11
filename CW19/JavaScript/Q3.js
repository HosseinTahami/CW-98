function storeUsername() {
    let username = prompt("Enter your username:");
    document.cookie = `username=${username}`;
    greetUser();
  }

