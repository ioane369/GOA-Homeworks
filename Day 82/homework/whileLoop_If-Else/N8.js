// Check Prime: Use a while loop to check if a number is prime. Use if-else to print whether the number is prime or not.

function isNumberPrime(num) {
    let divisor = 2;
    while (divisor <= Math.sqrt(num)) {
        if (num % divisor === 0) {
            return false;      
        } else {
            divisor++;
        }
    }
    return true;
}

console.log(isNumberPrime(7));
console.log(isNumberPrime(10));