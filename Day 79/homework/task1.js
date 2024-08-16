userName = document.getElementById('userName');
userEmail = document.getElementById('userEmail');
userMessage = document.getElementById('userMessage');

function clearInputs() {
    userName.value = '';
    userEmail.value = '';
    userMessage.value = '';
}

clearBtn.addEventListener('click', clearInputs);