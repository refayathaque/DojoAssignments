var math_module = require('./mathlib.js')();
//extra invocation bc of mathlib.js is a function that RETURNS an OBJECT
console.log(math_module);
math_module.add(3, 4);
math_module.multiply(3, 4);
math_module.square(3);
math_module.random(1, 10);
