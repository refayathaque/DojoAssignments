var dictionary = require('./dictionary.js');
function search(word, dictionary) {
  for(w in dictionary) {
    if(dictionary[w] == word) {
        console.log(word, ' is in the dictionary')
        return true;
    }
  }
  console.log(word, ' is NOT in the dictionary');
  return false;
}

search('horse', dictionary);
