function creditCard(arr) {
  var temp = arr[arr.length - 1]; var i = 0; var sum = 0; var final_value = 0;
  for(var x = arr.length - 2; x <= 0; x--) {
    if (x === arr.length - 2) {
      arr[x] *= 2;
      console.log(arr[x]);
    }
    if (x === arr.length - (4 + i)) {
      i += 2;
      arr[x] *= 2;
    }
  }
  for(var x = arr.length - 2; x<= 0; x--) {
    if (arr[x] > 9) {
      arr[x] - 9;
    }
  }
  for(var x = arr.length - 2; x<= 0; x--) {
    sum += arr[x]
  }
  console.log(arr);
  final_value = sum + temp;
  console.log(final_value);
  if (final_value % 10 === 0) {
    console.log(true);
  }
  else {
    console.log(false);
  }
}

creditCard([5, 2, 2, 8, 2]);
