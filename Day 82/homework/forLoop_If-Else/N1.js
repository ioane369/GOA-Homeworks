// Write a function that checks if a number is prime. Use a for loop to test divisibility and an if statement to return whether the number is prime.

function isNumberPrime(num) {
    for (let divisor = 2; divisor <= num / 2; divisor++) {
        if (num % divisor === 0) {
            return false;
        } 
        return true;
    }
}

console.log(isNumberPrime(7));
console.log(isNumberPrime(10));