function VehicleConstructor(name, num_wheels, num_pax) {
    var vehicle = {};
    vehicle.name = name;
    vehicle.num_wheels = num_wheels;
    vehicle.num_pax = num_pax;
    vehicle.makeNoise = function() {
        console.log('HONK!');
    }
    return vehicle;
}

var Bike = VehicleConstructor('Bike', 2, 1);
console.log(Bike);

Bike.makeNoise = function() {
    console.log("RING RING!")
}
Bike.makeNoise();

var Sedan = VehicleConstructor('Sedan', 4, 5);
console.log(Sedan);

Sedan.makeNoise = function() {
    console.log("HONK HONK!")
}
Sedan.makeNoise();

var Bus = VehicleConstructor('Bus', 6, 20);
console.log(Bus);

Bus.passengerCount = function(passengers) {
    var count = 0;
    count += passengers;
    console.log(count);
}

Bus.passengerCount(23);
console.log(Bus);
