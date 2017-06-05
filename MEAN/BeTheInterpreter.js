// Problem 1

// console.log(first_variable);
// var first_variable = "Yipee I was first!";
// function firstFunc() {
//   first_variable = "Not anymore!!!";
//   console.log(first_variable);
// }
// console.log(first_variable);

var first_variable = "Yipee I was first!";

function firstFunc() {
    var first_variable = "Not anymore!!!";
    console.log(first_variable)
}

firstFunc(); // Not anymore
console.log(first_variable); // Yipee I was first!

// Problem 2

// var food = "Chicken";
// function eat() {
//   food = "half-chicken";
//   console.log(food);
//   var food = "gone";
//   console.log(food);
// }
// eat();
// console.log(food);

var food = "Chicken";

function eat() {
    var food = "half-chicken";
    console.log(food);
    food = "gone";
    console.log(food);
}

eat(); // half chicken, gone
console.log(food); // Chicken

// Problem 3

// var new_word = "NEW!";
// function lastFunc() {
//   new_word = "old";
// }
// console.log(new_word);

var new_word = "NEW!";

function lastFunc() {
    var new_word = "old";
    console.log(new_word);
}

lastFunc(); // old
console.log(new_word); // NEW!
