
var name = prompt("what is your name?");

console.log("your name is " + name);

function getRandomInt(int) {
  return Math.floor(Math.random() * int);
}

function isNumber(num) {
	return typeof num === 'number' && !isNaN(num);
}

var n = parseInt(prompt("write any number"));


while (!isNumber(n)) {
  n = parseInt(prompt("try again"));
  console.log(isNumber(n));
}

var num1 = getRandomInt(n);
var num2 = getRandomInt(n);
num1 += num2;
num2++;

let colors = new Array("Red", "Green", "Blue");

document.write(Math.PI + "<br>");
document.write(Math.ceil(2.01) + "<br>");
document.write(Math.floor(2.9) + "<br>");
document.write(Math.round(2.5) + "<br>");
document.write(Math.abs(-224) + "<br>");

document.write("number: ", num1 * num2);


document.write(colors[getRandomInt(3)]);


const _name = "Denys";
let age = 16;
let bool = true;

console.log(typeof _name + ":" + _name, typeof age + ":" + age);


const header = document.getElementById('header');
let links = document.querySelectorAll('.nav-link');

console.log(header, links);
