// Require the Express Module
var express = require('express');

// Create an Express App
var app = express();

// Require body-parser (to receive post data from clients)
var bodyParser = require('body-parser');

// Integrate body-parser with our App
app.use(bodyParser.urlencoded({ extended: true }));

// Require path
var path = require('path');

// Setting our Static Folder Directory
app.use(express.static(path.join(__dirname, './static')));

// Setting our Views Folder Directory
app.set('views', path.join(__dirname, './views'));

// Setting our View Engine set to EJS
app.set('view engine', 'ejs');

// Require Mongoose
var mongoose = require('mongoose');

// Connecting to MongoDB database using Mongoose * 'users' is the name of our db * If you connect to a database that doesn't exist, mongoose WILL create the DB for you!
mongoose.connect('mongodb://localhost/users');

// Creating a Schema
var UserSchema = new mongoose.Schema({
    name: {type: String, required: true, minlength: 2},
    age: {type: Number, required: true, min: 17, max: 90}
}, {timestamps: true});
mongoose.model('User', UserSchema); // Setting this Schema in our Models as 'User'
var User = mongoose.model('User'); // Retrieving this Schema from our Models, named 'User'

// ROUTES

// Root Request
app.get('/', function(req, res) {
    // This is where we will retrieve the users from the database and include them in the view page we will be rendering.
    User.find({}, function(err, users) { // Finding all users * 'Mongoose Commands' section has info on all other querying
        if(err) {
            console.log('Something went wrong');
        }
        else {
            console.log('Succesfully displayed all users!');
            res.render('index', {users : users});
        }
    })
})

// Add User Request
app.post('/users', function(req, res) {
    console.log("POST DATA", req.body);
    // This is where we would add the user from req.body to the database.
    // Creating a new User with name and age from req.body
    var user = new User({name: req.body.name, age: req.body.age});
    // Inserting to db and running a CALLBACK with an error (if any)
    user.save(function(err) {
        if(err) {
            console.log('Something went wrong');
            res.render('index', {errors: user.errors})
            // Displays errors on front-end
        }
        else {
            console.log('Succesfully added a user!')
            res.redirect('/');
        }
    })
})

// Setting our Server to Listen on Port: 8000
app.listen(8000, function() {
    console.log("listening on port 8000");
})
