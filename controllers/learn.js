/**
 * GET /
 * Learn page.
 */
exports.learn = (req, res) => {
    res.render('learn', {
      title: 'Learn More'
    });
  };