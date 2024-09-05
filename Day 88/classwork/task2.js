const buttons = document.getElementsByTagName('button');
const spans = document.getElementsByTagName('span');
const rock = buttons[0];
const paper = buttons[1];
const scissors = buttons[2];

const userChoiceDisplayer = spans[0];
const compChoiceDisplayer = spans[1];
const userPoints = spans[2];
const compPoints = spans[3];

const quit = buttons[3];
const finalResult = quit.nextElementSibling;

const choices = ['rock', 'paper', 'scissors'];
rock.addEventListener('click', function(){
    const userChoice = 'rock';
    const compChoice = choices[Math.trunc(Math.random() * 3)];
    userChoiceDisplayer.textContent = userChoice;
    compChoiceDisplayer.textContent = compChoice;

    if (userChoice === compChoice){
        alert('Draw');
    } else if (compChoice === 'scissors'){
        alert('You won');
        userPoints.textContent++;
    } else {
        alert('Computer won');
        compPoints.textContent++;
    }
});

paper.addEventListener('click', function(){
    const userChoice = 'paper';
    const compChoice = choices[Math.trunc(Math.random() * 3)];
    userChoiceDisplayer.textContent = userChoice;
    compChoiceDisplayer.textContent = compChoice;

    if (userChoice === compChoice){
        alert('Draw');
    } else if (compChoice === 'rock'){
        alert('You won');
        userPoints.textContent++;
    } else {
        alert('Computer won');
        compPoints.textContent++;
    }
});

scissors.addEventListener('click', function(){
    const userChoice = 'scissors';
    const compChoice = choices[Math.trunc(Math.random() * 3)];
    userChoiceDisplayer.textContent = userChoice;
    compChoiceDisplayer.textContent = compChoice;

    if (userChoice === compChoice){
        alert('Draw');
    } else if (compChoice === 'paper'){
        alert('You won');
        userPoints.textContent++;
    } else {
        alert('Computer won');
        compPoints.textContent++;
    }
});

quit.addEventListener('click', function(){
    if (userPoints.textContent === compPoints.textContent){
        finalResult.textContent = 'Equal points, it is a draw.';
    } else if (userPoints.textContent > compPoints.textContent){
        finalResult.textContent = 'You have more points, you won.';
    } else {
        finalResult.textContent = 'Computer has more points, you lost.';
    }
});