//For Loop
function whileYouWait1(daysleft) {
  for(var x = daysleft; x >= 0; x--) {
    if (x >= 30) {
      console.log(x + ' days until my birthday. Such a long time... :(')
    }
    else if (x < 30 && x > 4) {
      console.log(x + ' days until my birthday. Almost there! :)')
    }
    else if (x <= 4 && x !== 0) {
      console.log(x + ' DAYS UNTIL MY BIRTHDAY!!!')
    }
    else {
      console.log('HAPPY BIRTHDAY TO ME!!! NO ONE CAN STOP ME NOW!!!')
    }
  }
}
whileYouWait1(60);

console.log('----');

//While Loop
function whileYouWait2(dayslefti) {
  var i = dayslefti;
  while (i >= 0) {
    if (i >= 30) {
      console.log(i + ' days until my birthday. Such a long time... :(')
      i--;
    }
    else if (i < 30 && i > 4) {
      console.log(i + ' days until my birthday. Almost there! :)')
      i--;
    }
    else if (i <= 4 && i !== 0) {
      console.log(i + ' DAYS UNTIL MY BIRTHDAY!!!')
      i--;
    }
    else {
      console.log('HAPPY BIRTHDAY TO ME!!! NO ONE CAN STOP ME NOW!!!')
      i--;
    }
  }
}
whileYouWait2(10);
