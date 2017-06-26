var users = require('../controllers/users.js')
module.exports = function(app) {
    app.post('/users', (req, res) => {
        console.log(req.body)
        users.create(req, res);
    })
}
