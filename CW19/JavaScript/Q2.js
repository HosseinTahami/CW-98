const age = prompt("Please enter your age:");

if (age >= 0 && age <= 10) {
  console.log("You are a child.");
} else if (age >= 11 && age <= 18) {
  console.log("You are a teenager.");
} else if (age >= 19 && age <= 30) {
  console.log("You are a young person.");
} else {
  console.log("You are an adult.");
}