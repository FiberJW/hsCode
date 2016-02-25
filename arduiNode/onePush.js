var five, board, button;
five = require('johnny-five');
board = new five.Board();

board.on("ready", function() {
  var button = new five.Button(12);
  var led = new five.Led(8);
  var ledState = false;
  button.on('press', function() {
    led.toggle();
    console.log('toggled');
  });
});
