function missing(array) {
    var min = array[0];
    for(var x = 0; x < array.length; x++) {
        if(array[x] < min) {
            min = array[x];
        }
    }
    for(var i = 0; i < array.length; i++) {
        if(array[i] === min + 1) {
            min = array[i];
            i = -1;
        }
    }
    return min + 1;
}

var z = missing([2, 1, -2, 0, -3]);
console.log(z);
