const myForm = document.getElementById('myForm');
const dataBase = [];

function Account(firstName, lastName, email) {
    // 'this' refers to the newly created object instance. It allows you to define and assign properties and methods to the object being created.
    this.firstName = firstName;
    this.lastName = lastName;
    this.email = email;
}

function sendToDataBase(event) {
    event.preventDefault();

    const firstName = myForm.elements.firstName.value;
    const lastName = myForm.elements.lastName.value;
    const email = myForm.elements.email.value;
    // 'new' keyword creates a new instance of an object that is defined by a constructor function. It initializes a new object and sets up the this context within the constructor function.
    const currentUser = new Account(firstName, lastName, email);

    dataBase.push(currentUser);
    myForm.reset();

    console.log(dataBase);
}

myForm.addEventListener('submit', sendToDataBase);