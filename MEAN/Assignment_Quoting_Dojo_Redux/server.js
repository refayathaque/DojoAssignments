var express = require('express');
var app = express();
var bodyParser = require('body-parser');
app.use(bodyParser.urlencoded({ extended: true }));
var path = require('path');
app.use(express.static(path.join(__dirname, './static')));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');
var mongoose = require('mongoose');
mongoose.connect('mongodb://localhost/quotes');

var UserSchema = new mongoose.Schema({
    name: {type: String, required: true, minlength: 2},
    quote: {type: String, required: true, minlength: 20}
}, {timestamps: true});
mongoose.model('Quote', QuoteSchema);
var User = mongoose.model('Quote');

app.get('/', function(req, res) {
    if(err) {
        console.log('Something went wrong');
        res.render('index', {errors: user.errors})
        // Displays errors on front-end
    }
    else {
        console.log('Succesfully loaded the index page!')
        res.render('index');
    }
})









app.listen(8000, function() {
    console.log("listening on port 8000");
})
