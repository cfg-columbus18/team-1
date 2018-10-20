/**
 * GET /
 * Home page.
 */
exports.index = (req, res) => {
  res.render('home', {
    title: 'Home'
  });
};

/**
 * GET /
 * About page.
 */
exports.about = (req, res) => {
  res.render('about', {
    title: 'About'
  });
};

/**
 * GET /
 * Find a Mentor page.
 */
exports.find = (req, res) => {
  res.render('find', {
    title: 'Find a Mentor'
  });
};