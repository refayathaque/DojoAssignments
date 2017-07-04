var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var BucketListSchema = new Schema({
    title: {type: String, required: true, minlength: 5},
    description: {type: String, required: true, minlength: 10},
    created_by: {type: String, required: true},
    status: {type: Boolean, required: true, default: false},
    friend: {type: String, required: false}
}, {timestamps: true});

BucketListSchema.methods.statusupdate = function(callback) {
    if(this.status === false) {
        this.status = true;
    }
    else if(this.status === true) {
        this.status = false;
    }
    this.save(function(err) {
        callback(err);
    });
}

var BucketList = mongoose.model('BucketList', BucketListSchema);
// IMPORTANT to have ^ all the way at the end when models have methods
