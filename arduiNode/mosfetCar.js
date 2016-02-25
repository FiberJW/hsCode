var five = require('johnny-five');
var board = new five.Board();

board.on('ready', function() {
  var mosfet1 = new five.Pin(6),
      mosfet2 = new five.Pin(8),
      leftSensor = new five.Pin("A0"),
      rightSensor = new five.Pin("A1");

  rightSensor.read(function(error, value) {
    if (error) {
      console.log(error);
    }
    if (value > 600) {
      mosfet1.write(1);
    } else {
      mosfet1.write(0);
    }
  });
});
