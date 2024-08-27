// Write a function that uses a while loop to check if a given string str is a palindrome (a word, phrase, or sequence that reads the same backward as forward). Use an if-else statement to compare characters from the beginning and end of the string, moving towards the center. If all corresponding characters match, return true; otherwise, return false.

function isPalindrome(str) {
    let reversedStr = '';
    let i = str.length - 1;

    while (i >= 0) {
        reversedStr += str[i];
        i--;
    }
    if (reversedStr === str) {
        return true;
    } else {
        return false;
    }
    // without if-else statement:
    // return reversedStr === str;
}

console.log(isPalindrome('abcdcba'));
console.log(isPalindrome('abcd'));