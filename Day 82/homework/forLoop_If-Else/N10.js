// Write a function that finds the missing number in an array. The sequence contains exactly one number missing. Use a for loop to identify the missing number. 

function findMissingNumber(array) {
    for (let i = 0; i < array.length - 1; i++) {
        if (array[i + 1] - array[i] !== 1) {
            return array[i] + 1;
        }  
    }
}

console.log(findMissingNumber([1, 2, 4, 5, 6]));