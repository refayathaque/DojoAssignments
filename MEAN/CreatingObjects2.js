function VehicleConstructor(name, wheels, pax, speed) {

    if (!(this instanceof VehicleConstructor)) {
        return new VehicleConstructor(name, wheels, passengerNumber, speed);
    }

    var self = this;
    // Private Variables and Methods
    var distance_travelled = 0;
    function updateDistanceTravelled() {
        distance_travelled += self.speed; // Allows private vars to access public vars...see 'var self = this;'
        console.log(distance_travelled);
    }
    //
    this.name = name || "Train"; // Default values
    this.wheels = wheels || 32;
    this.pax = pax || 500;
    this.speed = speed || 300;
    this.makeNoise = function() {
        console.log('HONK!');
    }
    this.move = function() {
        updateDistanceTravelled(); // No 'this' since it's a private method
        this.makeNoise();
    }
    this.checkMiles = function() {
        return distance_travelled; // PUBLIC way to view PRIVATE var, but still cannot alter 'distance_travelled' value, only way to alter is by calling 'move', which invokes the private method
    }
}

var bus = new VehicleConstructor('Bus', 8, 35, 60);
console.log(bus.checkMiles()); // 0
bus.move(); // Alters 'distance_travelled' because it invokes PRIVATE method
console.log(bus.checkMiles()); // 60

// var Bike = new VehicleConstructor('Bike', 2, 1, 200);
//
// Bike.makeNoise = function() {
//     console.log("RING RING!")
// }
// Bike.makeNoise();
//
// var Sedan = new VehicleConstructor('Sedan', 4, 5, 120);
//
// Sedan.makeNoise = function() {
//     console.log("HONK HONK!")
// }
// Sedan.makeNoise();
//
// var Bus = new VehicleConstructor('Bus', 6, 20, 60);
//
// Bus.pick_up_pax = function(new_pax) {
//     var total_pax_count = this.pax;
//     total_pax_count += new_pax;
//     return total_pax_count;
// }
//
// console.log(Bus);
// console.log(Bus.pick_up_pax(13)); // 33
//
// Bike.checkMiles();
// Bike.move();
