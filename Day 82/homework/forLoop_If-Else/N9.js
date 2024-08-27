// Write a function that finds all pairs of numbers in an array that add up to a given target sum. Use a for loop to iterate through the array and an if statement to check for pairs.

function findPairsWithSum(array, targetSum) {
    const len = array.length;
    if (len < 2) {
        return [];
    }

    const pairs = [];
    for (let i = 0; i < len - 1; i++) {
        let secondI = i + 1;
        while (secondI < len) {
            if (array[i] + array[secondI] === targetSum) {
                pairs.push([array[i], array[secondI]]);
            }
            secondI++;
        }
    }
    return pairs;
}

console.log(findPairsWithSum([1, 2, 3, 4, 3, 5], 6));
console.log(findPairsWithSum([2], 8));