function printRange(startpoint, endpoint, skipamount) {
  for(var x = startpoint; x < endpoint; x += skipamount) {
    console.log(x);
  }
}

printRange(0, 20, 4);
