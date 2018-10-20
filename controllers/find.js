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
  res.render('mentorslist', {

  });
};
exports.findMentor = (req,res,next) => {
	User.find({language: req.language}, (err,users) =>{
		if(err){ next(err); }
		res.render('mentorslist/', {
			users: users
		});
	});		
	return;
}
