//String: Get Digits pg. 51 //05.11.17 Practiced

var string_thing = '12&gh3#!5hd32'

function getDigits(str) { //defines function
  var new_string = ""; //declares empty new_string variable
  for(var i = 0; i < str.length; i++) { //for loops over characters in string
    if(parseInt(str[i]) || parseInt(str[i]) === 0) { //checks for numbers AND zeroes,
                                                     //zeroes are 'falsey', so are NaNs
      new_string += str[i] //(new_string = new_string + str[i]) CONCATENATES,
                           //populates new_string with ONLY string's numbers
    }
  }
  return(Number(new_string)); //converts new_string to number and returns
}

var new_number = getDigits(string_thing)
console.log(new_number); //Outputs 123532
