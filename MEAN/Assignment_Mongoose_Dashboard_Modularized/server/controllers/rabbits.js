var mongoose = require('mongoose');

var Rabbit = mongoose.model('Rabbit');

module.exports = {

    index: function(req, res) {
        Rabbit.find({}, function(err, rabbits) {
            res.render('index', {rabbits: rabbits})
        })
    },

    new: function(req, res) {
        res.render('adopt')
    },

    create: function(req, res) {
        console.log("POST DATA", req.body);
        var rabbit = new Rabbit({name: req.body.name, age: req.body.age});
        rabbit.save(function(err) { // Not Rabbit because we are saving an INSTANTIATION of the Rabbit OBJECT CONSTRUCTOR
            if(err) {
                console.log('Something went wrong');
                res.render('adopt', {errors: rabbit.errors})
            }
            else {
                console.log('Succesfully adopted a rabbit!')
                res.redirect('/');
            }
        })
    },

    show: function(req, res) {
        Rabbit.find({_id: req.params.id}, function(err, rabbits) {
            console.log(rabbits);
            res.render('display', {rabbits: rabbits})
        })
    },

    edit: function(req, res) {
        Rabbit.find({_id: req.params.id}, function(err, rabbits) {
            if(err) {
                console.log('Something went wrong');
            }
            else {
                console.log(rabbits);
                res.render('edit', {rabbits : rabbits});
            }
        })
    },

    update: function(req, res) {
        console.log("POST DATA", req.body);
        Rabbit.update({_id: req.params.id}, {name: req.body.name, age: req.body.age}, function(err, result) {
            if(err) {
                console.log('Something went wrong');
                res.render('edit', {errors: rabbit.errors});
            }
            else {
                console.log('Update was succesful!');
                res.redirect('/');
            }
        })
    },

    destroy: function(req, res) {
        Rabbit.remove({_id: req.params.id}, function(err) {
            if(err) {
                console.log('Something went wrong');
            }
            else {
                console.log('Removal was succesful!');
                res.redirect('/');
            }
        })
    }
}
