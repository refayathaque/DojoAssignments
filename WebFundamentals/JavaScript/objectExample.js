var glazedDonuts = [
  {
    frosting: 'glazed',
    style: 'cake',
    type: 'old fashioned',
    age: '45',
    time: 'minutes'
  },
  {
    frosting: 'glazed',
    style: 'yeast raised',
    type: 'regular',
    age: '5',
    time: 'minutes'
  },
  {
    frosting: 'glazed',
    style: 'yeast raised',
    type: 'jelly filled',
    age: '1',
    time: 'seconds'
  }
];
var numPurchase = 0;
for (var x = 0; x < glazedDonuts.length; x++) {
  if((glazedDonuts[x].age < 25 && glazedDonuts[x].time == 'minutes') || glazedDonuts[x].time == 'seconds'){
    numPurchase++;
  }
  else {
    console.log('not this donut...');
  }
}
console.log(numPurchase);
