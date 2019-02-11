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
        clearInputs: function() {
            document.querySelector(DOMstrings.inputItemName).value = '';
            document.querySelector(DOMstrings.inputItemValue).value = '';
            document.querySelector(DOMstrings.inputItemDate).value = '';
            document.querySelector(DOMstrings.inputItemDate).valueAsDate = new Date()
        },

        setInitialDate: function() {
            document.querySelector(DOMstrings.inputItemDate).valueAsDate = new Date();
        },

        getMonth: function() {
            return document.querySelector(DOMstrings.selectMonth).value;
        },

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
    //var month = UICtrl.getMonth();

    var expenses = [];
    var income = [];

    function toggleSmallMenu() {
        document.querySelector(DOM.smallMenuContent).classList.toggle('visible');
    }

    document.querySelector(DOM.btnSmallMenu).addEventListener('click', toggleSmallMenu);
    document.querySelector(DOM.btnSmallMenuClose).addEventListener('click', toggleSmallMenu);
    
    document.querySelector(DOM.btnAdd).addEventListener('click', function() {
        var values = UICtrl.getInputValues();
        UICtrl.clearInputs();
        if(values.type === 'expense') {
            expenses.push(values);
        } else {
            income.push(values);
        }
    });

    return {
        initialize: function() {
            UICtrl.setInitialDate();
            console.log('App has been initialized.');
        },

        getIncome: function() {
            return income;
        },

        getExpenses: function() {
            return expenses;
        }
    };
})(dataController, UIcontroller);

controller.initialize();
