function FizzBuzz() {
    for ( var i = 1; i < 101; i++ ) {
        if ( i % 2 === 0 && i % 3 === 0 ) {
            console.log('FizzBuzz');
        }
        else if ( i % 2 === 0 ) {
            console.log('Fizz');
        }
        else if ( i % 3 === 0 ) {
            console.log('Buzz');
        }
        else {
            console.log(i);
        }
    }
}

FizzBuzz();

console.log('---------------------')

function SkipNum() {
    for ( var i = 10; i > 0; i--) {
        if ( i % 2 === 0 ) {
            console.log(i)
        }
    }
}

SkipNum();

function SkipNum2() {
    for ( var i = 10; i > 0; i = i - 2) {
        console.log(i);
    }
}

console.log('---------------------')

SkipNum2();
