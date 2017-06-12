var express = require('express'),
    path    = require('path'),
    mongoose = require('mongoose'),
    bodyParser = require('body-parser'),
    port    = 8000,
    app     = express();

// Express basic setup
app.use(bodyParser.urlencoded({ extended: true }));
app.use(express.static(path.join(__dirname, './static')));
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

// Connect to db
mongoose.connect('mongodb://localhost/message_board');

// Declare and initialize schema variable
var Schema = mongoose.Schema;

// Create message schema
var MessageSchema = new Schema({
    name: { type: String, required: true, minlength: 2 },
    content: { type: String, required: true },
    comments: [{ type: Schema.Types.ObjectId, ref: 'Comment'}] // 'Comment' is the model
}, { timestamps: true } );

// Create comments schema
var CommentSchema = new Schema({
    _message: { type: Schema.Types.ObjectId, ref: 'Message' },
    name: { type: String, required: true, minlength: 2 },
    content: { type: String, required: true}
}, {timestamps: true});

// Register models
var Message = mongoose.model('Message', MessageSchema);
var Comment = mongoose.model('Comment', CommentSchema);

// Routes
app.get('/', function(req, res){ // Function is a 'callback'
    Message.find({})
    .populate('comments')
    .exec(function(err, results){
        if (err){ console.log(err); }
        console.log(results);
        res.render('index', { messages: results });
    });
});

app.post('/messages', function(req, res){
    Message.create(req.body, function(err, result){
        if (err) { console.log(err); }
        res.redirect('/');
    });
});

app.post('/messages/:id/comments', function(req, res){
    // Find message the comment will belong to
    Message.findOne({_id: req.params.id}, function(err, message){
        // Create a comment using data from form
        // req.params bring parameters from the URLs, so ':id' above
        // req.body bring information from forms
        var comment = new Comment(req.body);
        // Set the reference like this
        comment._message = message._id;
        // The comment now belogs to the message we found above
        // Now, save both to the DB
        comment.save(function(err){
            // Push the comment into the comments array of the message we found
            message.comments.push(comment);
            // Save the updated message
            message.save(function(err){
                if (err){ console.log(err); }
                else{
                    res.redirect('/');
                }
            })
        })
    })
})

// Setting our server to listen to port
app.listen(8000, function() {
    console.log("listening on port 8000");
});
