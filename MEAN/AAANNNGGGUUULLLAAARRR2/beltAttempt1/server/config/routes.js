var users = require('../controllers/users.js')

module.exports = function(app) {
    app.post('/users', (req, res) => {
        console.log('REQ BODY : ', req.body)
        users.create(req, res)
    })
    app.post('/login', (req,res) => {
        console.log('REQ BODY : ', req.body)
        users.login(req, res)
    })
    app.post('/questions', (req, res) => {
        console.log('REQ BODY : ', req.body)
        questions.create(req, res)
    })
}
