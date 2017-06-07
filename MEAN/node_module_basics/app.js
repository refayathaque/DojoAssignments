// var my_module = require('./my_module');
// my_module.greet();
// my_module.add(5, 6);

// Requiring a Node module allows you to use the module.exports object of another file!

// Normally, the require() method looks for node modules that AREN'T in the same directory as the file that is running; by default, the require() method looks for the modules located in a folder called NODE_MODULES.

// To tell require() to look in the current directory (i.e. the folder that the file is located in) we have to include "./" in front of the file path. "./" (DOT-SLASH) is the file path for the CURRENT DIRECTORY.

var my_module = require('./my_module')();     //notice the extra invocation parentheses!
console.log(my_module);
my_module.greet();
my_module.add(5, 6);
