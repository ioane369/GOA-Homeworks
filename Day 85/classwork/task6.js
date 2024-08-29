// Create a function called 'manualFilter' that takes a function as its first argument and an array as its second argument. Inside this function, use a for loop to iterate over the array. For each element, call the provided function with the current element as its argument. If the function returns true, add the element to a new array; if it returns false, do not add it. After the for loop finishes, return the new array. The provided function must return a boolean value and should accept a single element as its argument. What you check in the provided function is up to you.

function isPrime(num) {
    if (num < 2) {
        return false;
    }
    for (let divisor = 2; divisor <= Math.sqrt(num); divisor++) {
        if (num % divisor === 0) {
            return false;
        }
    }
    return true;
}

function manualFilter(isPrime, array) {
    const primes = [];

    for (let i = 0; i < array.length; i++) {
        if (isPrime(array[i])) {
            primes.push(array[i]);
        }
    }
    return primes;
}

console.log(manualFilter(isPrime, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]));