// Provide 3 examples for each method (indexOf, lastIndexOf, includes) and explain in your own words what these methods do.

const testArray = [-2, -1, 0, true, 'a', 'b', 'c', 'a', true];

// The indexOf() method returns the first index at which a given element can be found in the array. If the element is not found, it returns -1.
console.log(testArray.indexOf('a')); // Outputs 4
console.log(testArray.indexOf(true && false)); // Outputs -1 (element not found)
console.log(testArray.indexOf(-2)); // Outputs 0

// The lastIndexOf() method returns the last index at which a given element can be found in the array. If the element is not found, it returns -1.
console.log(testArray.lastIndexOf(true || false)); // Outputs 8
console.log(testArray.lastIndexOf('a')); // Outputs 7
console.log(testArray.lastIndexOf(0)); // Outputs 2

// The includes method checks if the array contains a certain element and returns true if it is found and false if it is not.
console.log(testArray.includes(false)); // Outputs false
console.log(testArray.includes('b')); // Outputs true
console.log(testArray.includes(-1 + 1)); // Outputs true