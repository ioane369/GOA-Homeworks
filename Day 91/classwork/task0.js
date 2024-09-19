const btns = document.getElementsByTagName('button');
const cartChilds = document.getElementsByClassName('cartChild');

let firstImgAdded = false;
let secondImgAdded = false;
let thirdImgAdded = false;
let fourthImgAdded = false;
let fifthImgAdded = false;

btns[0].addEventListener('click', function(){
    if (!firstImgAdded){
        const newImg = document.createElement('img');
        newImg.src = 'images/0.png';

        newSpan0 = document.createElement('span');
        newSpan0.textContent = 1;

        const newP = document.createElement('p');
        newP.textContent = 'Quantity: ';
        newP.appendChild(newSpan0);

        cartChilds[0].append(newImg, newP);
        firstImgAdded = true;
    } else{
        newSpan0.textContent++;   
    }
})

btns[1].addEventListener('click', function(){
    if (!secondImgAdded){       
        const newImg = document.createElement('img');
        newImg.src = 'images/1.png';

        newSpan1 = document.createElement('span');
        newSpan1.textContent = 1;

        const newP = document.createElement('p');
        newP.textContent = 'Quantity: ';
        newP.appendChild(newSpan1);

        cartChilds[1].append(newImg, newP);
        secondImgAdded = true;
    } else{
        newSpan1.textContent++;   
    }
})

btns[2].addEventListener('click', function(){
    if (!thirdImgAdded){
        const newImg = document.createElement('img');
        newImg.src = 'images/2.png';

        newSpan2 = document.createElement('span');
        newSpan2.textContent = 1;
        
        const newP = document.createElement('p');
        newP.textContent = 'Quantity: ';
        newP.appendChild(newSpan2);

        cartChilds[2].append(newImg, newP);
        thirdImgAdded = true;
    } else{
        newSpan2.textContent++;   
    }
})

btns[3].addEventListener('click', function(e){
    if (!fourthImgAdded){
        const newImg = document.createElement('img');
        newImg.src = 'images/3.png';

        newSpan3 = document.createElement('span');
        newSpan3.textContent = 1;

        const newP = document.createElement('p');
        newP.textContent = 'Quantity: ';
        newP.appendChild(newSpan3);

        cartChilds[3].append(newImg, newP);
        fourthImgAdded = true;
    } else{
        newSpan3.textContent++;   
    }
})

btns[4].addEventListener('click', function(e){
    if (!fifthImgAdded){  
        const newImg = document.createElement('img');
        newImg.src = 'images/4.png';

        newSpan4 = document.createElement('span');
        newSpan4.textContent = 1;

        const newP = document.createElement('p');
        newP.textContent = 'Quantity: ';
        newP.appendChild(newSpan4);

        cartChilds[4].append(newImg, newP);
        fifthImgAdded = true;
    } else{
        newSpan4.textContent++;   
    }
})