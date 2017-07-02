var mongoose = require('mongoose');
var Schema = mongoose.Schema;

var BucketListSchema = new Schema({
    title: {type: String, required: true, minlength: 5},
    description: {type: String, required: true, minlength: 10},
    created_by: {type: String, required: true},
    status: {type: Boolean, required: true, default: false},
    friend: {type: String}
}, {timestamps: true});

var BucketList = mongoose.model('BucketList', BucketListSchema);

// users: [{type: Schema.Types.ObjectId, ref: 'User'}]
