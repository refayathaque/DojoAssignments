const mongoose = require('mongoose');
const Question = mongoose.model('Question');

function QuestionsController() {

    this.create = function(req, res) {
        console.log("Inside controller (Question)")
        Question.findOne({question: req.body.question})
        .then((question) => {
            console.log(question)
            if(question) {
                res.json({error: true, messages: 'This question has already been submitted!'})
            } else {
                var question = new Question(req.body)
                question.save((err, question) => {
                    console.log('Question created!')
                    if(err) {
                        res.json({error: true, messages: err.errors.question.message})
                    } else {
                        res.json({error: false, question: question})
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
