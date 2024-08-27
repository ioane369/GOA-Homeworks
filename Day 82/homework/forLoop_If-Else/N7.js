// Write a function to find the largest sum of a contiguous subarray within a given array of integers. Use a for loop to iterate through the array and an if statement to track the maximum sum.

function largestSumSubarray(array) {
    const len = array.length;
    if (len === 0) {
        return 0;
    }

    let largestSum = array[0];
    for (let i = 1; i < len; i++) {
        let end = i + 2;
        while (end < len) {
            let currentSum = 0;
            let subarray = array.slice(i, end);
            
            for (const num of subarray) {
                currentSum += num;
            } 
            if (currentSum > largestSum) {
                largestSum = currentSum;
            }
            end++;
        }  
    }
    return largestSum;
}

console.log(largestSumSubarray([1, -2, 3, 4, -1, 2, 1, -5, 4]));
console.log(largestSumSubarray([-1, -2, -3, -4]));