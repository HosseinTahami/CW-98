log = document.getElementById('log')
log.addEventListener('submit', function(event){
    let username = log.username.value
    let passwod = log.password.value
    isRememberMe = document.getElementById('RememberMe')

    if (isRememberMe.checked) {
        document.cookie = `username=${username}; password=${passwod}`;
    }
})