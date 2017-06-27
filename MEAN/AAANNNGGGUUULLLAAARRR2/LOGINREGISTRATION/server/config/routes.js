var users = require('../controllers/users.js')
module.exports = function(app) {
    app.post('/users', (req, res) => {
        console.log(req.body)
        user.create(req, res);
    })
}
