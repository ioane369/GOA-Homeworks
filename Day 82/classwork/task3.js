// Create a function called generateEven. This function should accept a parameter named border. Its task is to create a new array, add all even numbers from 0 to border to the array, and return the array. Next, pass this array to a function called calculateSum. In calculateSum, use a for loop to calculate the sum of all the numbers in the array and return the sum.

function generateEven(border) {
    let evenNumbers = [];
    for (let num = 0; num <= border; num += 2) {
        evenNumbers.push(num);
    }
    return evenNumbers;
}

function calculateSum(array) {
    let sum = 0;
    for (let num of array) {
        sum += num;
    }
    // another method to iterate over an array:
    // for (let index = 0; index < array.length; index++) {
    //     sum += array[index];
    // }
    return sum;
}

const evens = generateEven(6);
console.log(evens);
console.log(calculateSum(evens));