var express = require("express");
var path = require("path");
var app = express();

// app.use(express.static(path.join(__dirname, "./static"))); bc no CSS/images here
app.set('views', path.join(__dirname, './views'));
app.set('view engine', 'ejs');

app.get('/', function(req, res) {
    res.render("index");
})

var server = app.listen(8000, function() {
 console.log("listening on port 8000");
});

var io = require('socket.io').listen(server);

io.sockets.on('connection', function (socket) {

    var counter = 0;

    socket.on('clicking_epic_button', function (data) {
        counter += 1;
        console.log(data.test);
        socket.emit('send_counter', {response: counter});
    });

    socket.on('clicking_reset_button', function (data) {
        counter = 0;
        console.log(data.test);
        socket.emit('send_zeroed_counter', {response: counter});
    });

});
