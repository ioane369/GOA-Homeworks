// Using all the newly learned methods, create 2 examples for each, and explain with comments in your own words what each method does (push, pop, unshift, shift, slice, splice).

const testArray = ['a', 'b', 'c', 'd', 1, 2, 3, 4];

// unshift() adds one or more elements to the beginning of an array
// Adding 0 and 'z' to the beginning of testArray
testArray.unshift(0, 'z');
console.log(testArray);
// Adding -1 to the beginning of testArray
testArray.unshift(-1);
console.log(testArray);

// shift() removes the first element from an array
// Removing the first element ('-1') from testArray
testArray.shift();
console.log(testArray);
// Removing the new first element ('0') from testArray
testArray.shift();
console.log(testArray);

// push() adds one or more elements to the end of an array
// Adding 'e' to the end of testArray
testArray.push('e');
console.log(testArray);
// Adding 5 and 6 to the end of testArray
testArray.push(5, 6);
console.log(testArray);

// pop() removes the last element from an array and returns it
// Removing the last element (6) from testArray
const lastElement = testArray.pop();
console.log(lastElement); // Logs the removed element (6)
console.log(testArray); // 6 got removed (popped) from the original array
// Removing the new last element (5) from testArray
const newLastElement = testArray.pop();
console.log(newLastElement); // Logs the removed element (5)
console.log(testArray); // 5 got removed (popped) from the original array

// splice() modifies the array by removing (I only know removing yet) elements
// Removing 2 elements starting from index 2
testArray.splice(2, 2); // removed 'b', 'c' from testArray
console.log(testArray);
// Removing 1 element starting from index 0
testArray.splice(0, 1); // removed 'z' from testArray
console.log(testArray); 

// slice() creates a new array containing a portion of the original array, without modifying the original
// Extracting a subarray from index 1 to index 4 (not including 4)
const slicedArray = testArray.slice(1, 4);
console.log(slicedArray);
// Extracting a subarray from index 0 to index 2 (not including 2)
const anotherSlicedArray = testArray.slice(0, 2);
console.log(anotherSlicedArray);