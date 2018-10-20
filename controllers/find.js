
/**
 * GET /
 * Find a Mentor page.
 */
exports.find = (req, res) => {
    res.render('find', {
      title: 'Find a Mentor'
    });
  };