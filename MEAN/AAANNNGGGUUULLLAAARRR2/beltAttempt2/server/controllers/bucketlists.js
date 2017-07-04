const mongoose = require('mongoose');
const BucketList = mongoose.model('BucketList');
const User = mongoose.model('User');

function BucketListsController() {

    this.show = function(req, res) {
        BucketList.find({})
        // .populate('users')
        .exec(function(err, bucketlists) {
            if(err) {
                console.log(err)
            } else {
                res.json(bucketlists)
            }
        })
    }

    this.update = function(req, res) {
        var id = req.params.id
        BucketList.findOne({_id: id}, function(err, bucketlistitem) {
            bucketlistitem.statusupdate(function(err) {
                if(err) {
                    console.log(err)
                }
                else {
                    res.json(bucketlistitem)
                }
            })
        })
    }
    //
    // this.show = function(req, res){
    // var question_id = req.params.id
    // Question.findOne({_id:question_id})
    // .populate({
    //     path: 'answers',
    //     options: { sort: {'likes': '-1'}}
    // })
    // // http://quabr.com/44231362/mongoose-express-sort-items-order-with-populate-function Where I learned how to do the sort
    // .exec(function(err, question){
    //   if(err){
    //     console.log(err)
    //   }
    //   else{
    //     res.json(question)
    //   }
    // })
    // }

    this.create = function(req, res) {
        console.log("--bucketlists controller--")
        BucketList.findOne({title: req.body.title})
        .then((title) => {
            console.log(req.body.title)
            console.log(req.body.description)
            console.log(req.body.created_by)
            if(title) {
                res.json({error: true, messages: 'This Bucket List item has already been added!'})
            } else {
                var bucketlist = new BucketList(req.body)
                var user = new User(req.body) //
                bucketlist.save((err, bucketlist) => {
                    user.bucketlists.push(bucketlist)
                    user.save(function(err, bucketlist){
                        if(err) {
                            res.json({error: true, messages: 'BucketList item NOT added!'})
                            console.log(err);
                        } else {
                            res.json({error: false, messages: 'BucketList item added!', bucketlist: bucketlist})
                            // ^ 'bucketlist: bucketlist' sends the newly created object back to HomeComponent, so we can display it in table without having to reload page
                        }
                    })
                })
            }
        })
        .catch((err) => {
            console.log(err)
        })
    }

}

module.exports = new BucketListsController();
