const userMessage = document.getElementById('userMessage');
const charCountDisplayer = document.getElementById('charCountDisplayer');

function displayCharsQuantity() {
    const currentLength = userMessage.value.length;
    if(currentLength > 200) {
        alert('You have reached the charachter limit of 200!');
        return
    }
    charCountDisplayer.textContent = String(currentLength) + '/200charachters';
}

userMessage.addEventListener('input', displayCharsQuantity);