// Create a function called 'manualIndexOf' that takes a value and an array as arguments. Your task is to return the index of the value in the array. If the pointer is not found, return -1.

function manualIndexOf(value, array) {
    for (let i = 0; i < array.length; i++) {
        if (array[i] === value) {
            return i;
        } 
    }
    return -1;
}

console.log(manualIndexOf(2, [1, 3, 4, 5, 2, 10]));
console.log(manualIndexOf(true, [1, 3, 4, 5, 2, 10]));