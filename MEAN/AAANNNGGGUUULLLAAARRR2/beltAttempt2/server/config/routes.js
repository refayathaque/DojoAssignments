var users = require('../controllers/users.js')
var bucketlists = require('../controllers/bucketlists.js')
// IMPORTANT TO HAVE ALL CONTROLLERS HERE!

module.exports = function(app) {

    // Registration
    app.post('/registration', (req, res) => {
        console.log('REQ BODY : ', req.body)
        users.create(req, res)
    })

    // Login
    app.post('/login', (req, res) => {
        console.log('REQ BODY : ', req.body)
        users.login(req, res)
    })

    // Show ALL users in db
    app.get('/show_all_users', (req, res) => {
        console.log('REQ BODY : ', req.body)
        users.show(req, res)
    })

    // Show ALL bucket list items in db
    app.get('/show_all_items', (req, res) => {
        console.log('REQ BODY : ', req.body)
        bucketlists.show(req, res)
    })

    // Adds bucket list item to db
    app.post('/create_item', (req, res) => {
        console.log('REQ BODY : ', req.body)
        bucketlists.create(req, res)
    })
    // HAVEN'T BEEN ABLE TO GET CREATE BUCKET LIST FUNCTION ^ TO WORK - 07/04/17

    app.post('/updatebucketlist/:id', (req, res) => {
        console.log('REQ BODY : ', req.body)
        bucketlists.update(req, res)
    })

    // app.post('/answers/:id', (req,res)=>{
    //     console.log("inside routes")
    //     answers.create(req, res);
    // })

    // app.post('/answers/:id/like', (req,res)=>{
    //     console.log("inside routes")
    //     answers.like(req, res);
    // })
    //


}
