var dataController = (function () {


})();




var UIcontroller = (function () {

    var DOMstrings = {
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
        getInputValues: function() {
            return {
                type: document.querySelector(DOMstrings.selectItemType).value,
                name: document.querySelector(DOMstrings.inputItemName).value,
                value: document.querySelector(DOMstrings.inputItemValue).value,
                date: document.querySelector(DOMstrings.inputItemDate).value,
            };
        },

        getDOMstrings: function() {
            return DOMstrings;
        }
    };
})();




var controller = (function (dataCtrl, UICtrl) {

    var DOM = UICtrl.getDOMstrings();

    function toggleSmallMenu() {
        document.querySelector(DOM.smallMenuContent).classList.toggle('visible');
    }

    document.querySelector(DOM.btnSmallMenu).addEventListener('click', toggleSmallMenu);
    document.querySelector(DOM.btnSmallMenuClose).addEventListener('click', toggleSmallMenu);
    
    document.querySelector(DOM.btnAdd).addEventListener('click', function() {
        var values = UICtrl.getInputValues();
        console.log(values);
    });

    return {
        initialize: function() {
            console.log('App has been initialized.');
        }
    };
})(dataController, UIcontroller);

controller.initialize();
