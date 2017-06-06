var JSLibrary = {
   map: function(arr, callback) {
     for (var i = 0; i < arr.length; i++) {
         arr[i] = callback(arr[i]);
     }
     return arr;
   },
   reduce: function(arr, callback, memo) {
       for (var i = 0; i < arr.length; i++) {
           memo = callback(memo, arr[i]);
       }
       return memo;
   },
   find: function(arr, callback) {
     for (var i = 0; i < arr.length; i++) {
         if (callback(arr[i])) {
             return arr[i];
         }
     }
   },
   filter: function(arr, callback) {
      var tempArr = [];
      for (var i = 0; i < arr.length; i++) {
          if (callback(arr[i])) {
              tempArr.push(arr[i]);
          }
      }
      return tempArr;
   },
   reject: function(arr, callback) {
     var tempArr = [];
     for (var i = 0; i < arr.length; i++) {
         if (!callback(arr[i])) {
             tempArr.push(arr[i]);
         }
     }
     return tempArr;
   }
}

a = JSLibrary.map([1, 2, 3],
    function(num) {
                    return num * 5
                }
);
console.log(a);

b = JSLibrary.reduce([1, 2, 3],
    function(memo, num) {
                    return memo + num
                },
                0
);
console.log(b);

c = JSLibrary.find([1, 2, 3, 15],
    function(num) {
                    return num == 15
                }
);
console.log(c);

d = JSLibrary.filter([1, 2, 3, 15],
    function(num) {
                    return num > 12
                }
);
console.log(d);

e = JSLibrary.reject([1, 2, 3, 4, 5, 6, 7, 8, 9],
    function(num) {
                    return num % 2 == 0
                }
);
console.log(e);
