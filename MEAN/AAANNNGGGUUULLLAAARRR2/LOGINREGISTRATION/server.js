// Express -- 'npm install express --save' in the server folder
const express = require('express');
const app = express();
// Path
const path = require('path');
// Body-Parser (to receive post data from clients) -- 'npm install body-parser --save' in the server folder
const bodyParser = require('body-parser');
// Mongoose -- 'npm install mongoose --save' in the server folder
const mongoose = require('mongoose');
// Mongoose Config
require('./server/config/mongoose.js');
// Routes
// const routes_setter = require('./server/config/routes.js');
// routes_setter(app);

app.use(express.static(path.join(__dirname, './public/dist')));
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());

app.get('*', function(req, res){
    res.redirect('/')
});

app.listen(8000, function() {
    console.log("listening on port 8000");
})
