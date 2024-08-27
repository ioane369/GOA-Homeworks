// Given an array of numbers, use a for loop to iterate through the array and an if-else statement to create a new array containing only the even numbers.

function filterEvens(array) {
    const evens = [];
    for (const num of array) {
        if (num % 2 === 0) {
            evens.push(num);
        }
    }
    return evens;
}

console.log(filterEvens([0, 1, 1, 2, 4, 5, 6, 8, 9, 11]));