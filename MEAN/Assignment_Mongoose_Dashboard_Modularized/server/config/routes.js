var rabbits = require('../controllers/rabbits.js');

module.exports = function(app) {

    // Displays all rabbits
    app.get('/', function(req, res) {
        rabbits.index(req, res)
    })

    // Takes to page with adoption form
    app.get('/rabbits/new', function(req, res) {
        rabbits.new(req, res)
    })

    // Inserts new rabbit's information
    app.post('/rabbits', function(req, res) {
        rabbits.create(req, res)
    })

    // Displays info of one specific rabbit
    app.get('/rabbits/:id', function(req, res) {
        rabbits.show(req, res)
    })

    // Displays form to edit info of one specific rabbit
    app.get('/rabbits/edit/:id', function(req, res) {
        rabbits.edit(req, res)
    })

    // Updates the information of a specific rabbit
    app.post('/rabbits/:id', function(req, res) {
        rabbits.update(req,res)
    })

    // Removes a specific rabbit
    app.post('/rabbits/destroy/:id', function(req, res) {
        rabbits.destroy(req, res)
    })
}
