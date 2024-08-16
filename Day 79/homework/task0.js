const pass = document.getElementById('pass');
const div1 = document.getElementById('div1');

function validatePassword() {
    if(pass.value.length < 8) {
        messageDisplayer.textContent = 'Password should be at least 8 characters long!';
        return
    }
    messageDisplayer.textContent = 'Valid password';
}

pass.addEventListener('input', validatePassword);