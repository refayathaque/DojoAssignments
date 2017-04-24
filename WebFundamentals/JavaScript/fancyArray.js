function fancyArray(arr, symbol, reversed = false) { //Default value in case
                                                //user forgets to input 'false'
  if (reversed === true) {
    for(var x = arr.length - 1; x >= 0; x--) {
    console.log(x + " " + symbol + " " + arr[x]);
    }
  }
  else {
    for(var x = 0; x < arr.length; x++) {
    console.log(x + " " + symbol + " " + arr[x]);
    }
  }
}
fancyArray(["James", "Jill", "Jane", "Jack"], "->", true);
