// Fibonacci Sequence: Write a while loop to generate the Fibonacci sequence up to a certain quantity of numbers.


function createFibonacciSequence(quantity) {
    const fibonacci = [0, 1];

    while (fibonacci.length < quantity) {
        let lastTwoSum = 0;
        for (const num of fibonacci.slice(-2)) {
            lastTwoSum += num;
        } 
        fibonacci.push(lastTwoSum);
    }
    return fibonacci;
}

console.log(createFibonacciSequence(10));