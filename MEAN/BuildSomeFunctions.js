// Function 1

function runningLogger() {
    console.log('I am running');
}

runningLogger(); // I am running

// Function 2

function multiplyByTen(parameter) {
    var product = parameter * 10;
    return product;
}

console.log((multiplyByTen(5))); // 50

// Function 3

function stringReturnOne() {
    var stringOne = 'Returning String One';
    return stringOne;
}

function stringReturnTwo() {
    var stringTwo = 'Returning String Two';
    return stringTwo;
}

console.log(stringReturnOne()); // Returning String One
console.log(stringReturnTwo()); // Returning String Two

// Function 4

function caller(parameter) {
    if ( typeof(parameter) == 'function' ) {
        console.log('Argument invoked');
    }
    else {
        return null;
    }
}

function test() {
    var test = 'test';
    return test;
}

caller(test);
caller('Not a function');

// Function 5

function myDoubleConsoleLog(parameter1, parameter2) {
    if ( typeof(parameter1) == 'function' && typeof(parameter2) == 'function' ) {
        parameter1();
        parameter2();
    }
    else {
        return null;
    }
}

function function1() {
    console.log('hello');
}

function function2() {
    console.log('world')
}

myDoubleConsoleLog(function1, function2);

// Function 6

function caller2(parameter) {
    console.log('starting');
    setTimeout(functionbelow, 2000);
        function functionbelow() {
            if ( typeof(parameter) == 'function' ) {
                console.log('ending?');
                return 'interesting';
                }
        }
}

caller2(myDoubleConsoleLog);
