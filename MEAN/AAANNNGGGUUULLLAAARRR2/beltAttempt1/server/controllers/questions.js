const mongoose = require('mongoose');
const Question = mongoose.model('Question');

function QuestionsController() {

    this.create = function(req, res) {
        console.log("Inside questions controller")
        Question.findOne({content: req.body.content})
        .then((content) => {
            console.log(req.body.content)
            console.log(req.body.description)
            console.log(req.body.created_by)
            if(content) {
                res.json({error: true, messages: 'This question has already been submitted!'})
            } else {
                var question = new Question(req.body)
                question.save((err, question) => {
                    console.log('Question created!')
                    if(err) {
                        res.json({error: true, messages: 'Question NOT submitted!'})
                    } else {
                        res.json({error: false, messages: 'Question submitted!'})
                    }
                })
            }
        })
        .catch((err) => {
            console.log(err)
        })
    }

}

module.exports = new QuestionsController();
