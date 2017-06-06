var Todd = {
    name : "Todd",
    sayName : function() {
        console.log("Todd");
    }
}

Todd.sayName();

// Object CONSTRUCTOR
function NewPerson(name) {
    return {
        name : name,
        sayName : function() {
            console.log(name);
        }
    }
}

var Jay = NewPerson('Jay');
var Sara = NewPerson('Sara');

Jay.sayName();
Sara.sayName();

function Person(name) {
    console.log(this);
    this.name = name;
    this.sayName = function() {
        console.log(name);
    }
}

var Jimmy = new Person('Jimmy');
Jimmy.sayName();

console.log('--------------------------');
console.log('--------------------------');

// OBJECT CONSTRUCTOR

function NinjaConstructor(name, age, prevOccupation) {
    var ninja = {}; // Will be population by key/value pairs of all information on what we'll be instantiating (OBJECT we will RETURN)
    // Addition of properties to ninja
    ninja.name = name;
    ninja.age = age;
    ninja.prevOccupation = prevOccupation;
    // Addition of methods to ninja
    ninja.introduce = function() {
        console.log("My name is " + ninja.name + ". I used to be a " + prevOccupation + ", and now I am a Ninja.")
    }
    // Return ninja
    return ninja;
}

// INSTANTIATING NINJAS

var Andrew = NinjaConstructor('Andrew', 24, 'Teacher');
console.log(Andrew);
Andrew.introduce();

var Michael = NinjaConstructor('Michael', 34, 'Founder');
console.log(Michael);
Michael.introduce = function() { // Redefining MICHAEL'S 'introduce' method in the Constructor
    console.log("I am the sensei!")
}
Michael.introduce();
