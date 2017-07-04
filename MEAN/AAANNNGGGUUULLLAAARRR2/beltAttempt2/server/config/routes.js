var users = require('../controllers/users.js')
var bucketlists = require('../controllers/bucketlists.js')
// IMPORTANT TO HAVE ALL CONTROLLERS HERE!

module.exports = function(app) {

    app.post('/users', (req, res) => {
        console.log('REQ BODY : ', req.body)
        users.create(req, res)
    })

    app.post('/login', (req,res) => {
        console.log('REQ BODY : ', req.body)
        users.login(req, res)
    })

    app.post('/addbucketlist', (req, res) => {
        console.log('REQ BODY : ', req.body)
        bucketlists.create(req, res)
    })

    app.post('/updatebucketlist/:id', (req, res) => {
        console.log('REQ BODY : ', req.body)
        bucketlists.update(req, res)
    })

    app.get('/listallusers', (req,res) => {
        console.log('REQ BODY : ', req.body)
        users.listallusers(req, res)
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
    app.get('/userbucketlists', (req,res)=>{
        console.log("Inside Routes (Bucket List Items)")
        console.log(req.body)
        bucketlists.userbucketlists(req, res)
    })

}
