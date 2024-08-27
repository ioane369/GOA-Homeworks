// Write a function that counts the number of prime numbers in a given array. Use a for loop to iterate through the array and an if-else statement to check if each number is prime.

function countPrimeNumbers(array) {
    let primeCount = 0;
    let isPrime;

    for (const num of array) {
        if (num <= 1) {
            continue;
        }

        isPrime = true;

        for (let i = 2; i <= Math.sqrt(num); i++) {
            if (num % i === 0) {
                isPrime = false;
                break;
            }
        }

        if (isPrime) {
            primeCount += 1;
        }
    }  
    return primeCount;
}

console.log(countPrimeNumbers([2, 3, 4, 5, 6, 7, 8, 9, 10]));