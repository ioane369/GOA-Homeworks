const myForm = document.getElementById('myForm');
const submitBtn = document.getElementById('submitBtn');
const dataBase = [];

function saveData() {
    let userInfo = {
        firstName: myForm.elements.firstName.value,
        lastName: myForm.elements.lastName.value,
        email: myForm.elements.email.value,
    };
    dataBase.push(userInfo); 
    console.log(dataBase);
}

// submitBtn.onclick = saveData; 
submitBtn.addEventListener('click', saveData);