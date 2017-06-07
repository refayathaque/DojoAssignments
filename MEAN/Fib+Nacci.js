function fib() {
    var previous = 0;
    var current = 1;
    function nacci() {
        console.log(current)
        var temp = current;
        current += previous;
        previous = temp;
    }
    return nacci
}

var fibCounter = fib();

fibCounter()
fibCounter()
fibCounter()
fibCounter()
fibCounter()
fibCounter()
