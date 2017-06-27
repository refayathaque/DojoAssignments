const mongoose = require('mongoose');
const User = mongoose.model('User');

function UsersController() {

    this.create = function(req, res) {
        User.findOne({email: req.body.email})
        .then((user) => {
            console.log(user)
            if(user) {
                res.json({error: true, messages: 'email already exists!'})
            } else {
                var user = new User(req.body)
                user.save((err, user) => {
                    console.log('user created!')
                    if(err) {
                        res.json({error: true, messages: err.errors.email.message})
                    } else {
                        res.json({error: false, user: user})
                    }
                })
            }
        })
        .catch((err) => {
            console.log(err)
        })
    }

}

module.exports = new UsersController();
