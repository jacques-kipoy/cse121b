/* W02-Task - Profile Home Page */

/* Step 1 - Setup type tasks - no code required */

/* Step 2 - Variables */
let fullName = "Jacques Kipoy";
const currentYear = new Date().getFullYear();
const profilePicture = "images/jacques_kipoy.jpg";


/* Step 3 - Element Variables */
//const nameElement = document.getElementById("#name")
//const nameElement = document.querySelector("#name")
const foodElement = document.querySelector("#food")  //block
const yearElement = document.querySelector("#year")
const imageElement = document.querySelector("img")

/* Step 4 - Adding Content */

//nameElement.innerHTML = <strong>${fullName}</strong>
yearElement.textContent = currentYear;
imageElement.setAttribute("src", profilePicture);
imageElement.setAttribute("alt",`This is ${fullName}, a student at BYU-Idaho`);


/* Step 5 - Array */
let favFoods = ["Apple", "Pineapple", "Watermelon", "Avocado", "Mango"];

//document.getElementById("food").innerHTML = favFoods;

foodElement.innerHTML = favFoods;
let newfood = "grapes";
favFoods.push(newfood);
foodElement.innerHTML += `<br>${favFoods}`;
favFoods.shift();
foodElement.innerHTML += `<br>${favFoods}`;
favFoods.pop()
foodElement.innerHTML += `<br>${favFoods}`;










