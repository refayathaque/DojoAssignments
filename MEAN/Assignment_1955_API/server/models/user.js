var mongoose = require('mongoose');

var UserSchema = new mongoose.Schema({
    name: {type: String, required: true}
}, {timestamps: false});

var User = mongoose.model('User', UserSchema);
