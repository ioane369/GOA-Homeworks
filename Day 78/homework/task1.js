let count = 0;
let p1 = document.getElementById('p1');

function clickCounter() {
    count += 1;
    p1.textContent = count;
}