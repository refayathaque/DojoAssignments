var express = require('express');
var app = express();
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));
var path = require('path');
app.use(express.static(path.join(__dirname, './static')));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/rabbits');

var RabbitSchema = new mongoose.Schema({
    name: {type: String, required: true},
    age: {type: Number, required: true}
}, {timestamps: true});
mongoose.model('Rabbit', RabbitSchema);
var Rabbit = mongoose.model('Rabbit');

// Displays all rabbits
app.get('/', function(req, res) {
    Rabbit.find({}, function(err, rabbits) {
        res.render('index', {rabbits: rabbits})
    })
})

// Takes to page with adoption form
app.get('/rabbits/new', function(req, res) {
    res.render('adopt');
})

// Displays info on one specific rabbit
app.get('/rabbits/:id', function(req, res) {
    Rabbit.find({_id: req.params.id}, function(err, rabbits) {
        console.log(rabbits);
        res.render('display', {rabbits: rabbits})
    })
})

app.post('/rabbits', function(req, res) {
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
})

app.get('/rabbits/edit/:id', function(req, res) {
    Rabbit.find({_id: req.params.id}, function(err, rabbits) {
        if(err) {
            console.log('Something went wrong');
        }
        else {
            console.log(rabbits);
            res.render('edit', {rabbits : rabbits});
        }
    })
})

app.post('/rabbits/destroy/:id', function(req, res) {
    Rabbit.remove({_id: req.params.id}, function(err) {
        if(err) {
            console.log('Something went wrong');
        }
        else {
            console.log('Removal was succesful!');
            res.redirect('/');
        }
    })
})

app.post('/rabbits/:id', function(req, res) {
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
})

app.listen(8000, function() {
    console.log("listening on port 8000");
})
