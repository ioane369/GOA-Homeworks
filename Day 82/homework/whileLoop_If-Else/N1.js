// Print Numbers: Write a while loop to print numbers from 1 to 10 (including). Use if-else to print "even" for even numbers and "odd" for odd numbers.

let num = 0;

while (num <= 10) {
    if (num % 2 !== 0) {
        console.log(num + ' is odd');
    } else {
        console.log(num + ' is even');
    }
    num ++;
}