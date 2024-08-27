// Given a sentence, use a for loop to iterate through the words and an if-else statement to find and return the longest word. If multiple words have the same length, the function should return the first one.

function findLongestWord(sentence) {
    let words = sentence.replace(/['.,:;?!']/g, '').split(' ');
    let longestWord = '';
    for (let i = 0; i < words.length; i++) {
        if (words[i].length > longestWord.length) {
            longestWord = words[i];
        }
    }
    return longestWord;
}

console.log(findLongestWord('It was a tiring day, so tiring he fell asleep on the train and missed his stop.'));