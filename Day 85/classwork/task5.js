// Create a function called manualSlice that takes an array and two numbers as arguments: the start index and the end index. Your task is to use a for loop to slice a part of the array from the start index to the end index (excluding the end index) and return the sliced portion.

function manualSlice(array, start, end) {
    const len = array.length;
    if (start < 0) {
        if (-start > len) {
            start = 0;
        } else {
            start = len + start;
        }
    }
    if (end < 0) {
        end = len + end;  
    }
    if (start >= len || start > end) {
        return [];
    }
    if (end > len) {
        end = len;
    }

    const slicedPortion = [];

    for (let i = start; i < end; i++) {
        slicedPortion.push(array[i]);
    }
    return slicedPortion;
}

console.log(manualSlice([1, 2, 3, 4, 5, 6], 2, 5));
console.log(manualSlice([1, 2, 3, 4, 5], -6, -1));
console.log(manualSlice([1, 2, 3, 4, 5], -2, -6));
console.log(manualSlice([1, 2, 3, 4], 3, 2));
console.log(manualSlice([42], -1, 0));
console.log(manualSlice([1, 2, 3, 4], 1, 10));
console.log(manualSlice([1, 2, 3, 4], 5, 7));
console.log(manualSlice([1, 2, 3], 0, -1));
console.log(manualSlice([1, 2, 3], -5, 2));
console.log(manualSlice([1, 2, 3, 4, 5], -4, -2));