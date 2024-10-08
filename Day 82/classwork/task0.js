// Create a function called evenSum that takes one parameter, border. The function should iterate through all the numbers from 0 to border (inclusive) and use an if conditional statement to check for even numbers. It should sum all these even numbers and return the result.

function evenSum(border) {
    let res = 0;
    for (let num = 0; num <= border; num++) {
        if (num % 2 === 0) {
            res += num;
        }
    }
    return res;
}
console.log(evenSum(6));