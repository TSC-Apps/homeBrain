const dataController = (function () {

})();

const UIcontroller = (function () {
    const DOMstrings = {
        selectMonth: '.select-months',
        selectItemType: '.select-type',
        inputItemName: '#name',
        inputItemValue: '#value',
        inputItemDate: '#date',
        btnAdd: '.btn-add',
        btnSmallMenu: '#ico-small-menu',
        smallMenuContent: '#small-menu',
        btnSmallMenuClose: '#btn-small-menu-close'
    };

    return {
        clearInputs: function() {
            const inputs = Array.from(document.querySelectorAll(DOMstrings.inputItemName + ', ' + DOMstrings.inputItemValue + ', ' + DOMstrings.inputItemDate));

            setTimeout(() => {
                inputs.forEach(current => {
                    current.value = '';
                });
            }, 100);

            document.querySelector(DOMstrings.inputItemDate).valueAsDate = new Date();

            inputs[0].focus();
        },

        setInitialDate: function() {
            document.querySelector(DOMstrings.inputItemDate).valueAsDate = new Date();
        },

        getDOMstrings: function() {
            return DOMstrings;
        }
    };
})();




const controller = (function (dataCtrl, UICtrl) {
    let DOM ;

    function toggleSmallMenu() {
        document.querySelector(DOM.smallMenuContent).classList.toggle('visible');
    }

    function setUpDOM() {
        DOM = UICtrl.getDOMstrings();

        document.querySelector(DOM.btnSmallMenu).addEventListener('click', toggleSmallMenu);
        document.querySelector(DOM.btnSmallMenuClose).addEventListener('click', toggleSmallMenu);
        document.querySelector(DOM.btnAdd).addEventListener('click', function() {
            UICtrl.clearInputs();
        });
    }

    return {
        initialize: function() {
            setUpDOM();
            UICtrl.setInitialDate();
        },
    };
})(dataController, UIcontroller);

controller.initialize();
