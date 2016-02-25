var five, board;
five = require('johnny-five');
board = new five.Board();

board.on('ready', function() {
  var led = new five.Led(8);
  led.blink(5);
});
