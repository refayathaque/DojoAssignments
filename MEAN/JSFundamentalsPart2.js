// Create a simple for loop that sums all the integers between x and y (inclusive). Have it console log the final sum.

function sum_between_x_and_y(x, y) {
    var sum = 0;
    for ( var i = x; i <= y; i++ ) {
        sum += i;
    }
    console.log(sum);
}

sum_between_x_and_y(4, 6);

// Write a loop that will go through an array, find the minimum value, and then return it

function minimum_in_array(array) {
    var min = array[0];
    for ( var i = 0; i < array.length; i++ ) {
        if (min > array[i]) {
            min = array[i];
        }
    }
    return min;
}

console.log(minimum_in_array([1, 2, 3, 6, -8, -6]));

// Write a loop that will go through an array, find the average of all of the values, and then return it

function average_of_array(array) {
    var sum = 0;
    for ( var i = 0; i < array.length; i++ ) {
        sum += array[i];
    }
    return sum / array.length
}

console.log(average_of_array([1, 2, 3, 4, 5]));

// Rewrite these 3 as anonymous functions assigned to variables.

var sumXY = function(x, y) {
    var sum = 0;
    for ( var i = x; i <= y; i++ ) {
        sum += i;
    }
    return sum;
}

var findMin = function findMin(array) {
    if (array) {
    var min = array[0];
    for ( var i = 0; i < array.length; i++ ) {
        if (min > array[i]) {
            min = array[i];
        }
    }
    return min;
    }
}

var findAvg = function(array) {
    var sum = 0;
    for ( var i = 0; i < array.length; i++ ) {
        sum += array[i];
    }
    return sum / array.length
}

// Rewrite these as methods of an object

var object = {
    sumXY: function(x, y) {
        var sum = 0;
        for ( var i = x; i <= y; i++ ) {
            sum += i;
        }
        return sum;
    },
    findMin: function findMin(array) {
        if (array) {
        var min = array[0];
        for ( var i = 0; i < array.length; i++ ) {
            if (min > array[i]) {
                min = array[i];
            }
        }
        return min;
        }
    },
    findAvg: function(array) {
        var sum = 0;
        for ( var i = 0; i < array.length; i++ ) {
            sum += array[i];
        }
        return sum / array.length
    }
}

// Create a JavaScript object called person with the following properties/methods

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
    },
    run: function() {
        person.distance_traveled += 10;
        console.log(person.name + ' is running, and his distance traveled is ' + person.distance_traveled);
    },
    crawl: function() {
        person.distance_traveled += 1;
        console.log(person.name + ' is crawling, and his distance traveled is ' + person.distance_traveled);
    }
}

person.say_name();
person.say_something("I am cool");
person.walk();
person.run();
person.crawl();
