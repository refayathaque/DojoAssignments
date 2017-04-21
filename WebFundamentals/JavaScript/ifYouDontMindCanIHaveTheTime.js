var hour = 3;
var minute = 48;
var period = 'AM';

if (minute < 30) {
  if (period === 'AM') {
    console.log('The time is ' + hour +':' + minute + ' ' + period + '. So it is just after ' + hour + ' in the morning.')
  }
  else if (period === 'PM') {
    console.log('The time is ' + hour +':' + minute + ' ' + period + '. So it is just after ' + hour + ' in the evening.')
  }
}
else if (minute > 30) {
  if (period === 'AM') {
    console.log('The time is ' + hour +':' + minute + ' ' + period + '. So it is almost ' + (hour + 1) + ' in the morning.')
  }
  else if (period === 'PM') {
    console.log('The time is ' + hour +':' + minute + ' ' + period + '. So it is almost ' + (hour + 1) + ' in the evening.')
  }
}
