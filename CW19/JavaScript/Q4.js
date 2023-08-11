let button = document.getElementById("myButton");
let element = document.getElementById("myElement");

button.addEventListener("click", function() {
    let text = element.textContent;
    console.log(text);
});