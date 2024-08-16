const selectColor = document.getElementById('selectColor');

function changeTextColor() {
    targetDiv.style.color = selectColor.value;;
}

selectColor.addEventListener('change', changeTextColor);