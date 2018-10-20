const User = require('../models/User');

/**
 * GET /
 * Find a Mentor page.
 */
exports.find = (req, res) => {
    res.render('find', {
      title: 'Find a Mentor'
    });
  };

exports.mentorslist = (req,res) => {
  console.log(users);
	res.render('mentorslist', {
  });
};

exports.findMentor = (req,res) => {
	console.log("It is reaching here");
	User.find({language: [req.query.language], type:1}, (err,users) =>{
		if(err){ return console.log(err); }
		console.log(users);
		res.render('mentorslist', {
			'users': users
		});
	});
	return;
}
