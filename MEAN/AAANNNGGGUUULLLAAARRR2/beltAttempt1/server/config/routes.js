var users = require('../controllers/users.js')
var questions = require('../controllers/questions.js')
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

    app.post('/newquestions', (req, res) => {
        console.log('REQ BODY : ', req.body)
        questions.create(req, res)
    })

    app.get('/index', (req,res) => {
        console.log("Inside Routes (Home)")
        console.log('REQ BODY : ', req.body)
        questions.showAllQuestions(req, res)
    })

}
