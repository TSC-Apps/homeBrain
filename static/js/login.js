const DOM = {
    btnCloseFlash: '.btn-close-flash',
    flashMessage: '.flash-message'
};

// close the flash message
document.querySelector(DOM.flashMessage).addEventListener('click', event => {
    if (event.target.className === 'fas fa-times btn-close-modal btn-close-flash') {
        document.querySelector(DOM.flashMessage).style.display = 'none';
    }
});


