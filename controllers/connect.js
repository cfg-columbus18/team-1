/**
 * GET /
 * Connection with mentee/mentor.
 */
exports.connect = (req, res) => {
    //var url = '52.90.61.82:4567';
    //var start = (process.platform == 'darwin'? 'open': process.platform == 'win32'? 'start': 'xdg-open');
    //require('child_process').exec(start + ' ' + url);
    res.redirect('http://52.90.61.82:4567/');
};