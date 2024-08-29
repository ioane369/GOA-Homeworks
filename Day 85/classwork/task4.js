// Create a function called 'manualReverse' that takes an array as an argument and returns a reversed version of the array.

function manualReverse(array) {
    const reversedArray = [];

    for (let i = array.length - 1; i >= 0; i--) {
        reversedArray.push(array[i]);
    }
    return reversedArray;
}

console.log(manualReverse([1, 2, 3, 3, true, false, 'a']));