// Write a function that generates the first n numbers of the Fibonacci sequence. Use a for loop to generate the sequence and an if-else statement to handle the first two numbers.

function createFibonacciSequence(n) { 
    if (n === 1) {
        return [0];
    } else if (n === 2) {
        return [0, 1];
    }

    fibonacci = [0, 1];
    for (let length = 2; length < n; length++) {
        let lastTwoSum = 0;
        for (const num of fibonacci.slice(-2)) {
            lastTwoSum += num;
        }
        fibonacci.push(lastTwoSum);
    }

    return fibonacci;
}

console.log(createFibonacciSequence(10));