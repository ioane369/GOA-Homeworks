// Sum of Digits: Use a while loop to sum the digits of a given number. Use if-else to handle cases where the number is negative.

// function sumOfDigits(num) {
//     let digitsSum = 0;

//     if (String(num).length === 1) {
//         return num
//     } else if (num < 0) {
//         const modifiedNum = String(num).slice(1);

//         for (const digit of modifiedNum) {
//             digitsSum += Number(digit);
//         }
//         return digitsSum;
//     } else {
//         for (const digit of String(num)) {
//             digitsSum += Number(digit);
//         }
//         return digitsSum
//     }
// }

// console.log(sumOfDigits(123));
// console.log(sumOfDigits(-123));
// console.log(sumOfDigits(3));

function sumOfDigits(num) {
    let digitsSum = 0;
    let strNum = String(num);

    if (strNum.length === 1) {
        return num;
    } else if (num < 0) {
        strNum = strNum.slice(1);
    } 

    let i = 0;
    while (i < strNum.length) {
        digitsSum += Number(strNum[i]);
        i++;
    }
    return digitsSum;
}

console.log(sumOfDigits(123));
console.log(sumOfDigits(-123));
console.log(sumOfDigits(3));