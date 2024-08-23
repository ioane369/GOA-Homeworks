const addBtn1 = document.getElementById('addBtn1');
const subtractBtn1 = document.getElementById('subtractBtn1');
const jordanQuantity = document.getElementById('jordanQuantity');
const jordanPrice = document.getElementById('jordanPrice');
const addBtn2 = document.getElementById('addBtn2');
const subtractBtn2 = document.getElementById('subtractBtn2');
const campusQuantity = document.getElementById('campusQuantity');
const campusPrice = document.getElementById('campusPrice');
const addBtn3 = document.getElementById('addBtn3');
const subtractBtn3 = document.getElementById('subtractBtn3');
const pumaQuantity = document.getElementById('pumaQuantity');
const pumaPrice = document.getElementById('pumaPrice');

addBtn1.onclick = function() {
    jordanQuantity.textContent = Number(jordanQuantity.textContent) + 1;
    jordanPrice.textContent = '$' + String(Number(jordanPrice.textContent.replace('$', '')) + 200);
};

subtractBtn1.onclick = function() {
    jordanQuantity.textContent = Number(jordanQuantity.textContent) - 1;
    jordanPrice.textContent = '$' +  String(Number(jordanPrice.textContent.replace('$', '')) - 200); 
};

addBtn2.onclick = function() {
    campusQuantity.textContent = Number(campusQuantity.textContent) + 1;
    campusPrice.textContent = '$' + String(Number(campusPrice.textContent.replace('$', '')) + 130);
};

subtractBtn2.onclick = function() {
    campusQuantity.textContent = Number(campusQuantity.textContent) - 1;
    campusPrice.textContent = '$' +  String(Number(campusPrice.textContent.replace('$', '')) - 130); 
};

addBtn3.onclick = function() {
    pumaQuantity.textContent = Number(pumaQuantity.textContent) + 1;
    pumaPrice.textContent = '$' + String(Number(pumaPrice.textContent.replace('$', '')) + 150);
};

subtractBtn3.onclick = function() {
    pumaQuantity.textContent = Number(pumaQuantity.textContent) - 1;
    pumaPrice.textContent = '$' +  String(Number(pumaPrice.textContent.replace('$', '')) - 150); 
};