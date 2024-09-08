const box = document.getElementById('box');

let position = 0;
let direction = 1;

function animateBox() {
    position += direction;

    if (position === 150){
        direction = -1;
    } else if (position === 0){
        direction = 1;
    }

    box.style.left = position + 'px';
}

setInterval(animateBox, 20); 