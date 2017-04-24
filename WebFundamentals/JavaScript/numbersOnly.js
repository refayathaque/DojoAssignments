function numbersOnly(arr) {
  var new_arr = [];
  for (var i = 0; i < arr.length; i++) {
    if (typeof arr[i] === "number") {
      new_arr.push(arr[i])
    }
    else {
      console.log(arr[i] + ' is not number!');
    }
  }
  console.log(new_arr);
}
numbersOnly([1, 2, 3, 'nissan', true, 4, [6, 3, 4], undefined, 6, 'audi']);
