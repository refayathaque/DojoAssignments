function random_color() {
   var rgb = ['a','b','c','d','e','f','0','1','2','3','4','5','6','7','8','9']; //array of strings, numbers also strings bc of
                                                                                //'appending' below
   color = '#' //this is what we'll return! must 'append' to #
   for(var i = 0; i < 6; i++) { //hexadecimal(6) color for loop, that's why conditional < 6
      x = Math.floor((Math.random()*16)) //16 bc that's array rgb.length, will give random value from 0 to 15
                                         //Math.floor() function returns the largest integer LESS than or equal to a given number
                                         //can also use Math.trunc here, since must round DOWN to ensure nothing higher than 15
      color += rgb[x]; } //'appending' to color var's # above
   console.log(color);
}
random_color();
