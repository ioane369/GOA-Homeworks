// Use the properties we've learned (parentElement, children, firstElementChild, lastElementChild, previousElementSibling, and nextElementSibling) to manipulate different elements with the help of these properties. Additionally, explain the purpose of each property. Utilize getElementsByTagName and getElementsByClassName, explain their purpose, what they return, and how they differ from other methods.

// Using the getElementsByTagName method to select all <p> elements.
// This method returns an HTMLCollection of all elements with the specified tag name.
// The HTMLCollection is live and updates if the document changes.
const paragraphs = document.getElementsByTagName('p');
console.log("getElementsByTagName('p'):", paragraphs);

// Using the getElementsByClassName method to select all elements with the class 'container'.
// This method returns a live HTMLCollection of all elements with the specified class name.
const containers = document.getElementsByClassName('container');
console.log("getElementsByClassName('container'):", containers);

// Accessing the parent element of the <h1> with the id 'mainHeading'.
// The parentElement property returns the parent node of the specified element in the DOM tree.
console.log("Parent element of <h1>:", document.getElementById("mainHeading").parentElement); 

// Accessin and logging all children of the first element with the class 'container'.
// The children property returns a live HTMLCollection of all child elements (excluding text nodes) of the specified element.
console.log("Children of first <div>:", containers[0].children); // Logs 

// Accessing and logging the first child element of the <main> element.
// The firstElementChild property returns the first child element (excluding text nodes) of the specified element.
console.log("First child of <main>:", document.getElementsByTagName('main')[0].firstElementChild); 

// Accessing and logging the last child element of the <main> element.
// The lastElementChild property returns the last child element (excluding text nodes) of the specified element.
console.log("Last child of <main>:", document.getElementsByTagName('main')[0].lastElementChild);

// Accessing and logging the previous sibling element of the second <div> with the class 'container'.
// The previousElementSibling property returns the previous sibling element (excluding text nodes) of the specified element.
console.log("Previous sibling of second <div>:", containers[1].previousElementSibling); 

// Accessing and logging the next sibling element of the first <p> element.
// The nextElementSibling property returns the next sibling element (excluding text nodes) of the specified element.
console.log("Next sibling of first <p>:", paragraphs[0].nextElementSibling); 