// prototype, which is how objects in JavaScript share properties and methods.

function Cat( cat_name ) {
    var name = cat_name;
    this.getName = function() {
        return name;
    };
}

// adding a method to the cat prototype
// Format: ObjConstructor.prototype.methodName = function() {}
Cat.prototype.sayHi = function() {
    console.log('meow');
};

// adding properties to the cat prototype
Cat.prototype.numLegs = 4;

var muffin = new Cat('muffin');
var biscuit = new Cat('biscuit');

console.log(muffin, biscuit);

muffin.sayHi();
biscuit.sayHi();

console.log(muffin.numLegs);

muffin.__proto__.numLegs++; // doing this will mess up all the cats, see below

console.log(biscuit.numLegs); // incrementing muffin's numLegs with 'prototype' also incremented biscuit's numLegs to 5

var cookie = new Cat('cookie');
console.log(cookie.numLegs); // also 5

muffin.__proto__.sayHi = function() { // doing this will make ALL cats say 'bark' instead of 'meow'
    console.log('bark')
}

muffin.sayHi(); // bark
biscuit.sayHi(); // bark
