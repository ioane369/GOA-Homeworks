// Write a function that takes a string and returns an object where the keys are characters and the values are the number of times they appear in the string. Use a for loop to iterate through the string and an if-else statement to update the count.

function countCharsFrequency(str) {
    frequency = {};
    let strWithoutDuplicates = '';

    for (const char of str) {
        if (!strWithoutDuplicates.includes(char)) {
            strWithoutDuplicates += char;
        } 
    }

    for (const char of strWithoutDuplicates) {
        for (const char1 of str) {
            if (char1 === char) {
                if (frequency[char]) {
                    frequency[char] += 1;
                } else {
                    frequency[char] = 1;
                }
            } 
        }
    }
    return frequency;
}

// Optimized version:
function countCharsFrequency1(str) {
    let frequency = {};

    for (const char of str) {
        if (frequency[char]) {
            frequency[char] += 1;
        } else {
            frequency[char] = 1;
        }
    }
    return frequency;
}

console.log(countCharsFrequency("mississippi"));
console.log(countCharsFrequency1("mississippi"));