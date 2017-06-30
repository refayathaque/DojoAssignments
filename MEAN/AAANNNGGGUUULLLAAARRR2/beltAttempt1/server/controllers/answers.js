const mongoose = require('mongoose');
const Answer = mongoose.model('Answer');
var Question = mongoose.model('Question')

function AnswersController() {

    // this.showAllQuestions = function(req, res) {
    //     Question.find({})
    //     .populate("answers")
    //     .exec(function(err, questions) {
    //         if(err) {
    //             console.log(err)
    //         } else {
    //             res.json(questions)
    //         }
    //     })
    // }
    //
    // this.show = function(req, res){
    // var question_id = req.params.id
    // Question.findOne({_id:question_id})
    // .populate("answers")
    // .exec(function(err, question){
    //   if(err){
    //     console.log(err)
    //   }
    //   else{
    //     res.json(question)
    //   }
    // })
    // }

    this.create=function(req, res){
    var question_id = req.params.id
    console.log(req.body)
    Question.findOne({_id:question_id}, function(err, question){
      var answer = new Answer(req.body);
      answer._question = question_id
      //we need to save both to the db!
      answer.save(function(err){
        question.answers.push(answer)
        question.save(function(err, question){
          if(err){
            console.log(err);
          }
          else{
            res.json(question)
          }
        })
      })
    })
}

    this.like=function(req, res){
        var answer_id = req.params.id
        Answer.findOne({_id:answer_id}, function(err, answer){
            answer.like(function(err){
                if(err){
                    console.log(err)
                }
                else{
                    res.json(answer)
                }
            })
        })
    }

}


module.exports = new AnswersController();
