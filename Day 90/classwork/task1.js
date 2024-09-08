const box = document.getElementById('box');

let positionX = 0;
let positionY = 0;
let direction = 'right';

function animateBox(){
    if (direction === 'right'){
        positionX++;
        if (positionX === 150){
            direction = 'bottom';
        }
    } else if (direction === 'bottom'){
        positionY++;
        if (positionY === 150){
            direction = 'left';
        }
    } else if (direction === 'left'){
        positionX--;
        if (positionX === 0){
            direction = 'top';
        }
    } else if (direction === 'top'){
        positionY--;
        if (positionY === 0){
            direction = 'right';
        }
    }
    box.style.left = positionX + 'px';
    box.style.top = positionY + 'px'; 
}

setInterval(animateBox, 20);