const arr = [
    product1 = {
        id: 'firstProduct',
        name: 'Product 1',
        src: 'images/0.png',
        width: '100',
    },
    product2 = {
        id: 'secondProduct',
        name: 'Product 2',
        src: 'images/1.png',
        width: '100',
    },
    product3 = {
        id: 'thirdProduct',
        name: 'Product 3',
        src: 'images/2.png',
        width: '100',
    }
];

const mainDiv = document.getElementById('mainDiv');
window.onload = addProducts;

function addProducts(){
    for (let i = 0; i <= arr.length; i++){
        const currentProduct = arr[i];

        const newImg = document.createElement('img');
        newImg.src = currentProduct['src'];
        newImg.width = currentProduct['width'];
        
        const newP = document.createElement('p');
        newP.id = currentProduct['id'];
        newP.textContent = currentProduct['name'];

        const newDiv = document.createElement('div');
        newDiv.append(newImg, newP);
        mainDiv.appendChild(newDiv);
    }
}