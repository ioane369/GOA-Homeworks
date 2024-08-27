// Write a function findGCD(a, b) that uses a while loop to calculate the greatest common divisor (GCD) of two positive integers a and b. Use an if-else statement to check if either number is zero (if so, return the other number as the GCD). Then, use the Euclidean algorithm inside the loop to repeatedly subtract the smaller number from the larger until both numbers are equal. The final value is the GCD.

function findGCD(num1, num2) {
    if (num1 === 0) {
        return num2;
    } else if (num2 === 0) {
        return num1;
    }

    let dividend = Math.max(num1, num2);
    let divisor = Math.min(num1, num2);
    let remainder = dividend % divisor;

    while (remainder !== 0) {
        dividend = divisor;
        divisor = remainder;
        remainder = dividend % divisor;
    }
    return divisor;
}

console.log(findGCD(10, 5));
console.log(findGCD(30, 40));