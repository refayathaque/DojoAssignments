// var mongoose = require('mongoose');
//
// var AnswerSchema = new mongoose.Schema({
//     content: {type: String, required: true},
//     detail: {type: String, required: true},
//     created_by: {type: String, required: true},
//     like: {type: Number, required: true},
//     _questions: [{type: QuestionSchema.Types.ObjectId, ref: 'Question'}]
// }, {timestamps: true});
//
// AnswerSchema.methods.like = function(callback) {
//     this.like += 1;
//     this.save(function(err) {
//         callback(err);
//     })
// }
//
// var Answer = mongoose.model('Answer', AnswerSchema);
