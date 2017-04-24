function servantsReward() {
  var total = 0.01;
  for(var x = 0; x < 30; x++) {
    total *= 2;
  }
  console.log(total);
}
servantsReward();

console.log('----');

//Days to make 10,000
function servantsReward1() {
  var total1 = 0.01;
  for(var i = 0; i < 30; i++) {
    if (total1 > 10000) {
      break;
    }
    else {
      total1 *= 2;
    }
  }
  console.log(total1);
  console.log(i);
}
servantsReward1();

console.log('----');

//Days to make 1,000,000,000
function servantsReward2() {
  var total2 = 0.01;
  for(var y = 0; y >= 0; y++) {
    if (total2 > 1000000000) {
      break;
    }
    else {
      total2 *= 2;
    }
  }
  console.log(total2);
  console.log(y);
}
servantsReward2();

console.log('----');
