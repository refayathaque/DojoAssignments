var users = require('../controllers/users.js')

module.exports = function(app) {
    app.post('/users', (req, res) => {
        console.log('HELLO', req.body)
        users.create(req, res);
    })
}

// module.exports = function(app) {
// app.post('/users', function(req, res) {
//     console.log('INSIDE OF ROUTE', req.body)
// })
// }
