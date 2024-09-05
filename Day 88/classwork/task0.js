// I don't understand how to use container and presentational functions, so I don't have that part of the task.

// Selecting the form and table body elements
const form = document.getElementById('myForm');
const tableBody = document.getElementById('tB');

function saveData(event){
    event.preventDefault(); // Prevents the default form submission behavior

     // Creating a table cell for the full name, extracting the input value, and setting it as the cell's text content
    const nameTD = document.createElement('td');
    const fullName = form.elements.fullName.value;
    nameTD.textContent = fullName;

    // Creating a table cell for the email, extracting the input value, and setting it as the cell's text content
    const emailTD = document.createElement('td');
    const email = form.elements.email.value;
    emailTD.textContent = email;

    // Creating a table cell for the password, extracting the input value, and setting it as the cell's text content
    const passwordTD = document.createElement('td');
    const password = form.elements.password.value;
    passwordTD.textContent = password;

    // Creating a new row and appending the previously created table cells to it
    const newRow = document.createElement('tr');
    newRow.append(nameTD, emailTD, passwordTD);
    // Appending the new row to the table body
    tableBody.appendChild(newRow);

    // Resetting the form fields after submission
    form.reset(); 
}

// Adding an event listener to the form to handle form submission
form.addEventListener('submit', saveData);