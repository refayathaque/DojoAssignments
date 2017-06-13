var mongoose = require('mongoose');

var RabbitSchema = new mongoose.Schema({
    name: {type: String, required: true},
    age: {type: Number, required: true}
}, {timestamps: true});

var Rabbit = mongoose.model('Rabbit', RabbitSchema);
