var mongoose = require('mongoose');
var bcrypt = require('bcrypt');
var UserSchema = new mongoose.Schema({
    firstname: {type: String, required: true},
    lastname: {type: String, required: true},
    birthdate: {type: Date, required: true},
    username: {type: String, required: true},
    email: {type: String, required: true},
    password: {type: String, required: true},
    confirmpassword: {type: String, required: true},
    created_at: {type: Date, required: true},
    updated_at: {type: Date, required: true}
}, {timestamps: false});

// Bcrypt Password Hashing
UserSchema.methods.generateHash = function(password){
    return bcrypt.hashSync(password, bcrypt.genSaltSync(8))
}
UserSchema.methods.comparePassword = function(password){
    return bcrypt.compareSync(password, this.password);
}
UserSchema.pre('save', function(done){
    this.password = this.generateHash(this.password);
    done()
})

var User = mongoose.model('User', UserSchema);
