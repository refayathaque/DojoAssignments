// Create a function that takes in one parameter called “name” and returns an object that looks similar to the person object from JS Fundamentals Part II.

var person = {
    name: 'Refayat Haque',
    distance_traveled: 0,
    say_name: function() {
        console.log(person.name);
    },
    say_something: function(parameter) {
        console.log(person.name + ' says ' + parameter);
    },
    walk: function() {
        person.distance_traveled += 3;
        console.log(person.name + ' is walking, and his distance traveled is ' + person.distance_traveled);
        return person;
    },
    run: function() {
        person.distance_traveled += 10;
        console.log(person.name + ' is running, and his distance traveled is ' + person.distance_traveled);
        return person;
    },
    crawl: function() {
        person.distance_traveled += 1;
        console.log(person.name + ' is crawling, and his distance traveled is ' + person.distance_traveled);
        return person;
    }
}

person.say_name();
person.say_something("I am cool");
person.walk();
person.run();
person.crawl();

function ninjaConstructor(name, cohort) {
    var ninja = {}
    var belts = ["yellow", "red", "black"]
    ninja.name = name;
    ninja.cohort = cohort;
    ninja.beltLevel = 0;
    ninja.levelUp = function() {
        if ( ninja.beltLevel < 2 ) {
            ninja.beltLevel++;
            ninja.belt = belts[ninja.beltLevel];
        }
        return ninja;
    }
    ninja.belt = belts[ninja.beltLevel];
    console.log(ninja);
}

console.log(ninjaConstructor('Harry', 'Kappa'));
