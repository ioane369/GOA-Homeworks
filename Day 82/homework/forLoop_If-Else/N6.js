// Write a function that returns an array of unique elements from a given array. Use a for loop to iterate through the array and an if statement to check if the element is already in the new array.

function removeDuplicates(array) {
    const uniques = [];

    for (const element of array) {
        if (!uniques.includes(element)) {
            uniques.push(element);
        }
    }
    return uniques;
}

console.log(removeDuplicates([3, 4, 4, 4, 6, 6, 7, 8, 9, 3]));