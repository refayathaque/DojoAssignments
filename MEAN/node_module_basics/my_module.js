// module.exports = {
//     greet: function(){
//         console.log("we are now using a module!");
//     },
//     add: function(num1, num2){
//         console.log("the sum is:", num1 + num2);
//     }
// }

// Requiring a Node module allows you to use the module.exports object of another file!

module.exports = function(){
    return {
        greet: function(){
            console.log("we are now using a module!");
        },
        add: function(num1, num2){
            console.log("the sum is:", num1 + num2);
        }
    }
}
