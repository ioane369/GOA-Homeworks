const imgSources = ['images/0.png', 'images/1.png', 'images/2.png', 'images/3.png', 'images/0.png', 'images/1.png', 'images/2.png', 'images/3.png'];
const img = document.getElementById('img');
const btns = document.getElementsByTagName('button');
const previousBtn = btns[0];
const nextBtn = btns[1];


nextBtn.addEventListener('click', function(){
    const currentIndex = imgSources.indexOf(img.getAttribute('src'));
    img.src = imgSources[currentIndex + 1];
});

previousBtn.addEventListener('click', function(){
    const currentIndex = imgSources.indexOf(img.getAttribute('src'), 1);
    img.src = imgSources[currentIndex - 1];
});