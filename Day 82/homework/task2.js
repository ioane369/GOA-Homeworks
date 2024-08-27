const myForm = document.getElementById('myForm');
const dataBase = [];

function storeInfo() {
    const fullName = myForm.elements.fullName.value;
    const email = myForm.elements.email.value;
    const password = myForm.elements.password.value;
    
    const currentUser = {
        fullName,
        email,
        password,
    };

    let emailAlreadyExists = false
    for (let i = 0; i < dataBase.length; i++) {
        if (dataBase[i].email === currentUser.email) {
            emailAlreadyExists = true;
            break;
        }    
    }

    if (emailAlreadyExists) {
        alert('An account with that email already exists!');
    } else {
        dataBase.push(currentUser);  
        alert('Account was created successfully');
        myForm.reset();
    }
}

myForm.addEventListener('submit', storeInfo);