// Countdown: Write a while loop to countdown from 10 to 1. Use if-else to print "Blast Off!" when the countdown reaches 1.

let num = 10;

while (num >= 1) {
    if (num === 1) {
        console.log('Blast Off!');
    } else {
      console.log(num);
    }
    num--;
}