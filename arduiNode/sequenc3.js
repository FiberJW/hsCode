var five = require('johnny-five');

var board = new five.Board();

board.on('ready', function() {
  var button = new five.Button(8);
  var led1 = new five.Led(9);

  button.on('press', function() {
    console.log('pressed');
    led1.toggle();
  });

});
