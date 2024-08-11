// Getting the form element by its ID so we can interact with it using JavaScript.
const myForm = document.getElementById('my-form');

// Creating function to validate the form when the submit button is clicked.
function validateForm() {
    // Getting the values entered by the user in each form field.
    // These fields correspond to the 'name' attributes defined in the HTML input elements.
    const fullName = myForm.elements.fullName.value; // Getting the value from the input field with name 'fullName'.
    const email = myForm.elements.email.value; // Getting the value from the input field with name 'email'.
    const password = myForm.elements.password.value; // Getting the value from the input field with name 'password'.
    const favColour = myForm.elements.favColour.value; // Getting the value from the input field with name 'favColour'.

    // Checking if any of the fields are empty.
    // If any field is empty, the user is alerted to fill in all fields.
    if(fullName == '' || email == '' || password == '' || favColour == '') {
        // Alerting the user that all fields need to be filled out.
        alert('Please fill all input fields!');
        // Returning from the function to prevent further execution since validation failed.
        return;
    }

    // If all fields are filled, logging a success message to the console.
    console.log('Form submitted successfully');
    // Logging the full name entered by the user.
    console.log('Full name: ' + fullName);
    // Logging the email address entered by the user.
    console.log("Email: " + email);
    // Logging the password entered by the user.
    console.log("Password: " + password);
    // Logging the favorite color entered by the user.
    console.log("Favourite colour: " + favColour);
}