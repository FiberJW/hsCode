var five, board;
five = require('johnny-five');
board = new five.Board();

board.on('ready', function() {
  function bling(pin) {
    this.digitalWrite(pin, 1);

    this.wait(1000, function() {
      // Turn it off...
      this.digitalWrite(pin, 0);
    });
  }
  this.loop(2000,function() {
    bling.call(this, 8);
    this.wait(1000, function() {
      bling.call(this, 12);
    });
  })
});
