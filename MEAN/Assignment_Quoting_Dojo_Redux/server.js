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

var QuoteSchema = new mongoose.Schema({
    name: {type: String, required: true},
    quote: {type: String, required: true}
}, {timestamps: true});
mongoose.model('Quote', QuoteSchema);
var Quote = mongoose.model('Quote');

app.get('/', function(req, res) {
    res.render('index')
})

app.post('/add_quote', function(req, res) {
    console.log("POST DATA", req.body);
    var quote = new Quote({name: req.body.name, quote: req.body.quote});
    quote.save(function(err) {
        if(err) {
            console.log('Something went wrong');
            res.render('quotes', {errors: quote.errors})
        }
        else {
            console.log('Succesfully added a quote!')
            res.redirect('/skip_to_quotes');
        }
    })
})

app.get('/skip_to_quotes', function(req, res) {
    Quote.find({}, function(err, quotes) {
        res.render('quotes', {quotes: quotes})
    })
})

app.listen(8000, function() {
    console.log("listening on port 8000");
})
