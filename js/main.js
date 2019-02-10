//================================================
// Assigning DOM elements to variables

var btnSmallMenu = document.getElementById('ico-small-menu');
var smallMenu = document.getElementById('small-menu');
var smallMenuLi = document.querySelector('.small-menu-li');
var btnSmallMenuClose = document.getElementById('btn-small-menu-close');

//================================================
// Small menu

btnSmallMenu.addEventListener('click', function(){
    smallMenu.style.display = 'block';
});

smallMenuLi.addEventListener('click', function() {
    smallMenu.style.display = 'none';
});

// Close "small menu" button
btnSmallMenuClose.addEventListener('click', function() {
    smallMenu.style.display = 'none';
});