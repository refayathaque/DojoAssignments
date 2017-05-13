function validParens(str){
  var countOpen = 0;
  for (var i = 0; i < str.length; i++) {
    if(str[i] == "(") {
      countOpen++;
    }
    if(str[i] == ")") {
      countOpen--;
      if(countOpen < 0) return false //single return statements don't need {}s!
    }
  }
  // if(countOpen == 0) return true
  // else return false
  return countOpen == 0 //new way to do if/else statements, examples ^ & below
  // return countOpen == 0 ? true : false //ternary operator!
}
console.log(validParens("(hello))"));
