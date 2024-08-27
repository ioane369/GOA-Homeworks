// 1) Create a function that takes two numbers, start and end, as arguments. Your task is to put all the numbers between these two numbers into an array and return the array.
// 2) Pass the returned array to a function called calculateAverage. In this function, calculate the average of the numbers in the array and return the result.

function getNumbersBetween(start, end) {
    const numbersArray = [];
    for (let num = start; num < end; num++) {
        numbersArray.push(num);
    }
    return numbersArray;
}

function calculateAverage(array) {
    let sum = 0;
    for (const num of array) {
        sum += num;
    }
    const average = sum / array.length;
    return average;
}

const testArray = getNumbersBetween(0, 5);
console.log(calculateAverage(testArray));