var users = require('../controllers/users.js')
var questions = require('../controllers/questions.js')

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
}
