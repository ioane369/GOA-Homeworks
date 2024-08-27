// Create a for loop that iterates over the numbers from 0 to 10 inclusive. On each iteration, create an object with two properties: value (the current number) and type (which should be 'Even' or 'Odd' depending on whether the number is even or odd). Then, add this object to an array. By the end of the loop, the array will contain objects representing each number from 0 to 10 along with its corresponding type.

let numsAndTypes = [];
for (let num = 0; num <= 10; num++) {
    let numAndType = {
        value: num,
        type: '',
    };

    if (num % 2 === 0) {
        numAndType.type = 'Even';
    } else {
        numAndType.type = 'Odd';
    }
    numsAndTypes.push(numAndType);
}
            
console.log(numsAndTypes);