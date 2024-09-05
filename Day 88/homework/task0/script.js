const spans = document.getElementsByTagName('span');
const startBtn = document.getElementById('startBtn');
const userScore = spans[0];
const compScore = spans[1];

const compChoiceDisplayer = spans[2];
const compChoiceP = compChoiceDisplayer.parentElement;
const imagesDiv = document.getElementById('imagesDisplayer');

function toggleGame(){
    if (startBtn.textContent === 'New Game'){
        imagesDiv.style.visibility = 'visible';
        compChoiceP.style.visibility = 'visible';
        startBtn.textContent = 'Quit'; 
    } else {
        imagesDiv.style.visibility = 'hidden';
        compChoiceP.style.visibility = 'hidden';
        startBtn.textContent = 'New Game';
        userScore.textContent = '';
        compScore.textContent = '';
        compChoiceDisplayer.textContent = '';
    }
}

startBtn.addEventListener('click', toggleGame);

const choices = ['rock', 'paper', 'scissors'];
imagesDiv.addEventListener('click', function(e){
    const userChoice = e.target.id;

    const compChoice = choices[Math.trunc(Math.random() * 3)];
    compChoiceDisplayer.textContent = compChoice;

    if (userChoice === compChoice){
        alert('It is a tie!');
    } else if(userChoice === 'rock' && compChoice === 'scissors' || userChoice === 'paper' && compChoice === 'rock' || userChoice === 'scissors' && compChoice === 'paper'){
        alert('You won!');
        userScore.textContent++;
    } else {
        alert('You lost!');
        compScore.textContent++;
    }
});