var hour = 4;
var minute = 5;
var period = 'AM';

if (minute < 30 && minute !== 5 && minute !== 15) {
  if (period === 'AM') {
    if (minute < 10) {
      console.log('The time is ' + hour +':0' + minute + ' ' + period + '. So it is just after ' + hour + ' in the morning.')
    }
    else {
      console.log('The time is ' + hour +':' + minute + ' ' + period + '. So it is just after ' + hour + ' in the morning.')
    }
  }
  else {
    if (minute < 10) {
      console.log('The time is ' + hour +':0' + minute + ' ' + period + '. So it is just after ' + hour + ' in the evening.')
    }
    else {
      console.log('The time is ' + hour +':' + minute + ' ' + period + '. So it is just after ' + hour + ' in the evening.')
    }
  }
}
else if (minute > 30) {
  if (period === 'AM') {
    console.log('The time is ' + hour +':' + minute + ' ' + period + '. So it is almost ' + (hour + 1) + ' in the morning.')
  }
  else {
    console.log('The time is ' + hour +':' + minute + ' ' + period + '. So it is almost ' + (hour + 1) + ' in the evening.')
  }
}
else if (minute === 30) {
  if (period === 'AM') {
    console.log('The time is ' + hour +':' + minute + ' ' + period + '. So it is half past ' + hour + ' in the morning.')
  }
  else {
    console.log('The time is ' + hour +':' + minute + ' ' + period + '. So it is half past ' + hour + ' in the evening.')
  }
}
else if (minute === 15) {
  if (period === 'AM') {
    console.log('The time is ' + hour +':' + minute + ' ' + period + '. So it is quarter after ' + hour + ' in the morning.')
  }
  else {
    console.log('The time is ' + hour +':' + minute + ' ' + period + '. So it is quarter after ' + hour + ' in the evening.')
  }
}
else if (minute === 5) {
  if (period === 'AM') {
    console.log('The time is ' + hour +':0' + minute + ' ' + period + '. So it is five after ' + hour + ' in the morning.')
  }
  else {
    console.log('The time is ' + hour +':0' + minute + ' ' + period + '. So it is five after ' + hour + ' in the evening.')
  }
}
