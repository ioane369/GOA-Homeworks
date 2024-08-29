// Task: Create a constructor function that takes four values as arguments (you can choose the type of object the constructor will create).

function Book(title, author, year, genre) {
    this.title = title;
    this.author = author;
    this.year = year;
    this.genre = genre;

    // Added method to return a summary of the book
    this.getSummary = function() {
        return this.title + ' by ' + this.author + ' (' + this.year + ') - ' + this.genre;
    };
}

const firstBook = new Book('Fight Club', 'Chuck Palahniuk', 1996, 'Psychological Thriller, Satire');
const secondBook = new Book('The Hobbit', 'J.R.R. Tolkien', 1937, 'Fantasy');

console.log(firstBook.getSummary());
console.log(secondBook.getSummary());