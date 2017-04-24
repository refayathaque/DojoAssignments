function randomChance(quarters) {
  var win = Math.trunc(Math.random()*100);
  for(var x = quarters; x > 0; x--) {
    var chance = Math.trunc(Math.random()*100);
  if(chance === win) {
    quarters += Math.trunc(Math.random()*50)+50;
    console.log('You won! And you have ' + quarters + ' quarters');
  }
  else {
    console.log('You did not win');
  }
}
console.log('You are out of quarters');
}
randomChance(100);
