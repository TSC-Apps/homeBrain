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
        setInitialDate: function() {
            document.querySelector(DOMstrings.inputItemDate).valueAsDate = new Date();
        },

        getDOMstrings: function() {
            return DOMstrings;
        }
    };
})();




const controller = (function (dataCtrl, UICtrl) {
    let DOM;

    function toggleSmallMenu() {
        document.querySelector(DOM.smallMenuContent).classList.toggle('visible');
    }

    function setUpDOM() {
        DOM = UICtrl.getDOMstrings();

        document.querySelector(DOM.btnSmallMenu).addEventListener('click', toggleSmallMenu);
        document.querySelector(DOM.btnSmallMenuClose).addEventListener('click', toggleSmallMenu);

        document.querySelector(DOM.selectItemType).addEventListener('change', () => {
            const inputs = document.querySelectorAll('.input');
            const arrInputs = Array.from(inputs);

            arrInputs.forEach(current => {
                current.classList.toggle('input-income');
            })
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
