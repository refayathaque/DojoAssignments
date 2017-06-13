var mongoose = require('mongoose');

var User = mongoose.model('User');

module.exports = {

    index: function(req, res) {
        User.find({}, function(err, data) {
            res.json(data)
        })
    },

    create: function(req, res) {
        var user = new User({name: req.params.name});
        user.save(function(err, data) {
            if(err) {
                res.json(err);
            }
            else {
                res.json(data);
            }
        })
    },

    destroy: function(req, res) {
        User.remove({name: req.params.name}, function(err, data) {
            if(err) {
                res.json(err);
            }
            else {
                User.find({}, function(err, data) {
                    if(err) {
                        res.json(err);
                    }
                    else {
                        res.json(data);
                    }
                })
            }
        })
    },

    show: function(req, res) {
        User.find({name: req.params.name}, function(err, data) {
            if(err) {
                res.json(err);
            }
            else {
                res.json(data);
            }
        })
    }
}
