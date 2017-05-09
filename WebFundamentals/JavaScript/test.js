var string_thing = '12&gh3#!5hd32'

function getDigits(str) { //define a function
  var new_string = ""; //declare a new string variable
  for(var i = 0; i < str.length; i++) { //for loop over elements in the string
    if(parseInt(str[i]) || parseInt(str[i]) === 0) { //checking for numbers and zeroes, zeroes are 'falsey' so are NaNs
      new_string += str[i] //new_string = new_string + str[i] CONCATENATING //building new string
                          //of just numbers (still string numbers)
    }
  }
  return(Number(new_string)); //convert new_string to number and return
}

var new_number = getDigits(string_thing)
console.log(new_number);
