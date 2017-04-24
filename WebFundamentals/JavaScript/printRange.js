function printRange(startPnt = 0, endPnt = 10, skipAmt = 1) { //Added default
                                                        //function parameters
  if (endPnt > 0) {
    for(var x = startPnt; x < endPnt; x += skipAmt) {
      console.log(x);
    }
  }
  else {
    for(var x = startPnt; x > endPnt; x -= skipAmt) {
      console.log(x);
    }
  }
}
printRange(-3, -12, 2);
