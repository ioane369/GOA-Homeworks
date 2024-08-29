// Use the sort() method to sort the elements in ascending order first, and then in descending order.

const numbers = [8, 3, 9, 483, 3, 4, 2, 1];

numbers.sort(function(a, b) {
    return a - b; // Sorts numbers in ascending order
});
console.log(numbers);

numbers.sort(function(a, b) {
    return b - a; // Sorts numbers in descending order
});
console.log(numbers);